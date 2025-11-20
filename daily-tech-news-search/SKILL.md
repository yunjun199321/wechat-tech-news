---
name: daily-tech-news-search
description: Pure data collection engine for daily AI tech news. Searches 45-55 raw items from major AI companies using deep research with strict 48h time window. No validation - delegates to daily-tech-news-validator.
---

# Daily Tech News Search

> **🔍 Version 4.0**: Pure collection engine - validation delegated to dedicated validator skill

## When to Use This Skill

Use this skill when you need to:
- Collect raw tech news data from authoritative sources
- Search 45-55 news items about AI and tech companies
- Prioritize freshness with 48-hour time window (24h preferred)
- Work with Chinese timezone dates (UTC+8) for news accuracy
- **Focus on quantity and coverage** - quality assurance done by validator

## Quick Start

```bash
使用 daily-tech-news-search skill
```

**Execution Time**: 15-20 minutes
**Output**: `tech_news_[YYYYMMDD]_raw.md`
**Next Phase**: Pass to daily-tech-news-validator for quality assurance

## Core Workflow (v4.0 - Collection Only)

1. **Auto-Calculate Date** - Determines current date in China timezone (UTC+8)
2. **Time-Progressive Search** - Prioritizes freshness
   - **Priority 1**: Today's news (Layer 0, 0-24h) - Collect as many as possible
   - **Priority 2**: Yesterday if needed (Layer 1, 24-48h) - Supplement to reach 45-55 items
   - **Priority 3**: ❌ Auto-disabled (>48h rejected to maintain freshness)
3. **Deep Research** - Executes `/sc:research --depth exhaustive --strategy unified`
4. **AI-Focus Filtering** - Only collect AI-relevant news (basic keyword check)
5. **Structured Output** - Generates markdown with ~45-55 raw items + metadata

## Search Coverage (AI-Focused)

**Primary Focus**: OpenAI, Anthropic, Google AI, Microsoft AI, Meta AI, Amazon AI, xAI, Mistral AI
**Secondary Focus**: NVIDIA/AMD (AI chips only), Apple Intelligence, AI tools/products, Chinese AI companies
**Tertiary Focus**: Major AI funding (>$100M), breakthrough AI research, AI policy, AI security/safety

**Excluded**: General semiconductor manufacturing, non-AI hardware, traditional tech news, pure quantum computing

## Search Strategy

### Phase 1: Company-Specific Search

Execute targeted searches for each major AI company:

```yaml
OpenAI:
  - "OpenAI" AND ("AI" OR "GPT" OR "ChatGPT") AND (today OR "24 hours")
  - "Sam Altman" AND "OpenAI" AND news

Anthropic:
  - "Anthropic" AND ("Claude" OR "AI safety") AND recent
  - "Dario Amodei" AND news

Google_AI:
  - "Google" AND ("Gemini" OR "Bard" OR "DeepMind" OR "AI")
  - "Sundar Pichai" AND "AI" AND news

Microsoft_AI:
  - "Microsoft" AND ("Azure AI" OR "Copilot" OR "OpenAI partnership")
  - "Satya Nadella" AND "AI"

[... similar for Meta, Amazon, xAI, etc.]
```

### Phase 2: Topic-Specific Search

```yaml
AI_Models:
  - "large language model" OR "LLM" AND (launch OR release OR announce)
  - "generative AI" AND (breakthrough OR "state of the art")

AI_Funding:
  - "AI startup" AND (funding OR "Series A" OR "Series B") AND "$"
  - "artificial intelligence" AND investment AND "million" OR "billion"

AI_Policy:
  - "AI regulation" OR "AI governance" AND government
  - "AI safety" AND policy AND (US OR China OR EU)

AI_Products:
  - "AI tool" OR "AI product" AND launch
  - "AI feature" AND release
```

### Phase 3: Geographic Balance

Ensure representation from both international and domestic (China) sources:

```yaml
Chinese_AI:
  - "百度" AND "AI" OR "文心一言"
  - "阿里" AND "通义千问"
  - "字节跳动" AND "AI"
  - "商汤" AND "AI"
  - Search Chinese tech media: 36kr, tmtpost, etc.
```

## Basic AI Relevance Filtering

**During Search** (lightweight filtering to reduce noise):

```yaml
Include_if:
  - Title contains: AI, GPT, Claude, Gemini, LLM, machine learning, deep learning
  - OR: Company in primary/secondary focus list + article mentions AI
  - OR: Funding amount >$100M + AI keyword in description

Exclude_if:
  - Title contains: rare earth, lithography, 5G, blockchain (without AI context)
  - AND: No AI keywords in first 200 characters of content
```

