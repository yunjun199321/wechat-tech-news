# Marketplace Best Practices

## Planning Your Marketplace

### Scope and Organization

**Start with clear purpose**
- Define what problem your marketplace solves
- Identify target users and their needs
- Plan for 3-10 related skills, not just 1-2
- Consider future growth and extensibility

**Group skills logically**
- Related functionality → Same plugin
- Different domains → Separate plugins
- Example: All document tools in `document-skills` plugin

**Naming strategy**
- Marketplace name: Broad, memorable (e.g., `productivity-tools`)
- Plugin names: Specific domains (e.g., `document-skills`, `web-automation`)
- Skill names: Clear actions (e.g., `pdf-editor`, `xlsx-analyzer`)

## Structuring Plugins

### Single vs. Multiple Plugins

**Use single plugin when:**
- All skills share common domain
- Skills often used together
- Total skills < 10
- Simple, focused marketplace

Example:
```json
{
  "name": "pdf-toolkit",
  "plugins": [{
    "name": "pdf-toolkit",
    "skills": ["./editor", "./merger", "./compressor"]
  }]
}
```

**Use multiple plugins when:**
- Skills span different domains
- Some skills rarely used together
- Total skills > 10
- Want independent versioning

Example:
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

### Directory Organization

**Flat structure** (recommended for < 10 skills):
```
marketplace/
├── .claude-plugin/marketplace.json
├── skill-1/
├── skill-2/
└── skill-3/
```

**Hierarchical structure** (for > 10 skills):
```
marketplace/
├── .claude-plugin/marketplace.json
├── documents/
│   ├── pdf-editor/
│   ├── xlsx-analyzer/
│   └── docx-formatter/
└── automation/
    ├── workflow-builder/
    └── task-scheduler/
```

## Writing Quality Descriptions

### Marketplace Description

**Good examples:**
- ✅ "Comprehensive document processing suite for PDF, Excel, Word, and PowerPoint files"
- ✅ "Automated tech news research and WeChat publishing workflow"
- ✅ "Web automation and testing toolkit with Playwright integration"

**Bad examples:**
- ❌ "Useful tools" (too vague)
- ❌ "This marketplace contains various skills for doing things" (no specific value)
- ❌ "Best marketplace ever created" (subjective, unhelpful)

### Plugin Description

**Formula:** "[Action/Purpose] + [Key capabilities] + [Target use case]"

**Good examples:**
- ✅ "Document processing suite including Excel, Word, PowerPoint, and PDF capabilities"
- ✅ "Three-skill suite: tech news research, compliance optimization, and workflow orchestration"
- ✅ "Browser automation toolkit for E2E testing, screenshots, and form interactions"

**Bad examples:**
- ❌ "Skills for documents" (incomplete)
- ❌ "Helps with various tasks" (vague)
- ❌ "Really great plugin" (subjective)

### Skill Descriptions (in SKILL.md)

**Third-person, specific, actionable:**
- ✅ "Create and manipulate PDF files with rotation, merging, and compression capabilities"
- ✅ "Transform tech news into WeChat-compliant articles with compliance optimization"
- ✅ "Automate browser interactions for testing, data extraction, and form submissions"

**Avoid:**
- ❌ First person: "Use this skill to..."
- ❌ Second person: "You can use this to..."
- ❌ Vague: "Helps with PDFs"

## Version Management

### Semantic Versioning

