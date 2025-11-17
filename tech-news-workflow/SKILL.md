---
name: tech-news-workflow
description: End-to-end automated workflow for daily tech news. Searches for ~50 items using daily-tech-news-search, then transforms them into WeChat-optimized articles using wechat-tech-news-writer. One-command solution from raw search to publication-ready content.
---

# Tech News Workflow

## When to Use This Skill

Use this skill when you need:
- Complete daily tech news workflow (search → format → publish)
- Publication-ready WeChat Official Account content
- Automated quality control and compliance checking
- Consistent daily tech news production
- Minimal manual intervention from search to final output

## Quick Start

```bash
使用 tech-news-workflow skill
```

**Execution Time**: 25-40 minutes (average: 30 min)
**Output Files**:
- `tech_news_[DATE]_raw.md` - Raw research (50 verified items)
- `tech_news_[DATE]_wechat.md` - WeChat-optimized (publication-ready)
- `workflow_[DATE].json` - Execution metadata

## Workflow Architecture

```
┌─────────────────────────────────────────────┐
│         tech-news-workflow                  │
│                                             │
│  Phase 1: Research   →   Phase 2: Optimize │
│  (15-25 min)             (5-8 min)          │
│                                             │
│  Skills Used:                               │
│  - daily-tech-news-search                   │
│  - wechat-tech-news-writer                  │
│                                             │
│  Quality Gates: ✓ Between phases           │
│  Error Recovery: ✓ Automatic retry         │
│  Metadata Tracking: ✓ workflow_[DATE].json │
└─────────────────────────────────────────────┘
```

## Two-Phase Pipeline

### Phase 1: Research (15-25 minutes)

**Automatically executes**:
1. Calculate China timezone date (UTC+8)
2. Run `/sc:research --depth exhaustive --strategy unified`
3. Execute 5-round verification pipeline
4. Save `tech_news_[DATE]_raw.md`

**Quality Gate** (between Phase 1 & 2):
- Item count: 45-55 ✓
- Average quality: ≥7.0/10 ✓
- Geographic balance: No region >60% ✓
- Topic diversity: ≥6 categories ✓
- All verification rounds complete ✓

**If any check fails** → Halt, report issue, request manual review

### Phase 2: Optimization (5-8 minutes)

**Automatically transforms**:
1. Load raw research output
2. Select optimal structure (domestic/international OR theme-based)
3. Create 本周焦点 (5 headline items)
4. Apply 100+ sensitive keyword substitutions
5. Add WeChat elements (引导语、目录、免责声明、互动引导)
6. Save `tech_news_[DATE]_wechat.md`

**Final Validation**:
- 本周焦点: 5 items present ✓
- Compliance: All flags addressed ✓
- Word count: 6000-8000 ✓
- WeChat elements: All required components ✓
- Format: Valid markdown ✓

**Recommendation**: Ready for publication / Needs review / Requires changes

## Customization Options

```bash
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

## Error Handling

### Automatic Recovery

| Scenario | Detection | Action |
|----------|-----------|--------|
| Insufficient items (<40) | Phase 1 | Extend scope, lower threshold, retry |
| Poor quality (<6.5) | Phase 1 | Enhance completeness, re-run Round 4-5 |
| Research timeout | Phase 1 | Save partial results, allow continuation |
| File conflict | Phase 2 | Backup existing, create timestamped filename |

### Manual Review Required

| Scenario | Detection | Action |
|----------|-----------|--------|
| Geographic imbalance | Quality Gate | Suggest adjustments, require confirmation |
| Compliance overload (>30%) | Phase 2 | Generate detailed report, halt for review |

## Output Files

### File 1: tech_news_[DATE]_raw.md

**Purpose**: Research results with full verification details
**Content**: 50 verified news items with source credibility, timestamps, compliance flags
**Size**: ~150-250 KB
**Use**: Archive, analysis, alternative formatting

### File 2: tech_news_[DATE]_wechat.md

**Purpose**: Publication-ready WeChat article
**Content**: 6000-8000 words with all WeChat elements and compliance optimizations
**Size**: ~180-300 KB
**Use**: Direct copy-paste to WeChat Official Account editor

### File 3: workflow_[DATE].json

**Purpose**: Execution metadata and quality metrics
**Content**:
```json
{
  "execution_date": "2025-11-07T15:30:00+08:00",
  "china_timezone_date": "2025-11-07",
  "phase1": {
    "status": "completed",
    "duration_minutes": 18,
    "items_found": 50,
    "quality_score": 8.2
  },
  "phase2": {
    "status": "completed",
    "duration_minutes": 5,
    "structure_selected": "domestic_international",
    "compliance_flags": 6,
    "word_count": 7245
  },
  "total_duration_minutes": 23,
  "recommendation": "Ready for publication"
}
```

## Performance Metrics

**Typical Execution**:
- Time: 25-40 minutes (average: 30 min)
- Items found: 45-55
- Quality score: 7.8-8.5/10
- Compliance flags: 10-15% (all addressed)
- Word count: 6500-7500
- Publication readiness: 85-90%

**Resource Usage**:
- Network: ~80-100 URLs fetched
- Storage: ~500 KB per day
- Memory: Peak ~300 MB

## Best Practices

✅ **Do**:
- Run daily at consistent time (e.g., 9 AM China time)
- Review quality gate failures before retrying
- Check compliance flags in Phase 2 output
- Archive both raw and optimized versions
- Track quality metrics over time

❌ **Don't**:
- Skip quality gates to save time
- Ignore compliance flags
- Delete raw results (needed for debugging)
- Run multiple times same date (causes file conflicts)
- Override existing files without backup

## Publishing Workflow

After workflow completion:

1. Open `tech_news_[DATE]_wechat.md`
2. Review compliance flags and verify substitutions
3. Copy entire content
4. Paste into WeChat Official Account editor
5. Add cover image and adjust formatting if needed
6. Preview and publish

**Expected**: Ready to publish with minimal manual editing

## Integration

**Dependencies**:
- `daily-tech-news-search` skill
- `wechat-tech-news-writer` skill
- `/sc:research` command
- Tavily MCP (or equivalent web search)

**Optional**: Serena MCP for project memory

---

**Version**: 1.0
**Performance**: 25-40 min end-to-end, 85-90% publication readiness
**Automation Level**: Fully automated with quality gates
