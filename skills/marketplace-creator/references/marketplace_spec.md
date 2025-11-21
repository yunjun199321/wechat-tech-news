# Marketplace Specification

## Overview

A Claude Code marketplace is a distribution system for plugins and skills. It consists of a standardized directory structure and a `marketplace.json` file that catalogs all available plugins.

## Directory Structure

```
marketplace-name/
├── .claude-plugin/
│   └── marketplace.json          # Required: Marketplace catalog
├── plugin-1/                      # Plugin directories
│   ├── SKILL.md                  # Skill definitions
│   ├── scripts/
│   ├── references/
│   └── assets/
├── plugin-2/
│   └── ...
└── README.md                      # Recommended: Marketplace documentation
```

## marketplace.json Structure

### Required Fields

```json
{
  "name": "marketplace-name",
  "owner": {
    "name": "Owner Name",
    "email": "owner@example.com"
  },
  "metadata": {
    "description": "Brief description",
    "version": "1.0.0"
  },
  "plugins": []
}
```

### Plugin Entry Structure

Each plugin in the `plugins` array must have:

```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "source": "./path/to/plugin",
  "strict": false,
  "skills": [
    "./path/to/skill-1",
    "./path/to/skill-2"
  ]
}
```

#### Field Descriptions

- **name** (required): Unique identifier for the plugin within the marketplace
  - Must be lowercase with hyphens
  - Example: `document-skills`, `example-skills`

- **description** (required): Clear, concise description of the plugin's capabilities
  - Should summarize all included skills
  - Length: 50-200 characters

- **source** (required): Relative path to plugin directory
  - Usually `"./"` for marketplace root
  - Can point to subdirectories for organized structures

- **strict** (optional): Validation mode
  - `false` (default): Lenient validation
  - `true`: Strict validation of skill structure

- **skills** (required): Array of skill paths
  - Paths relative to plugin source
  - Each path should point to a directory containing SKILL.md
  - Example: `["./skill-name"]` or `["./category/skill-name"]`

## Complete Example

```json
{
  "name": "wechat-tech-news",
  "owner": {
    "name": "Community Contributors",
    "email": "support@wechat-tech-news.dev"
  },
  "metadata": {
    "description": "Automated tech news research and WeChat formatting suite",
    "version": "1.0.0",
    "license": "MIT",
    "repository": "https://github.com/your-org/wechat-tech-news",
    "keywords": ["wechat", "tech-news", "research"]
  },
  "plugins": [
    {
      "name": "wechat-tech-news",
      "description": "Three-skill suite: tech news research, WeChat compliance optimization, and workflow orchestration",
      "source": "./",
      "strict": false,
      "skills": [
        "./daily-tech-news-search",
        "./wechat-tech-news-writer",
        "./tech-news-workflow"
      ]
    }
  ]
}
```

## Optional Metadata Fields

Additional metadata fields can be included:

- **license**: Software license (e.g., "MIT", "Apache-2.0")
- **repository**: Git repository URL
- **keywords**: Array of search keywords
- **homepage**: Plugin documentation URL
- **documentation**: Link to detailed docs
- **tags**: Categorization tags

## Naming Conventions

### Marketplace Names
- Use kebab-case: `my-marketplace-name`
- Be descriptive and unique
- Avoid generic names

### Plugin Names
- Use kebab-case: `my-plugin-name`
- Reflect functionality clearly
- Keep concise (2-4 words)

### Skill Paths
- Use kebab-case for directories
- Organize by category if needed
- Examples:
  - `./skill-name`
  - `./category/skill-name`
  - `./tools/pdf-editor`

## Validation Rules

### Required Validations

1. **marketplace.json must exist** in `.claude-plugin/` directory
2. **All required fields** must be present
3. **Plugin names must be unique** within marketplace
4. **All skill paths** must point to valid directories containing SKILL.md
5. **Email format** must be valid in owner field
6. **Version** must follow semantic versioning (e.g., "1.0.0")

### Recommended Validations

1. **Description quality**: Clear, informative, appropriate length
2. **Path validity**: All relative paths resolve correctly
3. **Skill structure**: Each skill directory contains proper SKILL.md with YAML frontmatter
4. **No orphaned directories**: All skill directories are referenced in marketplace.json
5. **Consistent naming**: Follow kebab-case conventions throughout

## Best Practices

### Organization

1. **Group related skills into plugins** rather than creating many single-skill plugins
2. **Use clear hierarchies** if you have many skills (e.g., `document-skills/pdf`, `document-skills/xlsx`)
3. **Keep marketplace.json clean** - one plugin entry per logical grouping

### Documentation

1. **Include comprehensive README.md** at marketplace root
2. **Document each plugin's purpose** and capabilities
3. **Provide usage examples** for common workflows
4. **List dependencies** and prerequisites

### Versioning

1. **Follow semantic versioning** (MAJOR.MINOR.PATCH)
2. **Update version** when adding/removing plugins or skills
3. **Document changes** in CHANGELOG.md or release notes
4. **Breaking changes** require major version bump

### Maintenance

1. **Validate regularly** using validation scripts
2. **Test skills** before publishing updates
3. **Respond to issues** from marketplace users
4. **Keep metadata current** (version, repository links, etc.)

## Common Patterns

### Single Plugin Marketplace

Simple marketplace with one plugin containing multiple skills:

```json
{
  "name": "my-tools",
  "plugins": [{
    "name": "my-tools",
    "skills": ["./skill-1", "./skill-2", "./skill-3"]
  }]
}
```

### Multi-Plugin Marketplace

Marketplace organizing skills into logical plugin groups:

```json
{
  "name": "productivity-suite",
  "plugins": [
    {
      "name": "document-tools",
      "skills": ["./pdf", "./xlsx", "./docx"]
    },
    {
      "name": "automation-tools",
      "skills": ["./workflow", "./scheduler"]
    }
  ]
}
```

### Category-Based Organization

Plugins with hierarchical skill organization:

```json
{
  "name": "dev-tools",
  "plugins": [{
    "name": "dev-tools",
    "skills": [
      "./frontend/react-builder",
      "./frontend/css-optimizer",
      "./backend/api-generator",
      "./backend/db-migrator"
    ]
  }]
}
```

## Troubleshooting

### Common Issues

**"Skill not found" errors**
- Verify skill path in marketplace.json matches actual directory
- Check that SKILL.md exists in skill directory
- Ensure paths are relative to plugin source

**"Invalid marketplace.json" errors**
- Validate JSON syntax (no trailing commas, proper quotes)
- Verify all required fields present
- Check that skill arrays are not empty

**Skills not loading**
- Confirm SKILL.md has proper YAML frontmatter
- Check file permissions are readable
- Verify no circular dependencies

**Version conflicts**
- Ensure version follows semantic versioning
- Check for incompatible Claude Code version requirements
- Verify no duplicate plugin names across marketplaces
