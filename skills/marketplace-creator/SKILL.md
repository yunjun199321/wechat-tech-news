---
name: marketplace-creator
description: Create and manage Claude Code marketplaces - initialize marketplace structure, validate configurations, add plugins, and ensure compliance with marketplace standards. Use when creating new marketplaces, publishing plugins, or validating existing marketplace configurations.
---

# Marketplace Creator

## Overview

Create and manage Claude Code marketplaces with comprehensive tooling for initialization, validation, and plugin management. This skill provides automated scripts, specification documentation, and templates for building professional, standards-compliant marketplaces.

## When to Use This Skill

Invoke this skill when the user:
- Requests to create a new marketplace
- Wants to publish a plugin to a marketplace
- Needs to validate marketplace structure or configuration
- Asks about marketplace specifications or best practices
- Mentions `marketplace.json` or marketplace-related operations
- Wants to add skills to an existing marketplace

## Core Capabilities

This skill provides four primary operations, each supported by dedicated scripts and documentation:

### 1. Initialize New Marketplace

Create a complete marketplace structure from scratch with proper directory layout and configuration files.

**Trigger phrases:**
- "Create a new marketplace"
- "Initialize marketplace"
- "Set up a marketplace for my plugins"

**Process:**

1. Run the initialization script:
   ```bash
   python scripts/init_marketplace.py <marketplace-name> --path <output-directory>
   ```

2. The script creates:
   - `.claude-plugin/marketplace.json` - Marketplace configuration
   - `README.md` - Marketplace documentation template
   - `LICENSE` - MIT license template
   - `CHANGELOG.md` - Version history template
   - `.gitignore` - Git ignore patterns

3. Prompt user to update:
   - Owner information (name, email)
   - Marketplace description
   - Repository URL
   - Keywords and metadata

**Example interaction:**
```
User: "Help me create a new marketplace called 'productivity-tools'"

1. Run: python scripts/init_marketplace.py productivity-tools --path ~/projects
2. Inform user: Marketplace created at ~/projects/productivity-tools
3. Guide next steps: Update owner info, add first plugin, validate structure
```

### 2. Validate Marketplace

Check marketplace structure, configuration, and compliance with standards.

**Trigger phrases:**
- "Validate my marketplace"
- "Check marketplace structure"
- "Is my marketplace.json correct?"

**Process:**

1. Run the validation script:
   ```bash
   python scripts/validate_marketplace.py <marketplace-directory>
   ```

2. The script validates:
   - `marketplace.json` exists and is valid JSON
   - All required fields present (name, owner, metadata, plugins)
   - Owner information format (name, email)
   - Metadata completeness (description, version)
   - Plugin configurations (names, descriptions, skills)
   - Skill paths resolve correctly
   - SKILL.md files exist with proper YAML frontmatter
   - Naming conventions (kebab-case)
   - Semantic versioning format

3. Reports:
   - ✅ Successful validations
   - ⚠️  Warnings (recommendations)
   - ❌ Errors (blocking issues)

**Strict mode:**
```bash
python scripts/validate_marketplace.py <marketplace-dir> --strict
```
Treats warnings as errors for production-ready validation.

**Example interaction:**
```
User: "Check if my marketplace is valid"

1. Ask for marketplace directory path
2. Run: python scripts/validate_marketplace.py <path>
3. Report validation results
4. If errors: Explain issues and provide fixes
5. If warnings: Suggest improvements
```

### 3. Add Plugin to Marketplace

Add a new plugin entry to an existing marketplace's configuration.

**Trigger phrases:**
- "Add a plugin to marketplace"
- "Publish my plugin"
- "Register skills in marketplace"

**Process:**

1. Gather required information:
   - Plugin name (kebab-case)
   - Description (50-200 characters recommended)
   - Skill paths (relative to marketplace root)

2. Run the add plugin script:
   ```bash
   python scripts/add_plugin.py <marketplace-dir> \
     --name <plugin-name> \
     --description "<description>" \
     --skills ./skill-1 ./skill-2
   ```

3. Optional parameters:
   - `--source <path>` - Plugin source directory (default: "./")
   - `--strict` - Enable strict validation mode

4. The script:
   - Validates plugin name format
   - Checks for duplicate names
   - Verifies skill paths exist
   - Confirms SKILL.md files present
   - Updates marketplace.json
   - Preserves JSON formatting

