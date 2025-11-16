# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code Plugin** providing an automated workflow for daily tech news collection and WeChat Official Account publication. It consists of three interconnected skills that work together to transform raw research into publication-ready content optimized for Chinese social media platforms.

## Architecture

### Three-Skill Pipeline

```
daily-tech-news-search → wechat-tech-news-writer → tech-news-workflow
     (Research)              (Optimization)          (Orchestration)
```

**Skill 1: daily-tech-news-search**
- Deep research using `/sc:research --depth exhaustive --strategy unified`
- 5-round verification pipeline (source credibility → date validation → deduplication → completeness → final quality gate)
- Targets ~50 news items from major AI/tech companies
- China timezone date handling (UTC+8)
- Output: `tech_news_[DATE]_raw.md`

**Skill 2: wechat-tech-news-writer**
- Transforms raw research into WeChat-compliant articles
- Geographic categorization (国内/国外) or theme-based structure
- Compliance optimization using 100+ sensitive keyword substitutions
- Adds WeChat elements (引导语, 目录, 免责声明, 互动引导)
- Creates "本周焦点" (focus highlights) section with 5 headline items
- Output: `tech_news_[DATE]_wechat.md`

**Skill 3: tech-news-workflow**
- End-to-end orchestration of the complete pipeline
- Two-phase execution with quality gates between phases
- Error recovery and automatic retry logic
- Metadata tracking in `workflow_[DATE].json`
- One-command automation: `使用 tech-news-workflow skill`

### Directory Structure

```
.
├── .claude-plugin/              # Plugin manifests
│   ├── plugin.json              # Plugin definition (NO skills array)
│   └── marketplace.json         # Marketplace metadata
├── skills/                      # ✅ Skills auto-discovered from this directory
│   ├── daily-tech-news-search/  # Skill 1: Research
│   │   ├── SKILL.md            # Skill definition and instructions
│   │   ├── references/         # Search queries, verification process
│   │   └── assets/             # Templates and examples
│   ├── wechat-tech-news-writer/ # Skill 2: Optimization
│   │   ├── SKILL.md            # Skill definition and instructions
│   │   ├── references/         # Compliance guidelines, sensitive keywords, engagement tactics
│   │   └── assets/             # Structure templates (domestic/international, theme-based, focus highlights)
│   └── tech-news-workflow/      # Skill 3: Orchestration
│       ├── SKILL.md            # Skill definition and instructions
│       └── references/         # Workflow patterns and error handling
├── README.md                   # User-facing documentation
└── CLAUDE.md                   # This file
```

## Key Concepts

### China Timezone Date Handling

All date calculations use China Standard Time (UTC+8):
- If current UTC time < 16:00 → use today's date (already tomorrow in China)
- If current UTC time >= 16:00 → use tomorrow's date (next day in China)
- All news items must be within 24-hour window from calculated China date

### Five-Round Verification

**Never skip verification rounds.** Each round serves a critical purpose:

1. **Source Credibility**: Score 1-10, minimum 7/10 average
2. **Date Validation**: 100% within 24h window (China time)
3. **Deduplication**: <5% duplicate rate after merging
4. **Completeness**: Score 1-10, minimum 7/10 average
5. **Final Quality Gate**: Geographic balance, topic diversity, compliance flags

### Compliance Optimization

Three risk tiers for sensitive content:

- **🔴 High Risk**: Military/defense, US-China confrontation, minor-related incidents
  - **Action**: Must neutralize (五角大楼 → 美国政府, 中美对抗 → 国际格局调整)

- **🟡 Medium Risk**: Financial data, policy changes, market predictions
  - **Action**: Add disclaimers, maintain objectivity, cite sources

- **🟢 Low Risk**: Product launches, funding news, technical progress
  - **Action**: Normal reporting

**Critical**: Reference `skills/wechat-tech-news-writer/references/sensitive_keywords.md` for 100+ keyword substitutions.

## Common Development Tasks

### Testing Individual Skills

**Test Skill 1 (Research)**:
```
使用 daily-tech-news-search skill
```
- Execution time: 15-25 minutes
- Output: `daily_news/docs/research/tech_news_[DATE]_raw.md`
- Expected: ~50 items, quality score ≥7.0/10

