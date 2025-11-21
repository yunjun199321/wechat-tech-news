# Search Query Reference

## Overview

This document provides optimized search queries for the daily-tech-news-search skill. Queries are organized by company, topic, and search strategy.

**v4.1 Update**: Enhanced product focus with 60/30/10 content ratio (products/business/investment)

---

## Company-Specific Queries

### AI Companies

#### OpenAI
```
Primary: "OpenAI" AND (launch OR release OR "new feature" OR "new model") AND "today"
Secondary: "ChatGPT" OR "GPT-4" OR "GPT-5" OR "DALL-E" OR "Sora"
Focus: **product launches, model updates, new features** (HIGH priority)
Secondary: partnerships, research papers (MEDIUM priority)
Low Priority: funding announcements (include only if >$500M)
```

#### Anthropic
```
Primary: "Anthropic" AND (launch OR release OR "Claude update") AND "today"
Secondary: "Claude" OR "Claude 4" OR "constitutional AI" OR "API"
Focus: **Claude model updates, API features, safety research** (HIGH priority)
Low Priority: funding rounds (include only if strategic)
```

#### Google/DeepMind
```
Primary: ("Google AI" OR "DeepMind" OR "Gemini") AND (launch OR release OR research) AND "today"
Secondary: "Bard" OR "Gemini Pro" OR "AI Studio" OR "PaLM"
Focus: **Gemini updates, DeepMind research papers, new AI products** (HIGH priority)
```

#### Microsoft
```
Primary: ("Microsoft AI" OR "Azure AI" OR "Copilot") AND news AND "today"
Secondary: "Satya Nadella" OR "OpenAI partnership"
Focus: Azure AI services, Copilot features, OpenAI integration
```

#### Meta
```
Primary: ("Meta AI" OR "LLaMA") AND news AND "today"
Secondary: "Mark Zuckerberg" OR "AI research"
Focus: LLaMA models, AI products, research publications
```

#### Amazon
```
Primary: ("Amazon AI" OR "AWS AI" OR "Alexa") AND news AND "today"
Secondary: "Amazon Q" OR "Bedrock" OR "SageMaker"
Focus: AWS AI services, Alexa improvements, Q assistant
```

#### xAI
```
Primary: "xAI" AND (news OR announcement) AND "today"
Secondary: "Grok" OR "Elon Musk AI"
Focus: Grok updates, infrastructure, partnerships
```

### Tech Giants

#### NVIDIA (AI-Focused Only)
```
Primary: "NVIDIA" AND ("AI" OR "H100" OR "Blackwell" OR "data center AI") AND news AND "today"
Secondary: "Jensen Huang" AND "AI" OR "NVIDIA" AND ("training" OR "inference" OR "AI chip")
Focus: AI chips, AI data centers, AI partnerships, AI product launches
Exclude: Gaming GPUs, crypto mining, automotive (unless AI-specific like autonomous driving)
```

#### Apple
```
Primary: ("Apple AI" OR "Apple Intelligence") AND news AND "today"
Secondary: "Siri" OR "Tim Cook" OR "Apple Silicon"
Focus: AI features, product launches, chip development
```

#### Tesla/SpaceX
```
Primary: ("Tesla FSD" OR "SpaceX") AND news AND "today"
Secondary: "Elon Musk" OR "autonomous" OR "Starship"
Focus: FSD progress, SpaceX launches, Optimus robot
```

#### TSMC
```
Primary: "TSMC" AND (news OR earnings OR expansion) AND "today"
Secondary: "Taiwan Semiconductor" OR "chip manufacturing"
Focus: Manufacturing capacity, advanced nodes, customer orders
```

### Chinese Tech Companies

#### Alibaba
```
Primary: ("Alibaba AI" OR "阿里巴巴" OR "Qwen") AND news AND "today"
Secondary: "Alibaba Cloud" OR "Tongyi Qianwen"
Focus: AI investment, cloud services, model development
```

