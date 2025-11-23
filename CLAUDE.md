# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code Plugin Marketplace** providing an automated 5-phase workflow for daily AI/tech news collection and WeChat Official Account publication. Version 4.0 implements Single Responsibility Principle with dedicated skills for collection, validation, writing, formatting, and export.

## Architecture (v4.0)

### Five-Phase Pipeline with Quality Gates

```
Phase 1       Phase 2        Phase 3       Phase 4         Phase 5
Collection  → Validation   → Writing    → Formatting   → Export
15-20 min     3-5 min        5-8 min      4-6 min        1-2 min
   ↓             ↓              ↓            ↓              ↓
raw.md → validation_report → draft.md → format_report → final.md + .docx
         (40-45 items)                                  (publication-ready)

Quality Gates: ✓ After EVERY phase (mandatory)
```

**Skill 1: daily-tech-news-search** (Pure Collection)
- Executes AI-focused web searches via `/sc:research --depth exhaustive`
- Collects 45-55 raw items (24h priority, 48h supplement)
- Basic AI keyword filtering only
- Output: `tech_news_[DATE]_raw.md`

**Skill 2: daily-tech-news-validator** (Hardcoded Validation)
- 5 mandatory rounds with rule-based checks:
  1. Source credibility (domain whitelist/blacklist)
  2. Time accuracy (strict 48h, double-verification)
  3. AI relevance (keyword matching + exclusion patterns)
  4. Deduplication (similarity detection)
  5. Quality assurance (completeness, geographic balance)
- Generates `validation_report_[DATE].md` (workflow checks for this file)
- Output: `tech_news_[DATE]_validated.json` (40-45 items)

**Skill 3: wechat-tech-news-writer** (Pure Content Writing)
- Transforms validated data into WeChat article structure
- Creates "48小时焦点" (focus highlights) section
- Geographic categorization (国内/国外) or theme-based structure
- Adds engagement elements (引导语, 互动引导, 相关阅读)
- NO formatting or compliance optimization (delegated to Phase 4)
- Output: `tech_news_[DATE]_wechat_draft.md`

**Skill 4: daily-tech-news-formatter** (Multi-Round Optimization)
- 5 optimization rounds:
  1. WeChat compliance (100+ sensitive keyword substitutions)
  2. Grammar refinement (readability, flow, transitions)
  3. Punctuation normalization (Chinese standards)
  4. Title enhancement (clickability, SEO)
  5. Final polish (consistency, formatting)
- Generates `format_report_[DATE].md` (before/after comparisons)
- Output: `tech_news_[DATE]_wechat_final.md` (publication-ready)

**Skill 5: wechat-tech-news** (Orchestration)
- Coordinates all 5 phases with quality gates between each
- Tracks execution in `workflow_[DATE].json`
- Phase-specific retry strategies
- Optional Word document export
- One-command automation: `使用 wechat-tech-news skill`

### Directory Structure

```
.
├── .claude-plugin/
│   ├── marketplace.json         # Marketplace metadata (v4.0.0)
│   └── plugin.json              # Plugin definition (NO skills array - auto-discovered)
├── daily-tech-news-search/      # Phase 1: Collection
│   ├── SKILL.md
│   └── references/
│       ├── search_queries.md    # AI companies, tech giants, search patterns
│       └── verification_process.md
├── daily-tech-news-validator/   # Phase 2: Validation (NEW in v4)
│   ├── SKILL.md
│   └── references/
│       ├── validation_rules.md  # Hardcoded domain lists, thresholds
│       └── report_template.md
├── wechat-tech-news-writer/     # Phase 3: Writing
│   ├── SKILL.md
│   ├── references/
│   │   ├── compliance_guidelines.md
│   │   ├── sensitive_keywords.md  # 100+ keyword substitutions
│   │   └── engagement_tactics.md
│   └── assets/templates/
│       ├── domestic_international.md
│       ├── theme_based.md
│       └── focus_highlights.md
├── daily-tech-news-formatter/   # Phase 4: Formatting (NEW in v4)
│   ├── SKILL.md
│   └── references/
│       └── punctuation_guide.md
├── wechat-tech-news/            # Phase 5: Orchestration (Main entry point)
│   └── SKILL.md
├── skills/marketplace-creator/  # Bonus: Marketplace creation utility
│   ├── SKILL.md
│   └── references/marketplace_spec.md
└── README.md
```

## Key Architectural Principles (v4.0)

### Single Responsibility Principle

**Each skill has ONE job**:
- ❌ **Old v3**: Writer did content + compliance + formatting (bloated)
- ✅ **New v4**: Writer writes, Formatter formats (separation of concerns)

**Benefits**:
- Easier maintenance (modify formatting without touching content logic)
- Better testing (validate each phase independently)
- Clear error boundaries (know exactly which phase failed)

