---
name: daily-tech-news-search
description: Automated daily tech news search with 5-round verification. Searches ~50 items about major AI and tech companies using deep research. Use when you need comprehensive daily tech news collection for Chinese timezone dates.
---

# Daily Tech News Search

## When to Use This Skill

Use this skill when you need to:
- Collect comprehensive daily tech news for publication or analysis
- Search ~50 verified news items about AI and tech companies
- Work with Chinese timezone dates (UTC+8) for news freshness
- Execute systematic research with quality verification (not just raw search)

## Quick Start

```bash
使用 daily-tech-news-search skill
```

**Execution Time**: 15-25 minutes
**Output**: `daily_news/docs/research/tech_news_[YYYYMMDD]_raw.md`

## Core Workflow

1. **Auto-Calculate Date** - Determines current date in China timezone (UTC+8)
2. **Deep Research** - Executes `/sc:research --depth exhaustive --strategy unified`
3. **5-Round Verification** - Systematic quality assurance pipeline
4. **Structured Output** - Generates markdown with ~50 verified items and metadata

## Verification Pipeline

| Round | Criteria | Threshold |
|-------|----------|-----------|
| 1. Source Credibility | Official sources, major tech media, verified accounts | ≥7/10 avg |
| 2. Date Validation | Publication timestamp within 24h (China time) | 100% |
| 3. Deduplication | Merge duplicate stories, keep highest quality | <5% duplicates |
| 4. Completeness | Essential facts, data, quotes, context | ≥7/10 avg |
| 5. Quality Gate | Item count, geographic balance, topic diversity | Pass all checks |

## Search Coverage

**Primary Focus**: OpenAI, Anthropic, Google, Microsoft, Meta, Amazon, xAI, Mistral AI
**Secondary Focus**: NVIDIA, Apple, Tesla, TSMC, Intel, AMD, Chinese tech giants
**Tertiary Focus**: Quantum computing, chip policy, major funding (>$100M), cybersecurity

## Quality Standards

**Minimum** (Will Fail Quality Gate):
- Item count: 45-55
- Source credibility: ≥7.0/10 average
- Geographic balance: No single region >60%
- Topic diversity: ≥6 major categories

**Excellence** (Recommended):
- Quality score: ≥8.5/10
- Completeness: ≥8.5/10
- Balanced geography: No region >50%
- All compliance flags documented

## Output Format

```markdown
# [Date] Tech News Research Results

> Total Items: 50 | Quality Score: 8.2/10 | Verification: 5/5 completed

## Coverage Summary
- AI Companies: 18 items
- Tech Giants: 12 items
- Chips & Hardware: 8 items
- [Additional categories...]

## [Category]
### [Company Name]
**[#]. [Headline]**
- Source: [publication] | [credibility]/10
- Date: [timestamp with timezone]
- Summary: [2-3 sentences]
- Key Data: [amounts, numbers, percentages]
- Compliance Notes: [flags if any]

## Verification Summary
[Detailed metrics for all 5 rounds]

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
- **[verification_process.md](references/verification_process.md)** - Detailed verification logic and criteria

## Integration

**Input**: Auto-calculated China timezone date (or user-specified `--date` parameter)
**Output**: Structured markdown ready for `wechat-tech-news-writer` skill
**Handoff**: Direct consumption by `tech-news-workflow` pipeline

---

**Version**: 1.0
**Dependencies**: `/sc:research` command, Tavily MCP (or equivalent web search)
**Performance**: ~50 items in 15-25 minutes, quality ≥7.8/10 typical