#### Tencent
```
Primary: ("Tencent AI" OR "腾讯") AND news AND "today"
Secondary: "WeChat AI" OR "Hunyuan"
Focus: AI features, investment, partnerships
```

#### Baidu
```
Primary: ("Baidu" OR "百度" OR "ERNIE") AND AI AND news AND "today"
Secondary: "Robin Li" OR "Apollo" OR "文心一言"
Focus: ERNIE models, Apollo autonomous driving, AI applications
```

#### ByteDance
```
Primary: ("ByteDance" OR "字节跳动" OR "TikTok AI") AND news AND "today"
Secondary: "Doubao" OR "豆包"
Focus: AI investment, algorithm development, products
```

#### Huawei
```
Primary: ("Huawei AI" OR "华为") AND news AND "today"
Secondary: "Ascend" OR "Pangu" OR "盘古"
Focus: AI chips, Pangu models, cloud services
```

---

## Topic-Based Queries

### 🚀 AI Product Launches (HIGH PRIORITY - 40%)

```
Primary: 
- "AI product launch" OR "AI tool release" OR "new AI app"
- "launches AI" OR "unveils AI" OR "announces AI product"
- "available now" OR "beta launch" OR "public release"

Secondary:
- "GPT-4" OR "Claude" OR "Gemini" OR "LLaMA" (new versions)
- "AI agent" OR "AI assistant" OR "AI copilot"
- "AI SDK" OR "AI API" OR "developer tools"

Focus: New AI models, tools, applications, SDKs, APIs
Time: Last 24-48 hours
Sources: Official blogs, TechCrunch, The Verge, Product Hunt

Filters:
- Must have clear product name and launch date
- Must be publicly available or in beta
- Exclude vaporware announcements
```

### 🎯 Trending AI Products (HIGH PRIORITY - 20%)

```
Sources:
- Product Hunt: site:producthunt.com "AI" (sort by upvotes)
- Hacker News: site:news.ycombinator.com "Show HN" "AI"
- Reddit: site:reddit.com/r/artificial "new AI tool"
- GitHub Trending: site:github.com/trending "AI" "machine learning"

Focus: Community-driven trending products, indie AI tools
Time: Last 48 hours
Validation: Must have >100 upvotes/stars or significant discussion

Example queries:
- site:producthunt.com "AI tool" "today" (sort by top)
- site:news.ycombinator.com "Show HN: AI" (last 48h)
- site:github.com/trending "AI agent" "LLM"
```

### 📊 AI Research & Papers (MEDIUM PRIORITY - 15%)

```
Primary:
- "AI research" OR "machine learning paper" OR "breakthrough"
- "arXiv" AND "AI" AND "today"
- Conference announcements: "NeurIPS" OR "ICML" OR "CVPR"

Secondary:
- "research paper" AND ("OpenAI" OR "DeepMind" OR "Meta AI")
- "AI breakthrough" OR "AI discovery"
- "open source" AND "research"

Focus: Major research publications, conference papers, breakthroughs
Sources: arXiv, official labs, academic conferences
Time: Last 48 hours
```

### 🤝 AI Activities & Events (MEDIUM PRIORITY - 10%)

```
Primary:
- "AI conference" OR "AI summit" OR "tech conference"
- "keynote" AND "AI" OR "demo day"
- "partnership" AND ("AI" OR "product launch")

Secondary:
- Company events: "OpenAI DevDay" OR "Google I/O" OR "Microsoft Build"
- "open source release" OR "GitHub" AND "AI"
- "collaboration" AND "AI" (product-focused only)

Focus: Conferences, keynotes, strategic product partnerships
Time: This week
Exclude: General business partnerships without product component
```

### 💼 Business & Strategy (MEDIUM PRIORITY - 15%)

```
Primary:
- "AI strategy" OR "AI adoption" OR "enterprise AI"
- "partnership" (if involves product integration)
- "expansion" AND "AI" (if involves new products/services)

Secondary:
- Leadership changes (C-level only)
- Market analysis (major shifts only)
- Policy impacts (direct product implications)

Focus: Strategic moves that affect products/services
Exclude: Generic business news, HR announcements
```