### Mandatory Quality Gates

**After EVERY phase, workflow checks**:
```yaml
Phase 1 → Gate 1:
  - Item count ≥45? YES → Phase 2 | NO → Retry with adjusted params

Phase 2 → Gate 2:
  - validation_report.md exists? YES → Check pass/fail gates
  - Average credibility ≥7.0? YES → Phase 3 | NO → Terminate

Phase 3 → Gate 3:
  - Draft structure valid? YES → Phase 4 | NO → Regenerate

Phase 4 → Gate 4:
  - format_report.md exists? YES → Check optimization rounds
  - All 5 rounds completed? YES → Phase 5 | NO → Continue formatting

Phase 5 → Gate 5:
  - Final file exists? YES → Success | NO → Retry export
```

### Hardcoded Validation Rules (v4 Innovation)

**No more subjective LLM scoring for critical checks**:

```yaml
# Phase 2 uses HARDCODED rules, not LLM judgment
Source_Credibility:
  Tier1_Domains: [techcrunch.com, bloomberg.com, reuters.com]  # 9-10/10
  Tier2_Domains: [wired.com, 36kr.com, tmtpost.com]           # 7-8/10
  Blacklist: [reddit.com, twitter.com, personal blogs]        # 0/10

Time_Validation:
  Strict_Window: 48 hours from calculated China date
  Double_Verification: Check both publish_date AND last_modified
  Timezone_Handling: All calculations in UTC+8 (China)

AI_Relevance:
  Required_Keywords: [AI, machine learning, LLM, neural network, ...]
  Exclusion_Patterns: [marketing, HR, general business, ...]
  Minimum_Score: 7/10 (keyword density + context)
```

## China Timezone Date Handling

All date calculations use **China Standard Time (UTC+8)**:

```python
# Current UTC time determines target China date
if UTC_time < 16:00:
    target_date = today        # Already next day in China
else:
    target_date = tomorrow     # Will be next day in China

# Validation window (Phase 2)
valid_window = [target_date - 48h, target_date]
```

**Critical**: News items must fall within 48-hour window (not 24h anymore in v4).

## Common Development Tasks

### Running Complete Workflow

```bash
# Basic usage (auto date, default settings)
使用 wechat-tech-news skill

# Custom date (use YYYYMMDD format)
使用 wechat-tech-news skill --date 20251122

# Adjust item count target
使用 wechat-tech-news skill --count 60

# Skip Phase 1 (use existing raw data)
使用 wechat-tech-news skill --skip-phase1

# Force specific structure
使用 wechat-tech-news skill --structure theme_based

# Strict compliance mode
使用 wechat-tech-news skill --compliance strict
```

### Testing Individual Phases

**Phase 1 only (Collection)**:
```bash
使用 daily-tech-news-search skill
```
- Time: 15-20 minutes
- Output: `tech_news_[DATE]_raw.md` (45-55 items)

**Phase 2 only (Validation)**:
```bash
使用 daily-tech-news-validator skill tech_news_20251122_raw.md
```
- Time: 3-5 minutes
- Output: `validation_report_[DATE].md` + `tech_news_[DATE]_validated.json`
- Check: Verify all 5 rounds completed and gates passed

**Phase 3 only (Writing)**:
```bash
使用 wechat-tech-news-writer skill tech_news_20251122_validated.json
```
- Time: 5-8 minutes
- Output: `tech_news_[DATE]_wechat_draft.md` (unoptimized)

**Phase 4 only (Formatting)**:
```bash
使用 daily-tech-news-formatter skill tech_news_20251122_wechat_draft.md
```
- Time: 4-6 minutes
- Output: `format_report_[DATE].md` + `tech_news_[DATE]_wechat_final.md`

### Modifying Behavior

**Add a new AI company to search**:
1. Edit `daily-tech-news-search/references/search_queries.md`
2. Add to appropriate category (AI Companies / Tech Giants / Emerging)
3. Restart workflow (Phase 1 will pick up new searches)

**Add a new credible source domain**:
1. Edit `daily-tech-news-validator/references/validation_rules.md`
2. Add domain to `Domain_Whitelist_Tier1` or `Tier2`
3. Next validation run will auto-score these domains high

**Add a new sensitive keyword**:
1. Edit `wechat-tech-news-writer/references/sensitive_keywords.md`
2. Format: `原词 | 替换词 | 风险等级 | 使用场景`
3. Formatter (Phase 4) will apply substitution automatically

**Customize article structure**:
1. Modify templates in `wechat-tech-news-writer/assets/templates/`
2. Test with `--structure` flag
3. Writer (Phase 3) will use new template

### File Output Locations

Default: `~/my-code/ResearchLab/daily_news/`

