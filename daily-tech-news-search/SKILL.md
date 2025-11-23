---
name: daily-tech-news-search
description: Pure data collection engine for daily AI tech news with product focus (60/30/10 ratio). Searches 45-55 raw items from major companies AND community platforms (Product Hunt, HN, GitHub). Strict 48h time window. No validation - delegates to daily-tech-news-validator.
---

# Daily Tech News Search

> **🔍 Version 4.1**: Product-focused collection engine with community discovery - validation delegated to dedicated validator skill

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

## Core Workflow (v4.1 - Product-Focused Collection)

1. **Auto-Calculate Date** - Determines current date in China timezone (UTC+8)
2. **Product-First Search Strategy** - NEW: Community platforms prioritized
   - **Phase 4 First**: Community discovery (Product Hunt, HN, GitHub) - 20-25 items (40%)
   - **Phase 1 Second**: Major companies (OpenAI, Google, etc.) - 15-20 items (30%)
   - **Phase 2/3 Last**: Topics and geographic balance - 10-15 items (30%)
3. **Time-Progressive Filtering** - Prioritizes freshness
   - **Priority 1**: Today's news (Layer 0, 0-24h) - Collect as many as possible
   - **Priority 2**: Yesterday if needed (Layer 1, 24-48h) - Supplement to reach 45-55 items
   - **Priority 3**: ❌ Auto-disabled (>48h rejected to maintain freshness)
4. **Deep Research** - Executes `/sc:research --depth exhaustive --strategy unified`
5. **Content Filtering** - Deprioritize financial news, prioritize product launches
6. **Structured Output** - Generates markdown with ~45-55 raw items targeting 60% products

## Search Coverage (AI-Focused with Product Priority)

**PRIMARY FOCUS** (60% target - Products & Tools):
- **Community Platforms**: Product Hunt, Hacker News, GitHub Trending, Reddit (r/artificial, r/MachineLearning)
- **Major Company Products**: OpenAI, Anthropic, Google AI, Microsoft AI, Meta AI, Amazon AI, xAI, Mistral AI
- **AI Tools & Apps**: Productivity tools, coding assistants, image/video generators, writing tools
- **Open Source**: GitHub trending repos, community-driven projects with working demos

**SECONDARY FOCUS** (30% target - Strategic Activities):
- **Infrastructure**: NVIDIA/AMD AI chips, data centers, compute platforms
- **Partnerships**: Product-focused integrations only (e.g., "Claude on Azure")
- **Research**: Major papers with code release, conference highlights
- **Policy**: Direct product impact (e.g., "EU AI Act affects chatbots")
- **Chinese AI**: Baidu, Alibaba, ByteDance, Tencent, SenseTime, DeepSeek

**TERTIARY FOCUS** (10% target - Investment & Business):
- **Major Funding**: ≥$100M rounds for AI companies with shipped products
- **Strategic Business**: M&A, IPOs, market-moving executive changes
- **Financial Results**: ONLY if >20% beat/miss + product announcements

**EXCLUDED** (Deprioritized or Removed):
- Stock price movements without product context
- Routine earnings reports
- Generic partnerships without product integration
- Executive changes below C-level
- General semiconductor manufacturing
- Non-AI hardware announcements
- Traditional tech news labeled as "AI"

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

### Phase 4: Community Product Discovery (HIGH PRIORITY - 40% target)

**🎯 Critical for 60/30/10 ratio**: This phase discovers trending AI products from community platforms that traditional media often misses.

Execute searches on community platforms for viral AI tools and indie products:

```yaml
Product_Hunt (Target: 8-10 items):
  Primary_Queries:
    - site:producthunt.com "AI" (sort by upvotes, today + yesterday)
    - site:producthunt.com "AI tool" "featured"
    - site:producthunt.com "machine learning" OR "LLM" OR "GPT"

  Filters:
    - >100 upvotes (indicates strong community interest)
    - Clear product description and working demo link
    - Published within 48 hours
    - Actual product (not just concepts or waitlists)

  Focus:
    - AI productivity tools, browser extensions, coding assistants
    - Image/video generation tools, writing assistants
    - Open-source AI projects with demos
    - AI automation and workflow tools

Hacker_News (Target: 5-7 items):
  Primary_Queries:
    - site:news.ycombinator.com "Show HN" "AI"
    - site:news.ycombinator.com "Show HN" "LLM" OR "GPT"
    - site:news.ycombinator.com/front (AI-related, >200 points)

  Filters:
    - "Show HN" posts: >50 points
    - Front page posts: >200 points
    - Active discussion (>30 comments indicates interest)
    - Working demo or open-source code available

  Focus:
    - Technical AI projects with code
    - Novel AI applications and experiments
    - AI research implementations
    - Developer tools and libraries

GitHub_Trending (Target: 4-6 items):
  Primary_Queries:
    - site:github.com/trending "AI" "machine learning"
    - site:github.com/trending "LLM" OR "language model"
    - site:github.com/trending python "AI agent"
    - site:github.com/trending typescript "AI"

  Filters:
    - >100 stars gained in past 48 hours
    - Clear README with demo/screenshots
    - Active development (recent commits)
    - Practical application (not just research papers)

  Focus:
    - AI frameworks and SDKs
    - LLM tooling and infrastructure
    - AI agents and automation
    - Model deployment tools

Reddit_AI_Communities (Target: 2-4 items):
  Primary_Queries:
    - site:reddit.com/r/artificial "new AI tool" OR "launched"
    - site:reddit.com/r/MachineLearning "project" OR "demo"
    - site:reddit.com/r/LocalLLaMA (practical AI applications)

  Filters:
    - >200 upvotes (quality threshold)
    - Verified working links
    - Positive community sentiment (check comments)
    - Only approved subreddits (r/artificial, r/MachineLearning, r/LocalLLaMA)

  Focus:
    - Community-vetted AI tools
    - Open-source projects getting traction
    - Practical AI applications
    - Local AI deployments and tools

⚠️ **Critical**: This phase should contribute 20-25 items (40% of 50 total) to achieve product-focused 60/30/10 ratio
```