### 💰 Funding & Investment (LOW PRIORITY - 10%)

```
Primary: ("AI funding" OR "AI investment") AND "today"
Secondary: ("Series C" OR "Series D") AND "AI" (later-stage only)
Focus: **Major rounds only (≥$100M)**, unicorn valuations, IPOs

⚠️ Strict Filters:
- Amount ≥ $100 million (increased from $50M)
- AI/tech companies with **actual products** (not pure R&D)
- Strategic significance (not routine venture rounds)
- Announced within 48 hours

Deprioritize:
- Series A/B rounds (unless breakthrough technology)
- Generic venture capital news
- Acquisition rumors (confirmed only)

Weight: 0.3x (compared to 1.0x for product launches)
```

---

## Advanced Search Strategies

### Multi-Source Aggregation

**Strategy**: Search same topic across multiple authoritative sources

```
site:techcrunch.com "AI news" "November 7 2025"
OR site:theverge.com "AI news" "November 7 2025"
OR site:bloomberg.com "artificial intelligence" "November 7 2025"
OR site:reuters.com "AI" "November 7 2025"
OR site:wsj.com "AI" "November 7 2025"
```

### Time-Sensitive Breaking News

**Strategy**: Focus on real-time announcements

```
"breaking" OR "just announced" OR "launches" OR "unveils"
AND ("AI" OR "tech")
AND "2025-11-07"
```

### Financial Data Focus

**Strategy**: Target quantitative business news

```
("revenue" OR "earnings" OR "market cap" OR "stock price" OR "valuation")
AND ("AI company" OR "tech company")
AND "Q3 2025" OR "Q4 2025"
```

### Product Launch Detection

```
("launches" OR "unveils" OR "releases" OR "announces" OR "introduces")
AND ("AI" OR "product" OR "service")
AND "November 7 2025"
```

---

## Date Handling


### China Timezone (UTC+8) Logic

```python
import datetime

def get_china_date():
    """Calculate current date in China timezone"""
    utc_now = datetime.datetime.utcnow()
    china_offset = datetime.timedelta(hours=8)
    china_now = utc_now + china_offset

    # If UTC time is before 16:00, China is already tomorrow
    if utc_now.hour < 16:
        search_date = china_now.date()
    else:
        search_date = (china_now + datetime.timedelta(days=1)).date()

    return search_date

# Example outputs:
# UTC 10:00 Nov 7 → China Nov 7 (search "November 7 2025")
# UTC 18:00 Nov 7 → China Nov 8 (search "November 8 2025")
```


```python
def generate_layer_dates(base_date, max_layers=8):
    """
    Generate date search targets for progressive backfill

    Args:
        base_date: Current China date
        max_layers: 0-7 (today through 7 days ago)

    Returns:
        List of (layer, date) tuples
    """
    layers = []
    for layer in range(max_layers):
        target_date = base_date - datetime.timedelta(days=layer)
        layers.append((layer, target_date))

    return layers

# Example usage:
china_date = get_china_date()  # 2025-11-17
layers = generate_layer_dates(china_date)

# Output:
# [(0, 2025-11-17),  # Layer 0: Today
#  (1, 2025-11-16),  # Layer 1: Yesterday
```

### Date Query Generation