```
daily_news/
├── docs/research/
│   ├── tech_news_20251122_raw.md              # Phase 1
│   ├── validation_report_20251122.md          # Phase 2
│   ├── tech_news_20251122_validated.json      # Phase 2
│   ├── tech_news_20251122_wechat_draft.md     # Phase 3
│   ├── format_report_20251122.md              # Phase 4
│   ├── tech_news_20251122_wechat_final.md     # Phase 4 (publication)
│   └── tech_news_20251122_wechat_final.docx   # Phase 5 (optional)
└── metadata/
    └── workflow_20251122.json                  # Execution tracking
```

**Change output directory**:
```bash
使用 wechat-tech-news skill --output-dir /path/to/custom/dir
```

## Quality Standards

### Minimum Requirements (Phase 2 Quality Gates)

Will **TERMINATE workflow** if:
- Source credibility average: <7.0/10 ❌
- Raw item count: <45 ❌
- Validated item count: <40 ❌
- Deduplication rate: <95% ❌
- Items from blacklisted sources: >5% ❌
- Time validation failures: >10% ❌

### Excellence Targets

- Source credibility average: ≥8.5/10 ✅
- Validated item count: 40-45 ✅
- Deduplication rate: ≥98% ✅
- AI relevance score: ≥8.0/10 ✅
- Geographic balance: No single region >50% ✅
- Compliance optimization: All high-risk keywords addressed ✅

## Error Handling by Phase

### Phase 1: Collection Failures

**Symptom**: <45 items collected

**Auto-recovery**:
1. Extend search to tier-2 companies
2. Include smaller funding rounds (>$50M)
3. Search additional Chinese sources
4. Max retries: 2

**If still fails**: Manual intervention required, adjust search queries

### Phase 2: Validation Failures

**Symptom**: validation_report.md shows gate failures

**Actions**:
- **Low credibility**: Review source domains, expand whitelist if legitimate
- **Time violations**: Check timezone logic, verify news item timestamps
- **AI irrelevance**: Review exclusion patterns, adjust keyword lists
- **High duplicates**: Improve deduplication threshold

**Critical**: Phase 2 failures terminate workflow (by design)

### Phase 3: Writing Failures

**Symptom**: Draft structure invalid

**Auto-recovery**:
- Regenerate with alternative structure template
- If domestic/international fails → try theme_based
- Max retries: 1

### Phase 4: Formatting Failures

**Symptom**: format_report.md shows incomplete rounds

**Auto-recovery**:
- Continue from last completed round
- Each round is idempotent (can re-run safely)
- Max retries per round: 2

### Phase 5: Export Failures

**Symptom**: Word document generation fails

**Fallback**: Markdown file is already publication-ready, Word is optional

## Compliance Best Practices

### Three-Tier Risk Classification

**🔴 High Risk** (MUST neutralize):
- Military/defense: 军事合同 → 政府研发合作
- US-China confrontation: 中美对抗 → 国际格局调整
- Trade restrictions: 制裁/禁令 → 政策调整
- Sensitive entities: 五角大楼 → 美国政府

**🟡 Medium Risk** (Add disclaimers):
- Financial data: Add "仅供参考,不构成投资建议"
- Policy changes: Cite official sources
- Market predictions: Maintain objectivity

**🟢 Low Risk** (Normal reporting):
- Product launches
- Funding announcements
- Technical progress

### Compliance Happens in Phase 4

**Important**: Phase 3 (Writer) does NOT handle compliance. It creates engaging content structure.

**Phase 4 (Formatter)** applies all compliance optimizations:
- Round 1: Sensitive keyword substitutions
- Round 4: Title enhancement (avoid clickbait violations)
- Round 5: Final compliance check

## Performance Expectations

### Typical Execution (v4.0)

```
Component              Time        Output Size      Items
─────────────────────────────────────────────────────────
Phase 1: Collection    15-20 min   150-250 KB       45-55
Phase 2: Validation    3-5 min     50-80 KB         40-45
Phase 3: Writing       5-8 min     180-250 KB       40-45
Phase 4: Formatting    4-6 min     200-300 KB       40-45
Phase 5: Export        1-2 min     200-400 KB       40-45
─────────────────────────────────────────────────────────
Total Workflow         30-45 min   ~800 KB          40-45

Network Usage:
- Search queries: ~25-30
- URLs fetched: ~80-100
- Data transferred: ~60-120 MB

Quality Metrics (after Phase 2):
- Validation pass rate: 85-95%
- Source credibility: 7.8-8.5/10
- AI relevance: 8.0-8.8/10
- Deduplication rate: 96-98%
- Publication readiness (after Phase 4): 90-95%
```

## Dependencies

### Required

- **Claude Code**: ≥1.0.0
- **MCP Server**: Tavily (or equivalent web search capability)
- **Command**: `/sc:research` must be available
- **File System**: Write access to output directory

### Optional