Follow [semver](https://semver.org/): `MAJOR.MINOR.PATCH`

**MAJOR version** (1.0.0 → 2.0.0):
- Breaking changes to skill interfaces
- Removal of plugins or skills
- Incompatible API changes

**MINOR version** (1.0.0 → 1.1.0):
- New plugins or skills added
- New features, backward compatible
- Enhancements to existing functionality

**PATCH version** (1.0.0 → 1.0.1):
- Bug fixes
- Documentation updates
- Minor improvements
- No new features or functionality

### When to Bump Version

**Always update version when:**
- Adding/removing plugins or skills
- Changing skill behavior or interfaces
- Updating dependencies
- Publishing to users

- All skills tested and working
- Documentation complete
- No known critical bugs
- Ready for production use

**Pre-1.0.0 versions:**
- 0.1.0: Initial development
- 0.5.0: Feature complete, testing
- 0.9.0: Release candidate

## Quality Standards

### Before Publishing

**Validation checklist:**
- [ ] marketplace.json validates successfully
- [ ] All skill paths resolve correctly
- [ ] Every SKILL.md has proper YAML frontmatter
- [ ] No syntax errors in JSON
- [ ] All required fields present
- [ ] Descriptions are clear and helpful

**Testing checklist:**
- [ ] Each skill loads in Claude Code
- [ ] Skills trigger appropriately
- [ ] Bundled scripts execute without errors
- [ ] Reference docs are accessible
- [ ] Assets load correctly
- [ ] No broken links in documentation

**Documentation checklist:**
- [ ] README.md is comprehensive
- [ ] Each skill has clear instructions
- [ ] Usage examples provided
- [ ] Installation steps documented
- [ ] Troubleshooting section included

### Maintenance

**Regular tasks:**
- Test skills quarterly
- Update dependencies
- Respond to user issues within 1 week
- Review and merge PRs within 2 weeks
- Keep documentation current

**Quality metrics to track:**
- Skill load time
- Error rates
- User feedback
- GitHub stars/issues
- Download counts

## Security Considerations

### Sensitive Data

**Never include:**
- API keys or credentials
- Personal information
- Private repository URLs
- Internal company details
- Copyrighted content

**Use environment variables for:**
- API keys
- Database credentials
- Service endpoints
- User-specific paths

### Code Safety

**In scripts:**
- Validate all inputs
- Handle errors gracefully
- Avoid shell injection
- Sanitize file paths
- Check file permissions

**In documentation:**
- Warn about destructive operations
- Document prerequisites clearly
- Provide safe examples
- Explain security implications

## Distribution

### GitHub Repository

**Recommended structure:**
```
marketplace-repo/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── skill-1/
│   └── skill-2/
├── .gitignore
├── README.md
├── LICENSE
└── CHANGELOG.md
```

**.gitignore should exclude:**
```gitignore
# Environment files
.env
.env.local

# User-specific files
.DS_Store
*.log

# IDE files
.vscode/
.idea/

# Temporary files
*.tmp
*.swp
```

### Installation Instructions

**Provide clear steps:**
1. Prerequisites (Claude Code version, dependencies)
2. Clone or download instructions
3. Installation command
4. Verification steps
5. Troubleshooting common issues

**Example:**
```markdown
## Installation

1. Ensure Claude Code 1.0.0+ is installed
2. Clone this repository:
   ```bash
   git clone https://github.com/user/marketplace-name
   ```
3. Link the marketplace:
   ```bash
   claude-code marketplace add ./marketplace-name
   ```
4. Verify installation:
   ```bash
   claude-code marketplace list
   ```
```

## Common Pitfalls

### To Avoid

**❌ Too many tiny skills**
- Problem: Each skill has overhead; 20 one-function skills bloats the system
- Solution: Combine related functionality into cohesive skills

**❌ Unclear skill boundaries**
- Problem: Skills overlap, users don't know which to invoke
- Solution: Make each skill's purpose distinct and well-documented

**❌ Missing error handling**
- Problem: Scripts fail silently or with cryptic errors
- Solution: Add try-catch, provide helpful error messages

**❌ Hardcoded paths**
- Problem: Skills break on different systems
- Solution: Use relative paths, environment variables, or ask user for paths

**❌ Incomplete documentation**
- Problem: Users can't use skills effectively
- Solution: Include clear instructions, examples, and troubleshooting

**❌ No version updates**
- Problem: Users don't know what changed
- Solution: Update version and maintain CHANGELOG.md

**❌ Untested skills**
- Problem: Skills fail when users try them
- Solution: Test each skill thoroughly before publishing

## Examples to Study

### Anthropic Agent Skills

Study the official [anthropic-agent-skills](https://github.com/anthropics/anthropic-agent-skills) marketplace:

**What to learn:**
- Plugin organization patterns
- Skill description quality
- Documentation structure
- Validation approaches
- Asset organization

**Notable patterns:**
- `document-skills`: Multi-format document processing grouped logically
- `example-skills`: Wide variety of capabilities in one plugin
- Clear, action-oriented naming throughout

### Your Own Marketplace

After publishing, reflect:
- Which skills get used most?
- Where do users get confused?
- What documentation is missing?
- How can organization improve?
- What features are requested?

Iterate based on real usage and feedback.