**Why Community Sources Matter**:
- Traditional media focuses on big companies (Google, OpenAI, Microsoft)
- Community platforms surface innovative indie tools and startups
- Higher engagement = proven user interest and product-market fit
- These are the "有趣AI产品，讨论度高的AI产品" users want

**Search Execution Order**:
1. Phase 1: Major companies (15-20 items) - Baseline coverage
2. **Phase 4: Community discovery (20-25 items)** - EXECUTE BEFORE Phase 2 to prioritize products
3. Phase 2: Topics (5-10 items) - Fill gaps
4. Phase 3: Geographic (5-8 items) - Balance coverage

## Content Prioritization & Filtering (v4.1 - Product Focus)

**During Search** (lightweight filtering to achieve 60/30/10 ratio):

### HIGH PRIORITY (Collect More) - Products & Tools

```yaml
Strongly_Include:
  Product_Launches:
    - Keywords: "launch", "release", "unveil", "introduce", "announce" + product name
    - Examples: "launches AI tool", "releases new model", "unveils platform"
    - Weight: HIGHEST (target 60% of collection)

  Feature_Updates:
    - Keywords: "new feature", "update", "improvement", "beta", "available now"
    - Examples: "adds AI capability", "new API", "beta access"

  Community_Products:
    - From: Product Hunt, Hacker News, GitHub Trending, Reddit
    - ALL items from these sources get HIGH priority
    - Minimum engagement thresholds ensure quality

  Open_Source:
    - Keywords: "open source", "GitHub", "Apache", "MIT license"
    - Community-driven projects and tools
```

### MEDIUM PRIORITY (Selective Collection) - Strategic Activities

```yaml
Selectively_Include:
  Strategic_Partnerships:
    - ONLY if involves product integration or deployment
    - Example: "partnership to deploy AI on Azure" ✅
    - Example: "strategic alliance announced" ❌ (too vague)

  Research_Breakthroughs:
    - Major papers from top labs (DeepMind, OpenAI Research, Meta FAIR)
    - Conference papers (NeurIPS, ICML) with code release

  Policy_Changes:
    - Direct product impact only
    - Example: "EU AI Act affects chatbots" ✅
    - Example: "AI regulation discussion continues" ❌
```

### LOW PRIORITY (Minimize Collection) - Financial & Personnel

```yaml
Deprioritize:
  Financial_News:
    - Stock movements: Include ONLY if >5% single-day change + major product news
    - Earnings reports: Include ONLY if beats/misses by >20% + product announcements
    - Revenue projections: Include ONLY if tied to specific product line

  Executive_Changes:
    - Include ONLY C-level at major AI companies (OpenAI, Anthropic, Google AI)
    - Skip: VP appointments, board changes, advisor announcements

  Generic_Partnerships:
    - Skip partnerships without clear product outcome
    - Skip "exploring collaboration" or "framework agreements" without specifics

Exclude_Completely:
  - Stock price movements without product context
  - Routine earnings beats/misses without surprises
  - Financial analyst upgrades/downgrades
  - Executive compensation details
  - Office openings/closings
  - Generic "AI is important" statements from executives
  - Conference attendance announcements
  - Hiring announcements
```

### AI Relevance Filtering

```yaml
Include_if:
  - Title contains: AI, GPT, Claude, Gemini, LLM, machine learning, deep learning, neural network
  - OR: Company in primary/secondary focus list + article mentions AI product
  - OR: Community source (Product Hunt, HN, GitHub) + AI keyword
  - OR: Funding amount >$100M + AI product mentioned

Exclude_if:
  - Title contains: rare earth, lithography, 5G, blockchain (without AI context)
  - AND: No AI keywords in first 200 characters of content
  - Pure hardware manufacturing without AI application
  - Traditional tech news repurposed as "AI news"
```

**Target Collection Distribution** (for ~50 items):
- 🚀 Products & Tools: 30 items (60%) - Product Hunt, HN, GitHub, major launches
- 🤝 Strategic Activities: 15 items (30%) - Partnerships, research, policy
- 💰 Investment & Business: 5 items (10%) - Major funding (≥$100M), significant business events

**Note**: This is initial filtering. Validator skill (Phase 2) enforces strict 60/30/10 ratio with weighted scoring.

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