**Example interaction:**
```
User: "Add my document-tools plugin with pdf-editor and xlsx-analyzer skills"

1. Confirm marketplace directory
2. Gather plugin details:
   - Name: document-tools
   - Description: "Document processing suite for PDF and Excel files"
   - Skills: ./pdf-editor, ./xlsx-analyzer
3. Run: python scripts/add_plugin.py <marketplace-dir> \
       --name document-tools \
       --description "Document processing suite for PDF and Excel files" \
       --skills ./pdf-editor ./xlsx-analyzer
4. Confirm success and suggest validation
```

### 4. Provide Guidance and Best Practices

Reference comprehensive documentation for marketplace standards and recommendations.

**When to reference documentation:**
- User asks about marketplace specifications
- User needs naming conventions guidance
- User wants to understand plugin organization
- User inquires about versioning strategies

**Available reference documents:**

**`references/marketplace_spec.md`** - Complete marketplace specification:
- Directory structure requirements
- marketplace.json schema and fields
- Plugin entry structure
- Validation rules
- Naming conventions
- Complete examples

**`references/best_practices.md`** - Expert guidance:
- Planning marketplace scope
- Single vs. multiple plugins
- Directory organization patterns
- Writing quality descriptions
- Version management strategies
- Quality standards checklists
- Security considerations
- Distribution best practices

**Usage pattern:**
```
User: "How should I organize plugins in my marketplace?"

1. Reference: references/best_practices.md sections:
   - "Planning Your Marketplace"
   - "Structuring Plugins"
   - "Directory Organization"
2. Provide specific recommendations based on user's needs
3. Show relevant examples from the documentation
```

## Workflow Patterns

### Creating a Complete Marketplace

Follow this end-to-end workflow when user wants to build a marketplace from scratch:

1. **Initialize**: Run `init_marketplace.py` to create structure
2. **Configure**: Update marketplace.json with actual information
3. **Add Skills**: Ensure skill directories exist with SKILL.md files
4. **Register Plugin**: Run `add_plugin.py` to add skills to marketplace
5. **Validate**: Run `validate_marketplace.py` to check everything
6. **Document**: Update README.md with usage instructions
7. **Test**: Test loading marketplace in Claude Code

### Publishing Existing Plugin

When user has existing skills and wants to publish to marketplace:

1. **Locate/Create Marketplace**: Use existing or initialize new marketplace
2. **Verify Skills**: Ensure each skill has proper SKILL.md with frontmatter
3. **Add to Marketplace**: Run `add_plugin.py` with skill paths
4. **Validate**: Run `validate_marketplace.py` to ensure compliance
5. **Update Docs**: Update marketplace README with new plugin info

### Troubleshooting Issues

When user encounters validation errors or structural problems:

1. **Run Validation**: Get specific error messages
2. **Reference Spec**: Check `marketplace_spec.md` for requirements
3. **Fix Issues**: Address errors one by one
4. **Re-validate**: Confirm fixes resolve problems
5. **Check Best Practices**: Ensure following recommendations

## Templates and Assets

### Marketplace Templates

**`assets/templates/marketplace.json`** - Starter marketplace configuration with placeholders:
- Marketplace name
- Owner information
- Metadata fields
- Empty plugins array

Use this as reference when manually creating or explaining marketplace.json structure.

**`assets/templates/README.md`** - Marketplace documentation template with sections for:
- Installation instructions
- Available plugins listing
- Usage examples
- Contributing guidelines
- Support information

### Using Templates

Templates use `{{PLACEHOLDER}}` syntax for variable content. When helping users create marketplaces, replace placeholders with actual values:

```
{{MARKETPLACE_NAME}} → actual-marketplace-name
{{OWNER_NAME}} → John Doe
{{OWNER_EMAIL}} → john@example.com
{{REPOSITORY_URL}} → https://github.com/user/repo
```

## Common Scenarios

### Scenario 1: First-Time Marketplace Creator

User is new to marketplaces and wants to publish their skills.

**Approach:**
1. Explain marketplace concept and benefits
2. Guide through initialization process
3. Help organize skills into logical plugin(s)
4. Walk through adding plugin
5. Validate and test
6. Provide publishing guidance

### Scenario 2: Converting Standalone Skills

User has individual skills they want to marketplace-ify.

**Approach:**
1. Assess skill count and relationships
2. Recommend plugin organization (single vs. multiple)
3. Create marketplace structure
4. Add skills with appropriate grouping
5. Validate and document

### Scenario 3: Debugging Validation Errors

User's marketplace fails validation with errors.

**Approach:**
1. Run validation to capture specific errors
2. Categorize errors (structure, format, content)
3. Reference specification for requirements
4. Provide specific fixes for each error
5. Re-validate after fixes
6. Address warnings as recommendations

