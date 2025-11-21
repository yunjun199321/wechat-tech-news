#!/usr/bin/env python3
"""
Initialize a new Claude Code marketplace structure.

Usage:
    python init_marketplace.py <marketplace-name> [--path <output-directory>]
"""

import argparse
import json
import os
import sys
from pathlib import Path


def validate_name(name: str) -> bool:
    """Validate marketplace name follows kebab-case convention."""
    if not name:
        return False
    # Must be lowercase with hyphens only
    valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-')
    return all(c in valid_chars for c in name) and not name.startswith('-') and not name.endswith('-')


def create_marketplace_structure(marketplace_name: str, output_path: Path):
    """Create the marketplace directory structure and files."""

    # Create main marketplace directory
    marketplace_dir = output_path / marketplace_name
    if marketplace_dir.exists():
        print(f"❌ Error: Directory '{marketplace_dir}' already exists")
        sys.exit(1)

    print(f"🚀 Initializing marketplace: {marketplace_name}")
    print(f"   Location: {marketplace_dir}")
    print()

    # Create directory structure
    marketplace_dir.mkdir(parents=True)
    claude_plugin_dir = marketplace_dir / ".claude-plugin"
    claude_plugin_dir.mkdir()

    # Create marketplace.json
    marketplace_json = {
        "name": marketplace_name,
        "owner": {
            "name": "Your Name",
            "email": "your.email@example.com"
        },
        "metadata": {
            "description": "Brief description of your marketplace",
            "version": "0.1.0",
            "license": "MIT",
            "repository": f"https://github.com/your-org/{marketplace_name}",
            "keywords": []
        },
        "plugins": []
    }

    marketplace_json_path = claude_plugin_dir / "marketplace.json"
    with open(marketplace_json_path, 'w') as f:
        json.dump(marketplace_json, f, indent=2)
    print(f"✅ Created {marketplace_json_path.relative_to(output_path)}")

    # Create README.md
    readme_content = f"""# {marketplace_name}

[Add marketplace description here]

## Installation

To install this marketplace in Claude Code:

```bash
# Clone the repository
git clone https://github.com/your-org/{marketplace_name}

# [Add specific installation instructions]
```

## Available Plugins

[List plugins here as they are added]

## Usage

[Add usage examples here]

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- GitHub Issues: https://github.com/your-org/{marketplace_name}/issues
- Email: your.email@example.com

## Changelog

### Version 0.1.0
- Initial marketplace structure created
"""

    readme_path = marketplace_dir / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    print(f"✅ Created {readme_path.relative_to(output_path)}")

    # Create .gitignore
    gitignore_content = """# Environment files
.env
.env.local

# User-specific files
.DS_Store
*.log

# IDE files
.vscode/
.idea/

# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# Temporary files
*.tmp
*.swp
~*

# OS
Thumbs.db
"""

    gitignore_path = marketplace_dir / ".gitignore"
    with open(gitignore_path, 'w') as f:
        f.write(gitignore_content)
    print(f"✅ Created {gitignore_path.relative_to(output_path)}")

    # Create LICENSE
    license_content = """MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    license_path = marketplace_dir / "LICENSE"
    with open(license_path, 'w') as f:
        f.write(license_content)
    print(f"✅ Created {license_path.relative_to(output_path)}")

    # Create CHANGELOG.md
    changelog_content = """# Changelog

All notable changes to this marketplace will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - [DATE]

### Added
- Initial marketplace structure
- README and documentation
"""

    changelog_path = marketplace_dir / "CHANGELOG.md"
    with open(changelog_path, 'w') as f:
        f.write(changelog_content)
    print(f"✅ Created {changelog_path.relative_to(output_path)}")

    print()
    print(f"✅ Marketplace '{marketplace_name}' initialized successfully at {marketplace_dir}")
    print()
    print("Next steps:")
    print(f"1. cd {marketplace_dir}")
    print("2. Update marketplace.json with your information (owner, description, repository)")
    print("3. Add your first plugin using the add_plugin.py script")
    print("4. Update README.md with marketplace details")
    print("5. Validate the marketplace structure using validate_marketplace.py")


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new Claude Code marketplace structure"
    )
    parser.add_argument(
        "marketplace_name",
        help="Name of the marketplace (kebab-case, e.g., 'my-marketplace')"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Output directory (default: current directory)"
    )

    args = parser.parse_args()

    # Validate marketplace name
    if not validate_name(args.marketplace_name):
        print("❌ Error: Invalid marketplace name")
        print("   Marketplace name must:")
        print("   - Use lowercase letters")
        print("   - Use hyphens to separate words (kebab-case)")
        print("   - Not start or end with a hyphen")
        print()
        print("   Examples: 'my-marketplace', 'productivity-tools', 'dev-utilities'")
        sys.exit(1)

    output_path = Path(args.path).resolve()
    if not output_path.exists():
        print(f"❌ Error: Output directory '{output_path}' does not exist")
        sys.exit(1)

    create_marketplace_structure(args.marketplace_name, output_path)


if __name__ == "__main__":
    main()