```python
def generate_date_query(target_date):
    """
    Generate multiple date format variations for robust search

    Args:
        target_date: datetime.date object

    Returns:
        List of date strings in various formats
    """
    formats = [
        target_date.strftime("%B %d, %Y"),     # November 17, 2025
        target_date.strftime("%b %d %Y"),      # Nov 17 2025
        target_date.strftime("%Y-%m-%d"),      # 2025-11-17
        target_date.strftime("%d %B %Y"),      # 17 November 2025
    ]

    # Add relative terms for Layer 0
    if is_today(target_date):
        formats.extend(["today", "今天"])

    return formats

def build_search_query(base_query, layer, target_date):
    """
    Build complete search query with date filters

    Args:
        base_query: Core search terms (e.g., "OpenAI news")
        layer: Time layer (0-7)
        target_date: Date to search for

    Returns:
        Complete search query string
    """
    date_formats = generate_date_query(target_date)

    # Create OR clause for date formats
    date_clause = " OR ".join([f'"{df}"' for df in date_formats])

    # Combine with base query
    query = f'{base_query} AND ({date_clause})'

    return query

# Example:
# Layer 0 (Today):
#   'OpenAI news AND ("November 17, 2025" OR "Nov 17 2025" OR "2025-11-17" OR "today" OR "今天")'
#
# Layer 1 (Yesterday):
#   'OpenAI news AND ("November 16, 2025" OR "Nov 16 2025" OR "2025-11-16")'
```

### Search Execution Strategy

```python
def progressive_search(target_count=50):
    """
    Execute progressive time-layered search

    Strategy:
    1. Start with Layer 0 (today)
    2. If count < 50, search Layer 1 (yesterday)
    3. Continue through Layers 2-7 until target reached
    """
    china_date = get_china_date()
    all_items = []
    layer = 0

    while len(all_items) < target_count and layer <= 7:
        # Calculate target date for this layer
        target_date = china_date - datetime.timedelta(days=layer)

        # Build and execute search
        queries = build_company_queries(target_date, layer)
        results = execute_search(queries)

        # Filter and process
        filtered = filter_by_quality(results)

        if layer == 0:
            # Layer 0: Accept all quality items
            all_items.extend(filtered)
        else:
            # Layer 1+: Intelligent supplementation
            needed = target_count - len(all_items)
            supplements = select_supplements(
                current_items=all_items,
                candidates=filtered,
                needed=needed,
                layer=layer
            )
            all_items.extend(supplements)

        layer += 1

    return all_items
```

### Date Format Variations

Use multiple formats for maximum coverage:

```
Standard Formats:
- "November 7, 2025"
- "Nov 7 2025"
- "2025-11-07"
- "7 November 2025"

Relative Terms (Layer 0 only):
- "today"
- "今天" (Chinese)
- "last 24 hours"

Layer-Specific Hints:
- Layer 0: "breaking", "just announced", "launches today"
- Layer 1: "yesterday", "昨天"
```

---

## Source Priority Tiers

### Tier 1: Official Sources (Score 10/10)
- Company blogs and press releases
- Official Twitter/X accounts
- GitHub repos (for open source)
- Product documentation sites

### Tier 2: Major Tech Media (Score 9/10)
- TechCrunch
- The Verge
- Ars Technica
- VentureBeat
- Wired

### Tier 3: Financial News (Score 8/10)
- Bloomberg (product launches only, not just financial news)
- Reuters
- Wall Street Journal
- CNBC

### **Tier 4: Community & Product Discovery (Score 8/10)** ⭐ NEW
- **Product Hunt** (producthunt.com) - AI category, trending
- **Hacker News** (news.ycombinator.com) - Show HN, AI discussions
- **GitHub Trending** (github.com/trending) - AI repositories
- **Reddit** (r/artificial, r/MachineLearning) - product discussions
- **AI Product Aggregators**: There's An AI For That, Futurepedia

**Validation Required**: Community sources must have:
- Significant engagement (>100 upvotes/comments)
- Clear product description
- Working demo/link
- Cross-reference with Tier 1-2 sources when possible

### Tier 5: Social Media (Score 7/10, requires verification)
- Verified Twitter/X accounts
- LinkedIn company pages
- Reddit r/MachineLearning (with verification)

**Note**: Always cross-reference with Tier 1-3 sources

---

## Query Optimization Techniques

### Boolean Operators

```
AND: Both terms must appear
OR: Either term can appear
NOT: Exclude terms
"": Exact phrase match
(): Group terms
```