### Scenario 4: Expanding Existing Marketplace

User wants to add new plugins/skills to established marketplace.

**Approach:**
1. Validate current marketplace first
2. Add new plugin(s) using add_plugin.py
3. Ensure consistent naming and style
4. Update marketplace version (minor bump)
5. Re-validate entire marketplace
6. Update README and CHANGELOG

## Key Validation Rules

Understanding these rules helps anticipate and prevent errors:

### Required Structure
- `.claude-plugin/marketplace.json` must exist
- All plugin skill paths must resolve to directories
- Each skill directory must contain SKILL.md
- SKILL.md must have YAML frontmatter with name and description

### Required Fields
- marketplace.json: name, owner, metadata, plugins
- owner: name, email (valid format)
- metadata: description, version (semantic versioning)
- plugin: name, description, source, skills

### Naming Conventions
- Marketplace names: kebab-case (e.g., `my-marketplace`)
- Plugin names: kebab-case (e.g., `document-tools`)
- Skill directories: kebab-case (e.g., `pdf-editor`)
- Must not start or end with hyphen
- Only lowercase letters, numbers, and hyphens

### Best Practices
- Description length: 50-200 characters
- Plugin count: Start with 1-3, expand as needed
- Skill grouping: Related skills in same plugin
- Version format: MAJOR.MINOR.PATCH (e.g., 1.0.0)

## Error Messages and Solutions

### "marketplace.json not found"
**Cause:** Missing marketplace configuration file
**Solution:** Run `init_marketplace.py` or manually create `.claude-plugin/marketplace.json`

### "Invalid JSON in marketplace.json"
**Cause:** Syntax error in JSON file
**Solution:** Check for trailing commas, missing quotes, unmatched brackets

### "Skill path does not exist"
**Cause:** Plugin references non-existent skill directory
**Solution:** Create skill directory or fix path in marketplace.json

### "Missing SKILL.md"
**Cause:** Skill directory lacks required SKILL.md file
**Solution:** Create SKILL.md with proper YAML frontmatter

### "Invalid email format"
**Cause:** Owner email doesn't match email pattern
**Solution:** Use valid email format: user@domain.com

### "Invalid semantic version"
**Cause:** Version doesn't follow semver format
**Solution:** Use format MAJOR.MINOR.PATCH (e.g., 1.0.0)

### "Duplicate plugin name"
**Cause:** Multiple plugins with same name
**Solution:** Ensure unique plugin names across marketplace

## Script Reference

All scripts include `--help` for detailed usage:

```bash
python scripts/init_marketplace.py --help
python scripts/validate_marketplace.py --help
python scripts/add_plugin.py --help
```

### Quick Reference

**Initialize marketplace:**
```bash
python scripts/init_marketplace.py <name> --path <dir>
```

**Validate marketplace:**
```bash
python scripts/validate_marketplace.py <marketplace-dir> [--strict]
```

**Add plugin:**
```bash
python scripts/add_plugin.py <marketplace-dir> \
  --name <plugin-name> \
  --description "<desc>" \
  --skills ./skill-1 ./skill-2 [./skill-N...] \
  [--source <path>] \
  [--strict]
```

## Version Management Guidance

Help users understand when and how to update marketplace versions:

- All skills tested and functional
- Documentation complete
- No known critical bugs
- Ready for production use

**When to bump version:**
- MAJOR (1.0.0 → 2.0.0): Breaking changes, removed plugins/skills
- MINOR (1.0.0 → 1.1.0): New plugins/skills added, new features
- PATCH (1.0.0 → 1.0.1): Bug fixes, documentation updates

**After version bump:**
- Update marketplace.json version field
- Document changes in CHANGELOG.md
- Create git tag if using version control

## Tips for Success

**For New Marketplaces:**
- Start with clear purpose and target users
- Plan for 3-10 skills, not just 1-2
- Group related skills into plugins logically
- Write clear, specific descriptions
- Validate early and often

**For Plugin Organization:**
- Single plugin: Skills share common domain, used together
- Multiple plugins: Different domains, independent usage
- Hierarchical: Use subdirectories for > 10 skills

**For Quality:**
- Test each skill before publishing
- Keep descriptions informative (50-200 chars)
- Follow kebab-case consistently
- Maintain comprehensive README
- Respond to issues promptly

**For Maintenance:**
- Validate quarterly
- Update dependencies
- Track user feedback
- Keep documentation current
- Use semantic versioning