**Test Skill 2 (Optimization)**:
```
使用 wechat-tech-news-writer skill [input-file]
```
- Execution time: 5-8 minutes
- Output: `daily_news/docs/research/tech_news_[DATE]_wechat.md`
- Expected: 6000-8000 words, all compliance flags addressed

**Test Skill 3 (Full Workflow)**:
```
使用 tech-news-workflow skill
```
- Execution time: 25-40 minutes (average: 30 min)
- Output: Both raw and WeChat files + metadata JSON
- Expected: "Ready for publication" recommendation

### Modifying Skill Behavior

**To add a new company to search scope**:
1. Edit `skills/daily-tech-news-search/references/search_queries.md`
2. Add company name to appropriate category (AI Companies / Tech Giants / Emerging)
3. Update SKILL.md documentation if adding a new category

**To add a new sensitive keyword**:
1. Edit `skills/wechat-tech-news-writer/references/sensitive_keywords.md`
2. Add entry with: 原词 | 替换词 | 风险等级 | 使用场景
3. Test with existing content to verify substitution works

**To customize article structure**:
1. Copy and modify templates in `skills/wechat-tech-news-writer/assets/templates/`
2. Update `skills/wechat-tech-news-writer/SKILL.md` to document new structure
3. Test with `--structure` flag in workflow skill

### File Output Locations

Default output directory: `~/my-code/ResearchLab/daily_news/`

```
daily_news/
├── docs/
│   └── research/
│       ├── tech_news_20251107_raw.md      # Phase 1 output
│       └── tech_news_20251107_wechat.md   # Phase 2 output
└── metadata/
    └── workflow_20251107.json              # Execution tracking
```

**To change output directory**:
- Use `--output-dir PATH` flag in workflow skill
- Or update default in `.claude-plugin/plugin.json` configuration

## Quality Standards

### Minimum Requirements (Will Fail Quality Gate)

- Source credibility average: <7.0/10 ❌
- Item count: <45 or >55 ❌
- Deduplication rate: <95% ❌
- Geographic imbalance: >60% from single region ❌
- Topic diversity: <6 major categories ❌

### Excellence Targets

- Source credibility average: ≥8.5/10 ✅
- Content completeness: ≥8.5/10 ✅
- Geographic balance: No single region >50% ✅
- Topic diversity: ≥6 categories with even distribution ✅
- Compliance readiness: All high-risk flags addressed ✅

## Dependencies

### Required

- **Claude Code**: ≥1.0.0
- **MCP Server**: Tavily (web search) or equivalent
- **Command**: `/sc:research` must be available
- **File System**: Write access to output directory

### Optional

- **MCP Server**: Serena (for project memory and optimization)

## Workflow Customization Options

```bash
# Basic usage (auto date, default settings)
使用 tech-news-workflow skill

# Custom date
使用 tech-news-workflow skill --date 2025-11-08

# Custom item count
使用 tech-news-workflow skill --count 60

# Force specific structure
使用 tech-news-workflow skill --structure theme_based

# Skip Phase 1 (use existing research)
使用 tech-news-workflow skill --skip-phase1

# Strict compliance mode
使用 tech-news-workflow skill --compliance strict

# Combined options
使用 tech-news-workflow skill --date 2025-11-08 --count 45 --compliance strict
```

## Error Handling Patterns

### Insufficient Items (<40)
**Automatic**: Workflow retries with adjusted parameters
- Extend search scope to tier-2 companies
- Lower completeness threshold to 6.5/10
- Expand time window to 30h
- Include smaller funding rounds (>$50M)

### Quality Gate Failure
**Semi-automatic**: Workflow suggests fixes, requires confirmation
- Review Round 5 selection criteria
- Manually adjust item selection
- Re-run specific verification round
- Document adjustment in metadata

### Compliance Flag Overload (>30%)
**Manual**: Requires editorial review
- Generate detailed compliance report
- Review each flagged item individually
- Consider splitting to separate sections
- Halt workflow for human review

### File Conflicts
**Automatic**: Workflow resolves with timestamp
- Backup existing file
- Generate new filename: `tech_news_[DATE]_wechat_[TIME].md`
- Continue processing
- Log conflict in metadata

## Compliance Best Practices

### Content That Requires Neutralization

1. **Military/Defense**: Always use "政府研发合作" instead of "军事合同"
2. **US-China Relations**: Frame as "国际格局调整" not "中美对抗"
3. **Trade Restrictions**: Use "政策调整" instead of "制裁" or "禁令"
4. **Minor-Related Incidents**: Focus on solutions, not negative cases
5. **Financial Speculation**: Add disclaimer: "仅供参考,不构成投资建议"