**Example**:
```
("OpenAI" OR "Anthropic") AND "funding" AND "2025" NOT "rumor"
```

### Wildcards and Variants

```
AI → "AI" OR "artificial intelligence" OR "machine learning"
chip → "chip" OR "semiconductor" OR "processor"
launch → "launch" OR "release" OR "unveil" OR "announce"
```

### Proximity Search

```
"OpenAI" NEAR "funding" (within 10 words)
"NVIDIA" ADJACENT "earnings" (next to each other)
```

### Negative Keywords

Exclude irrelevant results:

```
AI NOT ("air india" OR "amnesty international")
Meta NOT ("meta tag" OR "metadata")
Apple NOT ("apple fruit" OR "apple pie")
```

---

## Verification Query Templates

### Cross-Reference Query

After finding a story, verify with:

```
[Company name] [key fact] [date]
site:[official domain]
```

**Example**:
```
"Anthropic" "Google" "cloud partnership" "2025"
site:anthropic.com OR site:blog.google
```

### Fact-Checking Query

```
"[claimed fact]" AND ("confirms" OR "denies" OR "official")
```

**Example**:
```
"OpenAI 6 billion contract" AND ("confirms" OR "Pentagon")
```

---

## Language-Specific Queries

### English Sources
```
Primary query in English (as shown above)
Focus: US, Europe, global news
```

### Chinese Sources
```
Primary: "人工智能" OR "AI" OR "科技新闻" AND "今天"
Companies: "阿里巴巴" OR "腾讯" OR "百度" OR "华为"
Focus: China domestic news, policy, company developments

Sites:
site:36kr.com OR site:pingwest.com OR site:163.com OR site:sina.com.cn
```

---

## Sample Complete Search Sequence

### Morning Research Routine (China timezone) - v4.1 Product-Focused

```
1. Date calculation
   → Today is November 22, 2025 (CST)

2. 🚀 Product launches scan (15 queries) - HIGH PRIORITY
   → AI product launches today
   → New AI tools/websites
   → Each major company + "launch" OR "release"
   → Product Hunt trending AI (today + yesterday)
   → Hacker News "Show HN" AI (48h)

3. 🎯 Trending products (5 queries) - HIGH PRIORITY
   → GitHub trending AI repos
   → Reddit top AI tools discussions
   → AI product aggregator updates

4. 📊 Research & papers (5 queries) - MEDIUM PRIORITY
   → arXiv AI papers (today)
   → Major lab research announcements
   → Conference proceedings

5. 🤝 Activities & events (5 queries) - MEDIUM PRIORITY
   → AI conferences this week
   → Company keynotes/demos
   → Open source releases

6. 💼 Business & partnerships (5 queries) - MEDIUM PRIORITY
   → Strategic product partnerships
   → Major market shifts affecting products

7. 💰 Funding (3 queries) - LOW PRIORITY
   → Major funding only (≥$100M)
   → IPOs and unicorn valuations

8. Cross-reference verification (2 queries)
   → Verify top stories with official sources

Total: ~40 search queries
Expected yield: 60-80 raw results
Target output: 45-55 items with 60/30/10 ratio
Content mix: 60% products/tools, 30% activities/business, 10% investment
```

---

## Content Ratio Guidelines

**Target Distribution** (based on user preferences):

```yaml
High Priority (60%): ~27 items
  - Product Launches: 18 items (40%)
  - Trending AI Tools: 9 items (20%)

Medium Priority (30%): ~13 items
  - Research & Papers: 7 items (15%)
  - Activities & Events: 4 items (10%)
  - Business & Strategy: 2 items (5%)

Low Priority (10%): ~4-5 items
  - Major Funding: 4-5 items (10%)
  - Only rounds ≥$100M or strategic significance

Total: 45-55 items (after validation)
```

---

**Version**: 4.1.0
**Last Updated**: 2025-11-22
**Use Case**: Product-focused search strategy for daily-tech-news-search skill
**Key Changes**: Added community sources, increased product focus, deprioritized investment news