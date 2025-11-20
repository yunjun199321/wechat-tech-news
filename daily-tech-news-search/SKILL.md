---
name: daily-tech-news-search
description: Automated daily tech news search with 5-round verification and intelligent 7-day progressive backfill. Searches ~50 items about major AI and tech companies using deep research. Use when you need comprehensive daily tech news collection for Chinese timezone dates.
---

# Daily Tech News Search

> **🆕 Version 2.0**: Now with intelligent time-progressive search (up to 7 days backfill)

## When to Use This Skill

Use this skill when you need to:
- Collect comprehensive daily tech news for publication or analysis
- Search ~50 verified news items about AI and tech companies
- Prioritize today's news with intelligent backfill from previous days
- Work with Chinese timezone dates (UTC+8) for news freshness
- Execute systematic research with quality verification (not just raw search)

## Quick Start

```bash
使用 daily-tech-news-search skill
```

**Execution Time**: 15-25 minutes
**Output**: `daily_news/docs/research/tech_news_[YYYYMMDD]_raw.md`

## Core Workflow (v3.0 - Strict 48h Mode)

1. **Auto-Calculate Date** - Determines current date in China timezone (UTC+8)
2. **Strict Progressive Search** - Prioritizes freshness with 48-hour hard limit
   - **Phase 1**: Today's news (Layer 0, 0-24h) - Target: 40-50 items
   - **Phase 2**: Yesterday if needed (Layer 1, 24-48h) - Supplement to 40-45 items only
   - **Phase 3**: ❌ Auto-disabled (>48h rejected unless importance ≥9.5 + manual approval)
3. **Deep Research** - Executes `/sc:research --depth exhaustive --strategy unified`
4. **5-Round Verification** - Systematic quality assurance with enhanced time validation
5. **Intelligent Balancing** - Geographic/topic diversity with AI-focus filtering
6. **Structured Output** - Generates markdown with ~40-45 verified AI-focused items

## Verification Pipeline

| Round | Criteria | Threshold |
|-------|----------|-----------|
| 1. Source Credibility | Official sources, major tech media, verified accounts | ≥7/10 avg |
| 2. Time Validation (v3.0) | Strict 48h limit with double verification | 100% within 48h |
| 3. Deduplication | Merge duplicate stories, keep highest quality | <5% duplicates |
| 4. Completeness | Essential facts, data, quotes, context | ≥7/10 avg |
| 5. Quality Gate | AI-focus, time distribution, geo/topic balance | Pass all checks |

**Time Layers (v3.0 - Strict 48h)**:
- 🟢 Layer 0 (Today): 0-24h, Priority: Highest, Weight: 1.00, **Auto-include all**
- 🟡 Layer 1 (Yesterday): 24-48h, Priority: High, Weight: 0.90, **Supplement only**
- 🔴 Layer 2+ (>48h): **Auto-reject** unless importance ≥9.5/10 + manual approval

## Search Coverage (AI-Focused)

**Primary Focus**: OpenAI, Anthropic, Google AI, Microsoft AI, Meta AI, Amazon AI, xAI, Mistral AI
**Secondary Focus**: NVIDIA/AMD (AI chips only), Apple Intelligence, AI tools/products, Chinese AI companies
**Tertiary Focus**: Major AI funding (>$100M), breakthrough AI research, AI policy, AI security/safety

**Excluded**: General semiconductor manufacturing, non-AI hardware, traditional tech news, pure quantum computing

## Quality Standards

**Minimum** (Will Fail Quality Gate):
- Item count: 40-50 (reduced from 45-55 due to stricter time filter)
- Source credibility: ≥7.0/10 average
- Time compliance: 100% within 48h (strict)
- AI relevance: 95%+ AI-related content
- Geographic balance: No single region >60%

**Excellence** (Recommended):
- Quality score: ≥8.5/10
- Completeness: ≥8.5/10
- Time distribution: >80% from Layer 0 (today)
- AI focus: 100% AI-related
- All compliance flags documented

## Output Format

```markdown
# [Date] Tech News Research Results

> **Coverage Summary**
> - Total Items: 50
> - Time Distribution: Today 38 (76%) | Yesterday 10 (20%) | 2+ days 2 (4%)
> - Average Age: 14.2 hours
> - Quality Score: 8.2/10 | Verification: 5/5 completed

## Time Layer Breakdown

### 🟢 Layer 0 - Today (38 items, 76%)
High-priority fresh news with maximum relevance

### 🟡 Layer 1 - Yesterday (10 items, 20%)
Supplemental items for balance and completeness
- Reason: Geographic diversity (6), Topic gaps (4)

### 🟠 Layer 2-3 - Older (2 items, 4%)
High-impact items only (importance ≥9/10)
- Reason: Critical announcements

## Coverage Summary
- AI Companies: 18 items
- Tech Giants: 12 items
- Chips & Hardware: 8 items
- [Additional categories...]

## [Category]
### [Company Name]
**[#]. [Headline]**
- Source: [publication] | [credibility]/10
- Date: 2025-11-17 14:30 CST | Layer 0 (6h ago) 🟢
- Summary: [2-3 sentences]
- Key Data: [amounts, numbers, percentages]
- Compliance Notes: [flags if any]

**[#]. [Headline]**
- Source: [publication] | [credibility]/10
- Date: 2025-11-16 10:00 CST | Layer 1 (28h ago) 🟡
- Supplement Reason: High importance (8.5/10), fills topic gap
- Summary: [2-3 sentences]
- Key Data: [amounts, numbers, percentages]

## Verification Summary
[Detailed metrics for all 5 rounds including time layer distribution]

## Compliance Flags Summary
[High/medium priority flags with counts]
```

## Compliance Pre-Filtering

During research, automatically flags sensitive topics:
- 🔴 Military/defense contracts → Note for neutralization
- 🔴 US-China trade restrictions → Frame as policy adjustments
- 🟡 Financial speculation → Add disclaimers
- 🟡 Unverified claims → Mark for review

## Reference Documentation

- **[search_queries.md](references/search_queries.md)** - Customize search scope and company list
- **[verification_process.md](references/verification_process.md)** - Detailed verification logic and criteria (v2.0 with time layers)
- **[progressive_time_search_spec.md](references/progressive_time_search_spec.md)** - ⭐ Complete v2.0 technical specification

## Integration

**Input**: Auto-calculated China timezone date (or user-specified `--date` parameter)
**Output**: Structured markdown with time-layer metadata, ready for `wechat-tech-news-writer` skill
**Handoff**: Direct consumption by `tech-news-workflow` pipeline

---

**Version**: 3.0 (2025-01-20)
**Changes in v3.0**:
- ⚡ **Strict 48h mode**: Auto-reject >48h news (vs. 7-day backfill in v2.0)
- 🎯 **Pure AI focus**: Excludes general semiconductor, traditional tech (vs. mixed coverage in v2.0)
- ✅ Top AI chip companies only (NVIDIA/AMD AI-specific)
- ✅ Enhanced time validation with double-check mechanism
- ✅ Target count adjusted to 40-50 items (from 45-55)

**Dependencies**: `/sc:research` command, Tavily MCP (or equivalent web search)
**Performance**: ~40-45 items in 20-30 minutes (faster than v2.0 due to narrower scope), quality ≥7.5/10 typical