### Required Disclaimers

**For financial data** (funding, market cap, stock prices):
```markdown
**免责声明**

*本报告基于[DATE]的公开信息整理,数据来源包括官方公告、主流媒体报道和行业分析。
所有投资相关信息仅供参考,不构成投资建议。*
```

**For policy/regulatory content**:
```markdown
*以上政策信息均来自公开渠道,仅供了解行业动态参考,具体政策以官方公告为准。*
```

## Performance Expectations

### Typical Execution Metrics

```
Component                Time        Output Size
──────────────────────────────────────────────────
Phase 1: Research        15-25 min   150-250 KB
Phase 2: Optimization    5-8 min     180-300 KB
Total Workflow          25-40 min   ~500 KB
Average                 30 min

Network Usage:
- Search queries: ~30
- URLs fetched: ~80-100
- Data transferred: ~50-100 MB

Quality Metrics:
- Items found: 45-55
- Quality score: 7.8-8.5/10
- Compliance flags: 10-15% (all addressed)
- Publication readiness: 85-90%
```

## Plugin Development

### Adding a New Skill

1. Create new directory: `[skill-name]/`
2. Create `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Brief description
   ---
   ```
3. Add documentation sections:
   - Overview
   - When to Use This Skill
   - Core Capabilities
   - Workflow
   - Best Practices
4. Update `.claude-plugin/plugin.json` skills array
5. Update main `README.md`
6. Test skill loading: `/help` should show new skill

### Modifying Existing Skills

1. Edit `[skill-name]/SKILL.md` for behavior changes
2. Update `references/` for supporting documentation
3. Update `assets/templates/` for structural changes
4. Test thoroughly with all workflow phases
5. Update version in `.claude-plugin/marketplace.json`
6. Document in `RELEASE_NOTES.md`

## Important Notes for Claude Code

### When Working with this Plugin

1. **Respect Verification Rounds**: Never skip or shortcut the 5-round verification process in daily-tech-news-search
2. **Preserve China Timezone Logic**: All date calculations must account for UTC+8 offset
3. **Maintain Compliance Standards**: Always apply sensitive keyword substitutions from reference tables
4. **Track Quality Metrics**: Preserve metadata in workflow_[DATE].json for continuous improvement
5. **Follow File Naming**: Use consistent `tech_news_[YYYYMMDD]_[type].md` format

### When Debugging Issues

1. **Check Metadata First**: `workflow_[DATE].json` contains execution details and error context
2. **Verify Quality Gates**: Each phase has specific thresholds that must be met
3. **Review Compliance Flags**: High flag count (>30%) indicates need for manual review
4. **Examine Raw vs. Optimized**: Compare both outputs to understand transformation
5. **Reference Documentation**: Each skill's SKILL.md contains detailed troubleshooting sections

### When Extending Functionality

1. **Maintain Pipeline Integrity**: Skills are designed to work in sequence (search → optimize → orchestrate)
2. **Preserve Output Formats**: Downstream skills depend on specific markdown structures
3. **Document Template Changes**: Update both SKILL.md and reference docs when modifying templates
4. **Test End-to-End**: Always test with complete workflow, not just individual skills
5. **Update Quality Standards**: If adding new verification steps, update quality gate thresholds

## Publishing Workflow

After workflow completion, the typical publishing process:

1. Open `tech_news_[DATE]_wechat.md`
2. Review compliance flags and verify all substitutions applied
3. Copy entire content
4. Paste into WeChat Official Account editor
5. Add cover image and adjust formatting if needed
6. Preview and publish

Expected performance:
- 6000-8000 words
- ~15-20 sections
- 5 focus highlights
- All compliance requirements met
- Ready to publish with minimal manual editing

## Version Management

Current version: **1.0.0** (Production Ready)

When updating versions:
1. Update `.claude-plugin/marketplace.json` version field
2. Update `.claude-plugin/plugin.json` version field
3. Document changes in `RELEASE_NOTES.md`
4. Follow semantic versioning:
   - Major (1.0.0): Breaking changes to skill interfaces
   - Minor (0.1.0): New features, backward compatible
   - Patch (0.0.1): Bug fixes, compliance updates
