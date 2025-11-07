---
name: daily-tech-news-search
description: Automated daily tech news search using deep research capabilities. Searches for approximately 50 news items about major AI and tech companies, validates through 5 verification rounds, and outputs structured results. Use when you need comprehensive daily tech news collection for Chinese timezone dates.
---

# Daily Tech News Search

## Overview

Automates comprehensive daily tech news collection focusing on major AI companies (OpenAI, Anthropic, Google, Microsoft, etc.) and tech giants. Uses deep research methodology with 5-round verification to ensure quality and accuracy.

## When to Use This Skill

Invoke this skill when:
- Collecting daily tech news for publication or analysis
- Need comprehensive coverage of AI and tech company developments
- Require structured, verified news collection (not just raw search)
- Working with Chinese timezone dates for news freshness
- Need approximately 50 high-quality news items

## Core Capabilities

### 1. Deep Research Execution

**Research Strategy**: Unified planning with exhaustive depth

Uses the `/sc:research` command with optimized parameters:
```bash
/sc:research --depth exhaustive --strategy unified "[search query]"
```

**Key Parameters**:
- `--depth exhaustive`: Comprehensive multi-source search
- `--strategy unified`: Present research plan for approval before execution
- Targets: ~50 news items across all major tech companies

### 2. Search Scope

#### Primary Focus: AI Companies
- OpenAI (ChatGPT, GPT models, partnerships)
- Anthropic (Claude, safety research, funding)
- Google/DeepMind (Gemini, AI infrastructure, products)
- Microsoft (Azure AI, Copilot, investments)
- Meta (LLaMA, AI research, products)
- Amazon (AWS AI services, Alexa, Q)
- xAI (Grok, infrastructure)
- Mistral AI (open models, European AI)

#### Secondary Focus: Tech Giants
- NVIDIA (AI chips, market performance)
- Apple (AI features, products, services)
- Tesla/SpaceX (autonomous driving, AI applications)
- TSMC (chip manufacturing, AI chip production)
- Intel/AMD (AI accelerators, competition)
- Chinese tech companies (Alibaba, Tencent, Baidu, ByteDance, Huawei)

#### Tertiary Focus: Emerging Topics
- Quantum computing commercialization
- Chip policy and regulations
- Major funding rounds (>$100M)
- Cybersecurity and AI safety
- Regulatory developments

### 3. Date Handling

**Chinese Timezone (UTC+8) Date Logic**:

```
Current date calculation:
- If system time < 16:00 UTC: Use today's date (already tomorrow in China)
- If system time >= 16:00 UTC: Use tomorrow's date (next day in China)

Search queries include:
- "today" (implicit in search)
- "November 7, 2025" (explicit date)
- "2025-11-07" (ISO format)
- "last 24 hours" (time-based)
```

**Date Verification**:
- All news items must include publication timestamp
- Filter out news older than 24 hours (China time)
- Prioritize breaking news and official announcements

### 4. Five-Round Verification

#### Round 1: Source Credibility Check
**Criteria**:
- Official company announcements (highest priority)
- Major tech media (TechCrunch, The Verge, Bloomberg, Reuters)
- Financial sources (Bloomberg, Financial Times, Wall Street Journal)
- Verified Twitter/X accounts
- Industry analysts

**Actions**:
- Score each source (1-10)
- Flag sources below 7 for review
- Cross-reference with official sources

#### Round 2: Date and Freshness Validation
**Criteria**:
- Publication timestamp within last 24 hours (China time)
- Breaking news vs. scheduled announcements
- Time-sensitive information accuracy

**Actions**:
- Extract and normalize all timestamps
- Filter out outdated news
- Flag conflicting dates

#### Round 3: Content Deduplication
**Criteria**:
- Identify duplicate stories from different sources
- Merge related news items
- Keep highest-quality version

**Actions**:
- Compare headlines for similarity (>80% match)
- Compare core facts (company, amount, product, etc.)
- Consolidate duplicate entries

#### Round 4: Completeness and Detail Check
**Criteria**:
- Essential facts present (who, what, when, where, why)
- Quantitative data (funding amounts, user numbers, percentages)
- Official quotes or statements
- Context and background

**Actions**:
- Score each item for completeness (1-10)
- Flag items below 7 for enhancement
- Add missing context from additional sources

#### Round 5: Final Quality Gate
**Criteria**:
- Target count achieved (~50 items)
- Geographic balance (US/China/Europe/Global)
- Topic diversity (products, funding, policy, research)
- Compliance readiness (see sensitive topics handling)