**Note**: This is basic filtering only. Comprehensive validation done by validator skill.

## Output Format

```markdown
# [Date] Tech News Research Results (Raw Collection)

> **Collection Summary**
> - Total Items Collected: 52
> - Layer 0 (0-24h): 38 items (73%)
> - Layer 1 (24-48h): 14 items (27%)
> - Average Age: 16.5 hours
> - Next Step: Validation required (daily-tech-news-validator)

## Time Layer Breakdown

### 🟢 Layer 0 - Today (38 items, 73%)
Fresh news from past 24 hours

### 🟡 Layer 1 - Yesterday (14 items, 27%)
Supplemental items for coverage completeness

## Collection Statistics

- AI Companies: 20 items
- Tech Giants: 15 items  
- AI Chips: 8 items
- Funding: 6 items
- Policy: 3 items

## [Category]

### [Company Name]

**[#]. [Headline]**
- Source: [publication]
- URL: [link]
- Date: 2025-11-20 14:30 CST | Layer 0 (8h ago) 🟢
- Summary: [2-3 sentences as found in source]
- Key Data: [amounts, numbers, percentages if available]

**[#]. [Headline]**
- Source: [publication]
- URL: [link]
- Date: 2025-11-19 22:00 CST | Layer 1 (30h ago) 🟡
- Summary: [2-3 sentences]

[... 52 items total ...]

## Collection Notes

**Search Gaps Identified**:
- [Areas where search found limited results]

**High-Priority Items** (for validator):
- [Items that seem particularly important]

**Potential Duplicates** (for validator to merge):
- Items #5 and #12 may cover same OpenAI announcement
- Items #23 and #31 both about NVIDIA earnings

**Time Distribution**:
- Excellent freshness: 73% from today
- Minimal old content: 0% >48h

---

**Generated by**: daily-tech-news-search v4.0.0 (collection only)
**Execution Time**: 18 minutes 32 seconds
**Next Phase**: daily-tech-news-validator (mandatory)
**Workflow Status**: COLLECTION COMPLETE → VALIDATION PENDING
```

## Integration with v4.0 Workflow

### Responsibilities (v4.0)

**This Skill Does**:
- ✅ Execute comprehensive AI-focused web searches
- ✅ Collect 45-55 raw news items
- ✅ Prioritize fresh content (24h > 48h > reject)
- ✅ Basic AI relevance filtering (keyword-based)
- ✅ Structure data in standard markdown format
- ✅ Include all metadata (source, URL, timestamp, layer)

**This Skill Does NOT Do**:
- ❌ Source credibility scoring (→ validator)
- ❌ Deep time validation (→ validator)
- ❌ Deduplication (→ validator)
- ❌ Completeness checking (→ validator)
- ❌ Quality gates (→ validator)
- ❌ Content writing (→ writer)
- ❌ Compliance optimization (→ formatter)

### Workflow Handoff

```yaml
After_Collection:
  Output_File: tech_news_[DATE]_raw.md
  Expected_Count: 45-55 items
  Status: RAW - Unvalidated
  
  Next_Step:
    Skill: daily-tech-news-validator
    Input: tech_news_[DATE]_raw.md
    Expected: Validation may reject 10-20% of items
    Final: tech_news_[DATE]_validated.json (40-45 items)
```

## Reference Documentation

- **[search_queries.md](references/search_queries.md)** - Complete search query templates
- **[progressive_time_search_spec.md](references/progressive_time_search_spec.md)** - Time-layer search logic
- **[ai_focus_filters.md](references/ai_focus_filters.md)** - Basic AI relevance filters

## Performance Expectations

```
Component                    Time        Output
─────────────────────────────────────────────────
Date calculation             ~10s        China timezone date
Company-specific searches    8-12 min    ~35-40 items
Topic-specific searches      4-6 min     ~10-15 items
Geographic balance           2-3 min     ~5-10 items (Chinese sources)
Data structuring            ~2 min       Markdown formatting
─────────────────────────────────────────────────
Total                       15-20 min    45-55 raw items
```

---

**Version**: 4.0.0
**Role**: Pure collection engine
**Dependencies**: `/sc:research` command, Tavily MCP or equivalent
**Output**: Raw, unvalidated markdown (validation in next phase)
**Philosophy**: Quantity and coverage over quality - let validator handle quality assurance