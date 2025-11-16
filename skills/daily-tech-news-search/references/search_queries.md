# Search Query Reference

## Overview

This document provides optimized search queries for the daily-tech-news-search skill. Queries are organized by company, topic, and search strategy.

---

## Company-Specific Queries

### AI Companies

#### OpenAI
```
Primary: "OpenAI" AND (news OR announcement OR release) AND "today"
Secondary: "ChatGPT" OR "GPT-4" OR "GPT-5" OR "Sam Altman"
Focus: products, partnerships, funding, research
```

#### Anthropic
```
Primary: "Anthropic" AND (news OR announcement) AND "today"
Secondary: "Claude" OR "constitutional AI" OR "Dario Amodei"
Focus: Claude updates, safety research, Google partnership, funding
```

#### Google/DeepMind
```
Primary: ("Google AI" OR "DeepMind" OR "Gemini") AND news AND "today"
Secondary: "Bard" OR "PaLM" OR "Demis Hassabis"
Focus: Gemini updates, DeepMind research, AI infrastructure
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

#### NVIDIA
```
Primary: "NVIDIA" AND (AI OR chip) AND news AND "today"
Secondary: "Jensen Huang" OR "H100" OR "Blackwell" OR "stock"
Focus: AI chips, market performance, partnerships, data centers
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

### Funding & Investment

```
Primary: ("AI funding" OR "AI investment" OR "venture capital") AND "today"
Secondary: ("Series A" OR "Series B" OR "Series C") AND "AI"
Focus: Major rounds (>$50M), unicorn valuations, strategic investments

Filters:
- Amount ≥ $50 million
- AI/tech companies only
- Announced within 24 hours
```

### Chip & Semiconductor

```
Primary: ("AI chip" OR "semiconductor" OR "GPU") AND news AND "today"
Secondary: "AI accelerator" OR "TPU" OR "NPU"
Focus: New products, manufacturing, policy, market data

Sub-queries:
- Manufacturing: "fab" OR "foundry" OR "node"
- Policy: "export control" OR "CHIPS Act" OR "subsidy"
- Competition: "market share" OR "benchmark"
```

### Quantum Computing

```
Primary: "quantum computing" AND (news OR breakthrough OR commercial) AND "today"
Secondary: "quantum" AND ("IBM" OR "Google" OR "IonQ" OR "Rigetti")
Focus: Commercialization, breakthroughs, partnerships

Key terms:
- Qubit count and quality
- Error correction
- Commercial availability
- Application cases
```

### AI Regulation & Policy

```
Primary: ("AI regulation" OR "AI policy" OR "AI law") AND "today"
Secondary: "EU AI Act" OR "executive order" OR "privacy"
Focus: New regulations, enforcement, compliance

Geographic queries:
- US: "FTC" OR "FCC" OR "Congress"
- EU: "EU AI Act" OR "GDPR"
- China: "CAC" OR "网信办"
```

### Cybersecurity & Privacy

```
Primary: ("AI security" OR "privacy" OR "data protection") AND news AND "today"
Secondary: "breach" OR "vulnerability" OR "encryption"
Focus: Security incidents, new protections, compliance

Key areas:
- AI-specific vulnerabilities
- Privacy regulations
- Security products
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
# Pseudo-code for date calculation
import datetime

def get_china_date():
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

### Date Format Variations

Use multiple formats for maximum coverage:

```
"November 7, 2025"
"Nov 7 2025"
"2025-11-07"
"7 November 2025"
"今天" (today, for Chinese sources)
"last 24 hours"
```

---

## Source Priority Tiers

### Tier 1: Official Sources (Score 10/10)
- Company blogs and press releases
- Official Twitter/X accounts
- SEC filings and investor relations
- Government announcements

**Search example**:
```
site:openai.com OR site:anthropic.com OR site:blog.google
```

### Tier 2: Major Tech Media (Score 9/10)
- TechCrunch
- The Verge
- Ars Technica
- VentureBeat
- Wired

**Search example**:
```
site:techcrunch.com OR site:theverge.com OR site:arstechnica.com
```

### Tier 3: Financial News (Score 9/10)
- Bloomberg
- Reuters
- Wall Street Journal
- Financial Times
- CNBC

**Search example**:
```
site:bloomberg.com OR site:reuters.com OR site:wsj.com
```

### Tier 4: Industry Analysis (Score 8/10)
- InfoQ
- IEEE Spectrum
- MIT Technology Review
- Hacker News (with verification)

**Search example**:
```
site:infoq.com OR site:spectrum.ieee.org OR site:technologyreview.com
```

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

### Morning Research Routine (China timezone)

```
1. Date calculation
   → Today is November 7, 2025 (CST)

2. Breaking news scan (10 queries)
   → AI breaking news today
   → Tech breaking news today
   → Each major company + "today"

3. Company-specific deep dive (15 queries)
   → One query per major company
   → Include subsidiaries and products

4. Topic-specific search (10 queries)
   → Funding announcements
   → Product launches
   → Policy/regulation
   → Market performance
   → Research breakthroughs

5. Cross-reference verification (5 queries)
   → Verify top stories with official sources
   → Check financial data with multiple sources

Total: ~40 search queries
Expected yield: 80-120 raw results
Target output: 50 verified items
```

---

**Version**: 1.0
**Last Updated**: 2025-01-07
**Use Case**: Search query reference for daily-tech-news-search skill