**Actions**:
- Rank all items by importance score
- Select top 50 (or adjust to meet target)
- Final compliance scan
- Generate structured output

### 5. Sensitive Topics Handling

**Pre-emptive Compliance Filtering**:

During research and verification, flag these topics:
- Military/defense contracts → Note for neutralization
- US-China trade restrictions → Frame as policy adjustments
- Company controversies involving minors → Focus on solutions
- Unverified financial speculation → Add disclaimers
- Political statements → Maintain neutrality

**Output Annotations**:
Each flagged item includes compliance notes for downstream processing.

### 6. Structured Output Format

**Standard Output Structure**:

```markdown
# [Date] Tech News Research Results

> **Search Date**: [China timezone date]
> **Total Items**: [count]
> **Verification Status**: 5/5 rounds completed
> **Quality Score**: [average score]/10

---

## 📊 Coverage Summary

- AI Companies: [count] items
- Tech Giants: [count] items
- Chips & Hardware: [count] items
- Funding & Investment: [count] items
- Policy & Regulation: [count] items
- Other: [count] items

---

## 🤖 AI Companies

### [Company Name]

**[News Item Number]. [Headline]**
- **Source**: [publication] | [credibility score]/10
- **Date**: [timestamp with timezone]
- **Summary**: [2-3 sentence summary]
- **Key Data**: [amounts, percentages, user numbers]
- **Compliance Notes**: [if any flags]

---

## 💼 Tech Giants

[Same structure]

---

## 💾 Chips & Semiconductors

[Same structure]

---

## 💰 Funding & Investment

[Same structure]

---

## ⚖️ Policy & Regulation

[Same structure]

---

## 📋 Verification Summary

### Round 1: Source Credibility
- Total sources reviewed: [count]
- Average credibility score: [score]/10
- Sources flagged: [count]

### Round 2: Date Validation
- Items within 24h: [count]
- Outdated items removed: [count]
- Timestamp conflicts resolved: [count]

### Round 3: Deduplication
- Duplicate clusters identified: [count]
- Items merged: [count]
- Final unique items: [count]

### Round 4: Completeness
- Average completeness score: [score]/10
- Items enhanced: [count]
- Missing data filled: [count]

### Round 5: Final Quality Gate
- Target achieved: [yes/no] ([actual count]/~50)
- Geographic balance: US [%] | China [%] | Europe [%] | Global [%]
- Topic diversity score: [score]/10
- Compliance flags: [count] items

---

## 🚩 Compliance Flags Summary

**High Priority** (require neutralization):
- Military/defense: [count] items
- Trade policy: [count] items
- Minor-related: [count] items

**Medium Priority** (add disclaimers):
- Financial speculation: [count] items
- Unverified claims: [count] items

---

## 📈 Quality Metrics

- Overall quality score: [score]/10
- Source credibility avg: [score]/10
- Content completeness avg: [score]/10
- Freshness score: [score]/10
- Diversity score: [score]/10

**Recommendation**: [Ready for publication / Needs review / Requires enhancement]

---

**Generated**: [timestamp]
**Timezone**: China Standard Time (UTC+8)
**Research Method**: Deep exhaustive search with unified planning
**Verification Rounds**: 5/5 completed
```

## Workflow

### Automated Execution Steps

1. **Initialize Search**
   ```
   - Determine China timezone current date
   - Build comprehensive search query
   - Invoke /sc:research with exhaustive depth
   ```

2. **Execute Deep Research**
   ```
   - Multi-source web search
   - Official announcements collection
   - Financial data aggregation
   - Social media monitoring
   - Industry analyst reports
   ```

3. **Round 1: Source Verification**
   ```
   - Score each source (1-10)
   - Flag low-credibility sources (<7)
   - Cross-reference with official sources
   ```

4. **Round 2: Date Validation**
   ```
   - Extract all timestamps
   - Filter by 24-hour window (China time)
   - Resolve timestamp conflicts
   ```

5. **Round 3: Deduplication**
   ```
   - Identify duplicate stories
   - Merge related items
   - Keep highest-quality versions
   ```

6. **Round 4: Enhancement**
   ```
   - Score completeness (1-10)
   - Fill missing data
   - Add context and background
   ```

7. **Round 5: Final Gate**
   ```
   - Achieve target count (~50)
   - Balance geography and topics
   - Compliance scan and flagging
   - Generate structured output
   ```

## Search Query Templates