- **Serena MCP**: For project memory (recommended)
- **docx library**: For Phase 5 Word export (optional, Python `python-docx`)

## Important Notes for Claude Code

### When Working with This Plugin

1. **Respect Phase Boundaries**: Each phase has a specific job. Don't mix responsibilities.
2. **Check Quality Gates**: Workflow WILL terminate on gate failures. This is intentional.
3. **Preserve Hardcoded Rules**: Phase 2 validation rules are NOT suggestions. Don't override with LLM judgment.
4. **Maintain 48h Window**: v4 uses 48-hour window (more lenient than v3's 24h)
5. **Follow File Naming**: `tech_news_[YYYYMMDD]_[stage].md` format is critical for phase handoffs

### When Debugging Issues

1. **Check Metadata First**: `workflow_[DATE].json` shows which phase failed
2. **Read Validation Report**: `validation_report_[DATE].md` explains Phase 2 failures
3. **Read Format Report**: `format_report_[DATE].md` shows Phase 4 optimizations
4. **Compare Draft vs Final**: Phase 3 output vs Phase 4 output shows formatting impact
5. **Verify File Handoffs**: Each phase expects specific input file format

### When Extending Functionality

1. **Add New Phase**: Insert between existing phases, update workflow orchestration
2. **Modify Validation Rules**: Edit `validation_rules.md`, document rationale
3. **Add Template**: Place in `assets/templates/`, reference in Writer SKILL.md
4. **Update Quality Gates**: Coordinate with workflow skill, test thoroughly
5. **Version Bump**: Update both `marketplace.json` and `plugin.json`, document in `RELEASE_NOTES.md`

## Publishing Workflow

After successful workflow completion:

1. **Open final file**: `tech_news_[DATE]_wechat_final.md`
2. **Final review**:
   - Check `format_report_[DATE].md` for optimization summary
   - Verify all high-risk keywords addressed
   - Confirm 48小时焦点 section has 5 items
3. **Copy content**: Entire markdown ready for WeChat editor
4. **Paste into WeChat**: Official Account editor
5. **Add cover image**: Select relevant AI/tech visual
6. **Preview**: Check formatting, emoji display
7. **Publish**: Schedule or publish immediately

Expected final article:
- Word count: 6500-7500
- Sections: 15-20
- Focus highlights: 5 headline items
- Compliance: All flags addressed
- Readability: Optimized through 5 formatting rounds

## Version Management

Current version: **4.0.0** (Production Ready)

**Major Changes from v3 to v4**:
- 3-phase → 5-phase pipeline
- Added dedicated Validator skill (hardcoded rules)
- Added dedicated Formatter skill (multi-round optimization)
- Writer now focused solely on content structure
- 24h window → 48h window (more lenient)
- Mandatory quality gates after EVERY phase

When updating versions:
1. Update `marketplace.json` version field
2. Update `plugin.json` version field (if it exists - currently auto-discovered)
3. Document changes in `RELEASE_NOTES.md`
4. Follow semantic versioning:
   - Major (4.0.0): Architecture changes, breaking API
   - Minor (4.1.0): New features, backward compatible
   - Patch (4.0.1): Bug fixes, compliance updates

## Troubleshooting Common Issues

### "validation_report.md not found"

**Cause**: Phase 2 (Validator) did not complete successfully

**Solution**:
1. Check if `tech_news_[DATE]_raw.md` exists
2. Manually run: `使用 daily-tech-news-validator skill [raw-file]`
3. If still fails, check validator SKILL.md for dependencies

### "Insufficient validated items (<40)"

**Cause**: Phase 2 filtered out too many items

**Solution**:
1. Review `validation_report.md` → see which rounds rejected items
2. If credibility issues: Expand domain whitelist
3. If time issues: Check China timezone calculation
4. If AI relevance issues: Adjust keyword lists
5. Re-run Phase 1 with `--count 60` to collect more

### "Compliance flags >30%"

**Cause**: High-risk content detected in Phase 4

**Solution**:
1. Review `format_report.md` → Round 1 details
2. Verify `sensitive_keywords.md` is up to date
3. Manually review flagged items
4. Consider splitting content to separate sections
5. If acceptable, proceed (formatter already neutralized)

### Skills not loading

**Cause**: Auto-discovery failed or SKILL.md missing

**Solution**:
1. Verify each skill directory has `SKILL.md` with YAML frontmatter
2. Check marketplace.json lists skills correctly
3. Restart Claude Code
4. Run `/help` to verify skills appear

## Marketplace Creation (Bonus Skill)

This plugin includes `marketplace-creator` skill for building new marketplaces:

```bash
使用 marketplace-creator skill
```

Generates:
- `.claude-plugin/marketplace.json`
- `README.md` template
- Skill directory structure
- Validation scripts

See `skills/marketplace-creator/SKILL.md` for details.
