#!/usr/bin/env python3
"""
Add a new plugin to an existing marketplace.

Usage:
    python add_plugin.py <marketplace-dir> --name <plugin-name> --description <desc> --skills <skill-paths>
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List


def validate_name(name: str) -> bool:
    """Validate plugin name follows kebab-case convention."""
    if not name:
        return False
    valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-')
    return all(c in valid_chars for c in name) and not name.startswith('-') and not name.endswith('-')


def load_marketplace_json(marketplace_dir: Path) -> dict:
    """Load marketplace.json from the marketplace directory."""
    marketplace_json_path = marketplace_dir / ".claude-plugin" / "marketplace.json"

    if not marketplace_json_path.exists():
        print(f"❌ Error: marketplace.json not found at {marketplace_json_path}")
        sys.exit(1)

    try:
        with open(marketplace_json_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in marketplace.json: {e}")
        sys.exit(1)


def save_marketplace_json(marketplace_dir: Path, data: dict):
    """Save marketplace.json with proper formatting."""
    marketplace_json_path = marketplace_dir / ".claude-plugin" / "marketplace.json"

    with open(marketplace_json_path, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')  # Add trailing newline


def verify_skill_paths(marketplace_dir: Path, skill_paths: List[str]) -> bool:
    """Verify that all skill paths exist and contain SKILL.md."""
    all_valid = True

    for skill_path in skill_paths:
        # Remove leading ./ if present
        clean_path = skill_path[2:] if skill_path.startswith('./') else skill_path
        skill_dir = marketplace_dir / clean_path

        if not skill_dir.exists():
            print(f"⚠️  Warning: Skill directory does not exist: {skill_path}")
            all_valid = False
            continue

        if not skill_dir.is_dir():
            print(f"⚠️  Warning: Skill path is not a directory: {skill_path}")
            all_valid = False
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            print(f"⚠️  Warning: SKILL.md not found in: {skill_path}")
            all_valid = False

    return all_valid


def add_plugin(
    marketplace_dir: Path,
    plugin_name: str,
    description: str,
    skill_paths: List[str],
    source: str = "./",
    strict: bool = False
):
    """Add a new plugin to the marketplace."""

    print(f"➕ Adding plugin '{plugin_name}' to marketplace")
    print()

    # Validate plugin name
    if not validate_name(plugin_name):
        print("❌ Error: Invalid plugin name")
        print("   Plugin name must:")
        print("   - Use lowercase letters")
        print("   - Use hyphens to separate words (kebab-case)")
        print("   - Not start or end with a hyphen")
        sys.exit(1)

    # Load marketplace.json
    marketplace_data = load_marketplace_json(marketplace_dir)

    # Check for duplicate plugin name
    existing_names = {p['name'] for p in marketplace_data.get('plugins', [])}
    if plugin_name in existing_names:
        print(f"❌ Error: Plugin '{plugin_name}' already exists in marketplace.json")
        sys.exit(1)

    # Normalize skill paths (ensure they start with ./)
    normalized_paths = []
    for path in skill_paths:
        if not path.startswith('./'):
            normalized_paths.append(f'./{path}')
        else:
            normalized_paths.append(path)

    # Verify skill paths
    print("Verifying skill paths...")
    all_valid = verify_skill_paths(marketplace_dir, normalized_paths)

    if not all_valid:
        print()
        response = input("Some skill paths have issues. Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(1)

    # Create plugin entry
    plugin_entry = {
        "name": plugin_name,
        "description": description,
        "source": source,
        "strict": strict,
        "skills": normalized_paths
    }

    # Add plugin to marketplace
    if 'plugins' not in marketplace_data:
        marketplace_data['plugins'] = []

    marketplace_data['plugins'].append(plugin_entry)

    # Save updated marketplace.json
    save_marketplace_json(marketplace_dir, marketplace_data)

    print()
    print(f"✅ Successfully added plugin '{plugin_name}'")
    print()
    print("Plugin configuration:")
    print(json.dumps(plugin_entry, indent=2))
    print()
    print("Next steps:")
    print("1. Verify the marketplace structure: python validate_marketplace.py <marketplace-dir>")
    print("2. Update README.md to document the new plugin")
    print("3. Test the plugin in Claude Code")


def main():
    parser = argparse.ArgumentParser(
        description="Add a plugin to a Claude Code marketplace"
    )
    parser.add_argument(
        "marketplace_dir",
        help="Path to marketplace directory"
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Plugin name (kebab-case, e.g., 'my-plugin')"
    )
    parser.add_argument(
        "--description",
        required=True,
        help="Plugin description (50-200 characters recommended)"
    )
    parser.add_argument(
        "--skills",
        required=True,
        nargs='+',
        help="Skill paths relative to marketplace root (e.g., './skill-name' or 'category/skill-name')"
    )
    parser.add_argument(
        "--source",
        default="./",
        help="Plugin source path (default: './')"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode for plugin validation"
    )

    args = parser.parse_args()

    marketplace_dir = Path(args.marketplace_dir).resolve()
    if not marketplace_dir.exists():
        print(f"❌ Error: Marketplace directory does not exist: {marketplace_dir}")
        sys.exit(1)

    # Check description length
    if len(args.description) < 20:
        print("⚠️  Warning: Description is very short (< 20 characters)")
        print("   Consider providing a more detailed description")
        print()

    if len(args.description) > 200:
        print("⚠️  Warning: Description is quite long (> 200 characters)")
        print("   Consider making it more concise")
        print()

    add_plugin(
        marketplace_dir,
        args.name,
        args.description,
        args.skills,
        args.source,
        args.strict
    )


if __name__ == "__main__":
    main()