### Primary Query (Comprehensive)
```
"AI news today [date]" OR "tech news today [date]"
OpenAI OR Anthropic OR Google OR Microsoft OR Meta OR Amazon OR NVIDIA
OR "artificial intelligence" OR "large language model" OR "AI chip"
OR "quantum computing" OR funding OR acquisition OR product launch
site:techcrunch.com OR site:theverge.com OR site:bloomberg.com OR site:reuters.com
```

### Company-Specific Queries
```
OpenAI news [date]
Anthropic Claude [date]
Google Gemini [date]
Microsoft AI [date]
NVIDIA AI chips [date]
Tesla autonomous [date]
[etc. for each major company]
```

### Topic-Specific Queries
```
"AI funding" [date]
"chip policy" [date]
"AI regulation" [date]
"quantum computing" [date]
```

## Integration Points

### Input
- **Date**: Auto-calculated China timezone current date
- **Optional**: User can override date or provide custom search scope

### Output
- **Format**: Structured markdown (ready for next skill)
- **Location**: `daily_news/docs/research/tech_news_[YYYYMMDD].md`
- **Metadata**: Verification summary and quality scores

### Handoff to Next Skill
Outputs structured research results that can be directly consumed by:
- `wechat-tech-news-writer` for WeChat optimization
- `tech-news-workflow` for automated pipeline
- Custom analysis tools

## Best Practices

### Do's ✅
- Always use exhaustive depth for comprehensive coverage
- Verify dates in China timezone (UTC+8)
- Complete all 5 verification rounds systematically
- Flag compliance issues early in the process
- Maintain source credibility standards
- Aim for 50±5 items (adjust for quality over quantity)

### Don'ts ❌
- Don't skip verification rounds to save time
- Don't include news older than 24 hours (China time)
- Don't accept low-credibility sources (<7/10)
- Don't ignore compliance flags
- Don't sacrifice quality for quantity
- Don't forget to timestamp outputs

## Quality Standards

**Minimum Requirements**:
- Source credibility: ≥7/10 average
- Content completeness: ≥7/10 average
- Date accuracy: 100% within 24h window
- Deduplication: <5% duplicate rate
- Target count: 45-55 items

**Excellence Targets**:
- Source credibility: ≥8.5/10
- Content completeness: ≥8.5/10
- Geographic balance: No single region >60%
- Topic diversity: ≥6 major categories
- Compliance readiness: All flags documented

## Error Handling

### Insufficient Results (<40 items)
1. Expand search scope to emerging companies
2. Include secondary tech topics
3. Extend time window to 36 hours
4. Lower source credibility threshold to 6/10

### Excessive Results (>60 items)
1. Raise source credibility threshold to 8/10
2. Prioritize major companies only
3. Focus on breaking news and major announcements
4. Increase importance scoring threshold

### Date Ambiguity
1. Default to China Standard Time (UTC+8)
2. Convert all timestamps to CST
3. Flag items with missing timestamps
4. Use publication time, not update time

## Examples

### Example Search Execution

**Command**:
```
使用 daily-tech-news-search skill 搜索今日科技新闻
```

**Process**:
1. Calculate date: 2025-11-07 (China time)
2. Execute: `/sc:research --depth exhaustive --strategy unified "AI and tech news November 7 2025"`
3. Collect: ~80 raw items from multiple sources
4. Verify Round 1: Filter to ~65 high-credibility items
5. Verify Round 2: Confirm ~60 within 24h window
6. Verify Round 3: Deduplicate to ~52 unique items
7. Verify Round 4: Enhance all to ≥7/10 completeness
8. Verify Round 5: Final selection of top 50 items
9. Output: Structured markdown with full verification summary

**Output Location**:
`daily_news/docs/research/tech_news_20251107.md`

## Technical Notes

### Dependencies
- Requires `/sc:research` command availability
- Needs web search access (Tavily MCP or similar)
- Requires date/time calculation capabilities
- Needs markdown output formatting

### Performance
- Average execution time: 15-25 minutes
- Search queries: 20-30 individual searches
- Sources consulted: 50-100 URLs
- Verification processing: 5-10 minutes
- Total items reviewed: 80-120 raw items
- Final output: ~50 verified items

### Limitations
- Depends on search API availability and quality
- May miss news behind paywalls
- Chinese-language sources require translation
- Real-time breaking news may be delayed
- Source credibility is subjective scoring

---

**Version**: 1.0
**Last Updated**: 2025-01-07
**Skill Type**: Research automation with verification pipeline
**Target Output**: ~50 verified daily tech news items
