#!/usr/bin/env python3
"""
Validate a Claude Code marketplace structure and configuration.

Usage:
    python validate_marketplace.py <marketplace-directory>
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Tuple


class MarketplaceValidator:
    def __init__(self, marketplace_dir: Path):
        self.marketplace_dir = marketplace_dir
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.marketplace_json = None

    def error(self, message: str):
        """Add an error message."""
        self.errors.append(f"❌ ERROR: {message}")

    def warning(self, message: str):
        """Add a warning message."""
        self.warnings.append(f"⚠️  WARNING: {message}")

    def validate(self) -> bool:
        """Run all validation checks. Returns True if valid."""
        print(f"🔍 Validating marketplace at: {self.marketplace_dir}")
        print()

        # Check if directory exists
        if not self.marketplace_dir.exists():
            self.error(f"Marketplace directory does not exist: {self.marketplace_dir}")
            return False

        if not self.marketplace_dir.is_dir():
            self.error(f"Path is not a directory: {self.marketplace_dir}")
            return False

        # Run validation checks
        self.check_marketplace_json()

        if self.marketplace_json:
            self.check_owner_info()
            self.check_metadata()
            self.check_plugins()

        # Print results
        print()
        if self.warnings:
            print("Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()

        if self.errors:
            print("Errors:")
            for error in self.errors:
                print(f"  {error}")
            print()
            print("❌ Validation failed")
            return False

        print("✅ Validation passed successfully!")
        if self.warnings:
            print(f"   ({len(self.warnings)} warning(s))")
        return True

    def check_marketplace_json(self):
        """Validate marketplace.json exists and is valid JSON."""
        marketplace_json_path = self.marketplace_dir / ".claude-plugin" / "marketplace.json"

        if not marketplace_json_path.exists():
            self.error("marketplace.json not found at .claude-plugin/marketplace.json")
            return

        print("✓ marketplace.json exists")

        try:
            with open(marketplace_json_path, 'r') as f:
                self.marketplace_json = json.load(f)
            print("✓ marketplace.json is valid JSON")
        except json.JSONDecodeError as e:
            self.error(f"marketplace.json is invalid JSON: {e}")
            return

        # Check required top-level fields
        required_fields = ['name', 'owner', 'metadata', 'plugins']
        for field in required_fields:
            if field not in self.marketplace_json:
                self.error(f"Missing required field in marketplace.json: '{field}'")

    def check_owner_info(self):
        """Validate owner information."""
        owner = self.marketplace_json.get('owner', {})

        if not isinstance(owner, dict):
            self.error("'owner' field must be an object")
            return

        # Check required owner fields
        if 'name' not in owner:
            self.error("Missing required field: owner.name")
        elif not owner['name'] or owner['name'] == "Your Name":
            self.warning("owner.name should be updated with actual name")

        if 'email' not in owner:
            self.error("Missing required field: owner.email")
        elif not owner['email'] or owner['email'] == "your.email@example.com":
            self.warning("owner.email should be updated with actual email")
        elif not self.validate_email(owner['email']):
            self.error(f"Invalid email format: {owner['email']}")

        print("✓ Owner information structure is valid")

    def check_metadata(self):
        """Validate metadata section."""
        metadata = self.marketplace_json.get('metadata', {})

        if not isinstance(metadata, dict):
            self.error("'metadata' field must be an object")
            return

        # Check required metadata fields
        if 'description' not in metadata:
            self.error("Missing required field: metadata.description")
        else:
            desc = metadata['description']
            if not desc or desc == "Brief description of your marketplace":
                self.warning("metadata.description should be updated with actual description")
            elif len(desc) < 20:
                self.warning(f"metadata.description is too short ({len(desc)} chars). Aim for 50-200 characters.")
            elif len(desc) > 200:
                self.warning(f"metadata.description is too long ({len(desc)} chars). Aim for 50-200 characters.")

        if 'version' not in metadata:
            self.error("Missing required field: metadata.version")
        elif not self.validate_semver(metadata['version']):
            self.error(f"Invalid semantic version: {metadata['version']}")

        # Optional but recommended fields
        if 'license' not in metadata:
            self.warning("Consider adding metadata.license field")
        if 'repository' not in metadata:
            self.warning("Consider adding metadata.repository field")
        elif metadata.get('repository', '').startswith('https://github.com/your-org/'):
            self.warning("metadata.repository should be updated with actual repository URL")

        print("✓ Metadata structure is valid")

    def check_plugins(self):
        """Validate plugins array and plugin configurations."""
        plugins = self.marketplace_json.get('plugins', [])

        if not isinstance(plugins, list):
            self.error("'plugins' field must be an array")
            return

        if len(plugins) == 0:
            self.warning("No plugins defined in marketplace.json")
            return

        print(f"✓ Found {len(plugins)} plugin(s)")

        plugin_names = set()
        for idx, plugin in enumerate(plugins):
            if not isinstance(plugin, dict):
                self.error(f"Plugin at index {idx} is not an object")
                continue

            self.check_plugin(plugin, idx, plugin_names)

    def check_plugin(self, plugin: dict, idx: int, plugin_names: set):
        """Validate individual plugin configuration."""
        # Check required plugin fields
        required_fields = ['name', 'description', 'source', 'skills']
        for field in required_fields:
            if field not in plugin:
                self.error(f"Plugin at index {idx} missing required field: '{field}'")

        plugin_name = plugin.get('name', f'plugin-{idx}')

        # Check for duplicate plugin names
        if plugin_name in plugin_names:
            self.error(f"Duplicate plugin name: '{plugin_name}'")
        plugin_names.add(plugin_name)

        # Validate plugin name format
        if plugin_name and not self.validate_name(plugin_name):
            self.error(f"Plugin '{plugin_name}' has invalid name format (must be kebab-case)")

        # Validate description
        desc = plugin.get('description', '')
        if not desc:
            self.error(f"Plugin '{plugin_name}' has empty description")
        elif len(desc) < 20:
            self.warning(f"Plugin '{plugin_name}' description is too short ({len(desc)} chars)")
        elif len(desc) > 200:
            self.warning(f"Plugin '{plugin_name}' description is too long ({len(desc)} chars)")

        # Validate source path
        source = plugin.get('source', '')
        if not source:
            self.error(f"Plugin '{plugin_name}' has empty source path")

        # Validate skills array
        skills = plugin.get('skills', [])
        if not isinstance(skills, list):
            self.error(f"Plugin '{plugin_name}' skills field must be an array")
        elif len(skills) == 0:
            self.error(f"Plugin '{plugin_name}' has no skills defined")
        else:
            self.check_skills(plugin_name, skills)

        print(f"  ✓ Plugin '{plugin_name}' structure is valid")

    def check_skills(self, plugin_name: str, skills: List[str]):
        """Validate skill paths exist and contain proper SKILL.md files."""
        for skill_path in skills:
            if not isinstance(skill_path, str):
                self.error(f"Plugin '{plugin_name}' has non-string skill path")
                continue

            # Resolve skill directory
            # Remove leading ./ if present
            clean_path = skill_path[2:] if skill_path.startswith('./') else skill_path
            skill_dir = self.marketplace_dir / clean_path

            if not skill_dir.exists():
                self.error(f"Plugin '{plugin_name}' skill path does not exist: {skill_path}")
                continue

            if not skill_dir.is_dir():
                self.error(f"Plugin '{plugin_name}' skill path is not a directory: {skill_path}")
                continue

            # Check for SKILL.md
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                self.error(f"Plugin '{plugin_name}' skill missing SKILL.md: {skill_path}")
                continue

            # Validate SKILL.md has YAML frontmatter
            self.check_skill_md(plugin_name, skill_path, skill_md)

    def check_skill_md(self, plugin_name: str, skill_path: str, skill_md: Path):
        """Validate SKILL.md file has proper YAML frontmatter."""
        try:
            with open(skill_md, 'r') as f:
                content = f.read()

            # Check for YAML frontmatter
            if not content.startswith('---'):
                self.error(f"Plugin '{plugin_name}' skill '{skill_path}' SKILL.md missing YAML frontmatter")
                return

            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.error(f"Plugin '{plugin_name}' skill '{skill_path}' SKILL.md has malformed YAML frontmatter")
                return

            frontmatter = parts[1].strip()

            # Basic check for required fields (simple regex, not full YAML parsing)
            if not re.search(r'name\s*:', frontmatter):
                self.error(f"Plugin '{plugin_name}' skill '{skill_path}' SKILL.md frontmatter missing 'name' field")

            if not re.search(r'description\s*:', frontmatter):
                self.error(f"Plugin '{plugin_name}' skill '{skill_path}' SKILL.md frontmatter missing 'description' field")

        except Exception as e:
            self.error(f"Plugin '{plugin_name}' skill '{skill_path}' SKILL.md could not be read: {e}")

    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate name follows kebab-case convention."""
        if not name:
            return False
        valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-')
        return all(c in valid_chars for c in name) and not name.startswith('-') and not name.endswith('-')

    @staticmethod
    def validate_email(email: str) -> bool:
        """Basic email validation."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_semver(version: str) -> bool:
        """Validate semantic version format."""
        pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$'
        return bool(re.match(pattern, version))


def main():
    parser = argparse.ArgumentParser(
        description="Validate a Claude Code marketplace structure"
    )
    parser.add_argument(
        "marketplace_dir",
        help="Path to marketplace directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )

    args = parser.parse_args()

    marketplace_dir = Path(args.marketplace_dir).resolve()
    validator = MarketplaceValidator(marketplace_dir)

    is_valid = validator.validate()

    # In strict mode, warnings count as failures
    if args.strict and validator.warnings:
        print()
        print("❌ Validation failed in strict mode due to warnings")
        is_valid = False

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
