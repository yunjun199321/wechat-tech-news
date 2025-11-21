# Validation Rules Reference

> **Complete specification of hardcoded validation rules for daily-tech-news-validator v4.1**
> **v4.1 Update**: Added community sources + content type classification for product focus

## Domain Whitelists and Blacklists

### Tier 1 Sources (Credibility 9-10/10)

```yaml
International_Tech_Media:
  - techcrunch.com
  - theverge.com
  - arstechnica.com
  - venturebeat.com
  - wired.com
  - cnet.com
  - zdnet.com

Business_Financial:
  - bloomberg.com
  - reuters.com
  - cnbc.com
  - wsj.com
  - ft.com
  - economist.com
  - forbes.com/tech

Company_Official:
  - openai.com/blog
  - anthropic.com/news
  - blog.google
  - blogs.microsoft.com
  - ai.meta.com/blog
  - aws.amazon.com/blogs
  - nvidia.com/blog
```

### Tier 2 Sources (Credibility 7-8/10)

```yaml
Tech_Publications:
  - siliconangle.com
  - techtarget.com
  - infoworld.com
  - computerworld.com
  - itworld.com

Chinese_Tech_Media:
  - 36kr.com
  - tmtpost.com (钛媒体)
  - caixin.com (财新)
  - yicai.com (第一财经)
  - jiemian.com (界面新闻)
  - geekpark.net (极客公园)

Academic_Research:
  - arxiv.org
  - papers.nips.cc
  - openreview.net
  - research.google
  - research.fb.com

Community_Product_Discovery:
  - producthunt.com
  - news.ycombinator.com (Hacker News)
  - github.com/trending
  - reddit.com/r/artificial
  - reddit.com/r/MachineLearning
  
  Validation_Requirements:
    - Must have significant engagement (>100 upvotes/stars)
    - Clear product description and working link
    - Published within 48 hours
    - Cross-reference with official sources when available
    
  Credibility_Boost:
    - Product Hunt: Featured product → 8/10
    - Hacker News: Front page (>200 points) → 8/10
    - GitHub: >500 stars in 48h → 8/10
    - Reddit: >200 upvotes + verified → 7/10
```

### Blacklist (Auto-Reject)

```yaml
Social_Media: # Reject unless official company account
  - reddit.com
  - twitter.com
  - x.com
  - facebook.com
  - linkedin.com (posts, not company pages)
  - instagram.com

User_Generated:
  - medium.com (unless @companyname or verified blogger)
  - substack.com (unless verified tech journalist)
  - zhihu.com (知乎专栏, unless official account)
  - xiaohongshu.com (小红书)
  - douyin.com (抖音)
  - bilibili.com (unless official corporate channel)

Low_Quality:
  - content farms
  - ad-heavy sites
  - clickbait domains
  - affiliate marketing sites
```

### Special Cases

```yaml
Official_Social_Accounts: # Whitelist exceptions
  Allowed_Twitter:
    - twitter.com/OpenAI
    - twitter.com/AnthropicAI
    - twitter.com/Google
    - twitter.com/Microsoft
    - twitter.com/MetaAI
    - twitter.com/sama (Sam Altman)
    - twitter.com/ylecun (Yann LeCun)
    - twitter.com/karpathy (Andrej Karpathy)

  Validation:
    - Check for verified badge (blue checkmark)
    - Cross-reference with company website
    - Require screenshot or archive link

Verified_Blogs:
  - medium.com/@karpathy
  - substack.com/profile/[verified-tech-journalist]
  - Must have: verified badge + 10K+ followers + consistent tech content

Community_Exceptions:
  Product_Hunt_Criteria:
    - Must be in "Product of the Day" or top 10
    - Maker must have verified account
    - Product must have working demo/link
    
  Hacker_News_Criteria:
    - "Show HN" posts with >50 points
    - Top 30 on front page
    - Positive comment sentiment (not controversy)
    
  GitHub_Criteria:
    - Trending page (daily/weekly)
    - >100 stars gained in 24-48h
    - Active repository (recent commits)
    - Clear README and documentation
```

## Timestamp Parsing Rules

### Supported Formats

```yaml
ISO8601:
  Patterns:
    - "2025-11-20T14:30:00Z"
    - "2025-11-20T14:30:00+08:00"
    - "2025-11-20T14:30:00.123Z"
  Regex: "^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?(Z|[+-]\d{2}:\d{2})$"

RFC2822:
  Patterns:
    - "Wed, 20 Nov 2025 14:30:00 GMT"
    - "Wed, 20 Nov 2025 14:30:00 +0800"
  Regex: "^\w{3}, \d{1,2} \w{3} \d{4} \d{2}:\d{2}:\d{2} [+-]?\d{4}$"

Unix_Timestamp:
  Patterns:
    - 1732115400
    - "1732115400"
  Validation: "1700000000 < timestamp < 1800000000" (2023-2027 range)

Natural_Language:
  Relative:
    - "2 hours ago" → calculate from current time
    - "yesterday" → current date - 1 day
    - "3 days ago" → current date - 3 days
  Absolute:
    - "November 20, 2025"
    - "Nov 20, 2025"
    - "20 Nov 2025"
  Regex_Patterns:
    - "(\d+)\s+(hour|minute|day|week)s?\s+ago"
    - "yesterday|today"
    - "(\w+)\s+(\d{1,2}),?\s+(\d{4})"

HTML_Metadata:
  Sources:
    - '<meta property="article:published_time" content="[timestamp]">'
    - '<meta property="og:published_time" content="[timestamp]">'
    - '<time datetime="[timestamp]">'
    - '<script type="application/ld+json">..."datePublished":"[timestamp]"...</script>'
```

### Extraction Priority

```
Priority 1: HTML <meta> tags (most reliable)
Priority 2: JSON-LD structured data
Priority 3: <time> element with datetime attribute
Priority 4: Content text parsing (least reliable)
```

### Timezone Handling

```yaml
Default_Timezone: UTC
Target_Timezone: Asia/Shanghai (UTC+8)

Conversion_Rules:
  IF no timezone specified:
    Assume UTC
  IF PST/PDT (common for US tech news):
    Convert: PST = UTC-8, PDT = UTC-7
  IF CST/China:
    CST = UTC+8

Age_Calculation:
  current_time_china = datetime.now(timezone='Asia/Shanghai')
  article_time_china = parse_timestamp(article).astimezone('Asia/Shanghai')
  age_hours = (current_time_china - article_time_china).total_seconds() / 3600
```

## AI Relevance Keywords

### Primary AI Keywords (High Confidence)

```yaml
Core_AI_Terms:
  - artificial intelligence
  - AI (as standalone or prefix: "AI model", "AI chip")
  - machine learning
  - deep learning
  - neural network
  - large language model
  - LLM
  - generative AI
  - foundation model

Model_Names:
  - GPT-3|GPT-4|GPT-5
  - ChatGPT
  - Claude (Anthropic)
  - Gemini|Bard (Google)
  - LLaMA|Llama (Meta)
  - PaLM
  - DALL-E|Midjourney|Stable Diffusion
  - Copilot (Microsoft)

Technical_Terms:
  - transformer
  - attention mechanism
  - RLHF (reinforcement learning from human feedback)
  - fine-tuning
  - prompt engineering
  - few-shot learning
  - zero-shot learning
  - multimodal
  - diffusion model
```

### Secondary AI Keywords (Context Required)

```yaml
AI_Application_Areas:
  - computer vision (require AI context)
  - natural language processing|NLP (require AI context)
  - speech recognition (require AI context)
  - autonomous driving (require AI/perception context)
  - recommendation system (require ML context)

AI_Infrastructure:
  - AI chip (explicit)
  - AI accelerator (explicit)
  - tensor processing unit|TPU
  - H100|A100|MI300 (NVIDIA/AMD AI chips)
  - inference engine
  - training cluster
  - AI data center

AI_Ethics_Safety:
  - AI alignment
  - AI safety
  - responsible AI
  - AI governance
  - AGI (artificial general intelligence)
  - AI regulation
```

### Company + AI Context Rules

```yaml
Requires_AI_Context: # Company name alone insufficient
  NVIDIA:
    Required_Keywords:
      - AI chip|H100|A100|Blackwell
      - AI data center
      - AI training|inference
    Excluded:
      - gaming GPU (unless "AI-enhanced gaming")
      - crypto mining
      - automotive (unless "autonomous driving AI")

  AMD:
    Required_Keywords:
      - MI300|Instinct
      - AI accelerator
      - ROCm (AMD AI software)
    Excluded:
      - Ryzen|EPYC (unless "AI workload")
      - Radeon gaming

  Apple:
    Required_Keywords:
      - Apple Intelligence
      - on-device AI
      - neural engine
      - Core ML
    Excluded:
      - iOS updates (unless AI features)
      - hardware specs (unless AI chip)

  Intel:
    Required_Keywords:
      - Gaudi (AI chip)
      - Habana Labs
      - AI PC
    Excluded:
      - desktop CPU
      - server CPU (unless AI workload)
```

### Exclusion Patterns (Auto-Reject)

```yaml
Non_AI_Semiconductor:
  Patterns:
    - "semiconductor manufacturing" WITHOUT "AI chip"
    - "3nm|5nm process" WITHOUT "AI|GPU|accelerator"
    - "foundry capacity" WITHOUT "AI chip"
    - "lithography|EUV" WITHOUT "AI chip production"
    - "rare earth|silicon wafer" WITHOUT "AI hardware"

Non_AI_Tech:
  Patterns:
    - "5G|6G network" WITHOUT "AI network optimization"
    - "cloud computing" WITHOUT "AI|ML service"
    - "blockchain|cryptocurrency" WITHOUT "AI application"
    - "quantum computing" WITHOUT "AI acceleration|algorithm"
    - "metaverse" WITHOUT "AI avatar|generation"

Gaming_Unless_AI:
  Patterns:
    - "gaming GPU|graphics card" WITHOUT "AI training"
    - "game engine" WITHOUT "AI NPC|procedural generation"
    - "esports" WITHOUT "AI analysis"
```

### Validation Logic

```python
def validate_ai_relevance(item):
    """
    Returns: (is_ai_relevant: bool, confidence: float, matched_keywords: list)
    """
    title = item['title'].lower()
    summary = item['summary'].lower()
    content = title + " " + summary

    # Check primary keywords (high confidence)
    for keyword in PRIMARY_AI_KEYWORDS:
        if keyword.lower() in content:
            return (True, 1.0, [keyword])

    # Check company + AI context
    company = extract_company(item)
    if company in REQUIRES_AI_CONTEXT:
        required = REQUIRES_AI_CONTEXT[company]['required_keywords']
        excluded = REQUIRES_AI_CONTEXT[company]['excluded']

        has_required = any(kw in content for kw in required)
        has_excluded = any(kw in content for kw in excluded)

        if has_required and not has_excluded:
            return (True, 0.8, [company, 'context-matched'])
        elif has_excluded:
            return (False, 0.0, ['excluded-pattern'])

    # Check exclusion patterns
    for pattern in EXCLUSION_PATTERNS:
        if matches_pattern(content, pattern):
            return (False, 0.0, [pattern])

    # Secondary keywords (manual review)
    for keyword in SECONDARY_AI_KEYWORDS:
        if keyword.lower() in content:
            return (None, 0.5, [keyword, 'needs-manual-review'])

    # No AI relevance detected
    return (False, 0.0, ['no-ai-keywords'])
```

## Deduplication Rules

### Title Similarity Detection

```python
def calculate_title_similarity(title1, title2):
    """
    Uses multiple similarity metrics
    """
    # Exact match
    if title1.lower() == title2.lower():
        return 1.0

    # Levenshtein distance
    lev_similarity = 1 - (levenshtein(title1, title2) / max(len(title1), len(title2)))

    # Word overlap
    words1 = set(title1.lower().split())
    words2 = set(title2.lower().split())
    jaccard_similarity = len(words1 & words2) / len(words1 | words2)

    # Combined score (weighted average)
    combined = 0.3 * lev_similarity + 0.7 * jaccard_similarity

    # Threshold
    if combined >= 0.8:
        return combined  # Likely duplicate
    else:
        return combined

def is_duplicate_title(title1, title2):
    return calculate_title_similarity(title1, title2) >= 0.8
```

### Content Fingerprinting

```python
def generate_fingerprint(item):
    """
    Creates unique fingerprint from key entities
    """
    company = extract_company(item)
    product = extract_product(item)
    event_type = extract_event_type(item)  # launch, funding, earnings, etc.
    amount = extract_amount(item)  # funding amount, revenue, etc.
    date = item['published_date'].date()

    fingerprint = f"{company}|{product}|{event_type}|{amount}|{date}"
    return hashlib.md5(fingerprint.encode()).hexdigest()

def are_duplicate_stories(item1, item2):
    """
    Two items are duplicates if:
    1. Same fingerprint, OR
    2. Same company + event type + date AND similar titles
    """
    fp1 = generate_fingerprint(item1)
    fp2 = generate_fingerprint(item2)

    if fp1 == fp2:
        return True

    # Fuzzy match
    same_company = extract_company(item1) == extract_company(item2)
    same_event = extract_event_type(item1) == extract_event_type(item2)
    same_date = item1['published_date'].date() == item2['published_date'].date()
    similar_title = is_duplicate_title(item1['title'], item2['title'])

    return same_company and same_event and same_date and similar_title
```

### URL Deduplication

```python
def normalize_url(url):
    """
    Removes tracking parameters and normalizes URL
    """
    parsed = urlparse(url)
    # Remove query parameters (tracking, utm, etc.)
    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    # Remove trailing slashes
    return clean_url.rstrip('/')

def are_duplicate_urls(url1, url2):
    """
    URLs are duplicates if:
    1. Exact match after normalization, OR
    2. Same domain + very similar path
    """
    norm1 = normalize_url(url1)
    norm2 = normalize_url(url2)

    if norm1 == norm2:
        return True

    # Check same domain + similar path
    parsed1 = urlparse(norm1)
    parsed2 = urlparse(norm2)

    if parsed1.netloc != parsed2.netloc:
        return False

    # Path similarity (for same-domain different-article-url cases)
    path_sim = calculate_title_similarity(parsed1.path, parsed2.path)
    return path_sim >= 0.9
```

### Merge Strategy

```python
def merge_duplicates(items):
    """
    When duplicates found, merge into single item with best attributes
    """
    def get_priority_score(item):
        """
        Priority ranking for keeping/merging
        """
        score = 0

        # Source tier (highest weight)
        if item['source']['tier'] == 1:
            score += 100
        elif item['source']['tier'] == 2:
            score += 50

        # Recency (within 48h, more recent is better)
        age_hours = item['timestamp']['age_hours']
        score += max(0, 48 - age_hours)  # Up to +48 points

        # Completeness
        score += item['completeness']['score']  # Up to +10 points

        # Content length (more detail is better)
        score += min(item['completeness']['summary_length'] / 10, 30)  # Up to +30 points

        return score

    # Sort by priority
    sorted_items = sorted(items, key=get_priority_score, reverse=True)
    primary = sorted_items[0]
    secondaries = sorted_items[1:]

    # Merge key details
    merged = primary.copy()
    merged['sources_merged'] = [primary['source']] + [s['source'] for s in secondaries]
    merged['duplicate_count'] = len(items)

    # Enhance summary with unique details from secondaries
    for secondary in secondaries:
        # Extract unique data points not in primary
        unique_data = extract_unique_data(secondary, primary)
        if unique_data:
            merged['summary'] += f" {unique_data}"

    return merged
```

## Completeness Scoring

### Required Fields Matrix

```yaml
Essential_Fields: # Missing any → reject item
  - title: String, 10-200 characters
  - source_url: Valid HTTP/HTTPS URL
  - source_name: String, recognizable publication
  - published_date: Valid timestamp
  - summary: String, ≥50 characters

Important_Fields: # Missing → lower score by 20%
  - company_name: String
  - category: String (AI Models, Funding, Product Launch, etc.)
  - key_data: Dict with amount/metric
  - compliance_flags: List (can be empty)

Optional_Fields: # Missing → lower score by 5%
  - author: String
  - tags: List[String]
  - image_url: URL
  - related_links: List[URL]
```

### Content Quality Scoring

```python
def score_completeness(item):
    """
    Returns completeness score 0-10
    """
    score = 10.0  # Start with perfect score

    # Essential fields check (fatal if missing)
    essential = ['title', 'source_url', 'source_name', 'published_date', 'summary']
    for field in essential:
        if not item.get(field):
            return 0.0  # Auto-reject

    # Summary length check
    summary_len = len(item['summary'])
    if summary_len < 50:
        return 0.0  # Too brief, reject
    elif summary_len < 150:
        score -= 2.0  # Marginal, penalize
    elif summary_len > 300:
        score -= 1.0  # Too verbose, minor penalty

    # Important fields check
    important = ['company_name', 'category', 'key_data']
    for field in important:
        if not item.get(field):
            score -= 2.0

    # Key data presence (context-dependent)
    if item.get('category') == 'Funding':
        if not has_funding_details(item['key_data']):
            score -= 1.5
    elif item.get('category') == 'Product Launch':
        if not has_product_details(item['key_data']):
            score -= 1.5
    elif item.get('category') == 'Financial Results':
        if not has_financial_metrics(item['key_data']):
            score -= 1.5

    # Context and depth check
    if not has_impact_statement(item['summary']):
        score -= 1.0
    if not has_quotes(item['summary']):
        score -= 0.5

    # Optional fields (minor bonus)
    optional = ['author', 'tags', 'image_url']
    for field in optional:
        if item.get(field):
            score += 0.3

    return max(0.0, min(10.0, score))

def has_funding_details(key_data):
    """Funding news must have: amount, currency, round type"""
    required = ['amount', 'currency', 'round_type']
    return all(key_data.get(k) for k in required)

def has_product_details(key_data):
    """Product launch must have: product name, key feature, release date"""
    required = ['product_name', 'key_feature', 'release_date']
    return all(key_data.get(k) for k in required)

def has_financial_metrics(key_data):
    """Financial results must have: metric, value, change %"""
    required = ['metric', 'value', 'change_percentage']
    return all(key_data.get(k) for k in required)

def has_impact_statement(summary):
    """Check if summary explains why this matters"""
    impact_indicators = [
        'significant', 'major', 'breakthrough', 'first', 'largest',
        'will enable', 'represents', 'marks', 'could', 'expected to'
    ]
    return any(indicator in summary.lower() for indicator in impact_indicators)

def has_quotes(summary):
    """Check if summary includes quotes from officials"""
    return '"' in summary or '"' in summary or '"' in summary
```

## Quality Gate Thresholds

### Master Thresholds Table

| Metric | Minimum | Target | Excellent | Action on Fail |
|--------|---------|--------|-----------|----------------|
| Source Credibility Avg | 7.0/10 | 8.0/10 | 8.5/10 | TERMINATE workflow |
| Time Compliance Rate | 100% | 100% | 100% | TERMINATE workflow |
| AI Relevance Rate | 95% | 98% | 100% | Remove non-AI items |
| Deduplication Rate | 95% | 97% | 98% | Re-run dedup logic |
| Completeness Avg | 7.0/10 | 8.0/10 | 8.5/10 | TERMINATE workflow |
| Final Item Count | 40-50 | 45-50 | 48-50 | Adjust search scope |
| Tier 1 Source Rate | 60% | 70% | 80% | WARNING only |
| Layer 0 (0-24h) Rate | 60% | 75% | 85% | WARNING only |

### Composite Quality Score

```python
def calculate_composite_quality(metrics):
    """
    Weighted composite score across all dimensions
    """
    weights = {
        'source_credibility': 0.25,
        'time_compliance': 0.20,
        'ai_relevance': 0.20,
        'deduplication': 0.15,
        'completeness': 0.20
    }

    composite = (
        metrics['source_credibility']['average'] / 10 * weights['source_credibility'] +
        metrics['time_accuracy']['compliance_rate'] * weights['time_compliance'] +
        metrics['ai_relevance']['relevance_rate'] * weights['ai_relevance'] +
        metrics['deduplication']['dedup_rate'] * weights['deduplication'] +
        metrics['completeness']['average'] / 10 * weights['completeness']
    ) * 10  # Scale to 0-10

    return composite

# Grade mapping
def get_quality_grade(composite_score):
    if composite_score >= 9.0:
        return 'A+', 'Excellent'
    elif composite_score >= 8.5:
        return 'A', 'Very Good'
    elif composite_score >= 8.0:
        return 'B+', 'Good'
    elif composite_score >= 7.5:
        return 'B', 'Acceptable'
    elif composite_score >= 7.0:
        return 'C', 'Marginal Pass'
    else:
        return 'F', 'Fail - Below Minimum Standards'
```

---

**Version**: 4.1.0
**Rule Type**: Hardcoded (70%) + LLM-assisted (30%)
**Update Frequency**: Monthly or as needed based on validation failures
**Maintenance**: Add new domains/patterns as they emerge in real-world usage
## Round 6: Content Type Classification (NEW in v4.1)

### Purpose

Classify news items by content type to implement 60/30/10 ratio (product/business/investment focus).

### Content Type Categories

```yaml
Product_Launch: # HIGH PRIORITY (Weight: 1.0x)
  Keywords_Required:
    - Primary: "launch", "release", "unveil", "announce", "introduces", "available now"
    - Products: "model", "tool", "app", "API", "SDK", "feature", "version"
    - Examples: "GPT-5 launch", "new Claude API", "GitHub Copilot update"
  
  Exclusions:
    - Pre-announcements without release date
    - "Coming soon" without concrete timeline
    - Vaporware or concept demos
  
  Scoring: 10/10 (highest priority)

Trending_Product: # HIGH PRIORITY (Weight: 1.0x)
  Sources_Required:
    - Product Hunt (>100 upvotes)
    - Hacker News (Show HN, >50 points)
    - GitHub Trending (>100 stars in 48h)
    - Reddit (>200 upvotes, r/artificial or r/MachineLearning)
  
  Validation:
    - Must have working demo or live product
    - Clear product name and description
    - Community engagement metrics met
  
  Scoring: 9/10 (very high priority)

Research_Activity: # MEDIUM PRIORITY (Weight: 0.8x)
  Keywords_Required:
    - "research paper", "study", "breakthrough", "discovery"
    - "arXiv", "conference", "NeurIPS", "ICML", "CVPR"
    - "open source", "GitHub release", "published findings"
  
  Validation:
    - Must have paper link or GitHub repo
    - Published within 48 hours
    - From recognized lab or conference
  
  Scoring: 8/10

Event_Activity: # MEDIUM PRIORITY (Weight: 0.7x)
  Keywords_Required:
    - "conference", "summit", "keynote", "demo day"
    - "partnership" (product-focused only)
    - "collaboration" (with deliverable)
  
  Validation:
    - Must have event date or partnership details
    - Product/tech focus (not generic business)
  
  Scoring: 7/10

Business_News: # MEDIUM PRIORITY (Weight: 0.5x)
  Keywords_Required:
    - "strategy", "expansion", "enterprise adoption"
    - "leadership" (C-level only)
    - "partnership" (strategic, non-product)
  
  Exclusions:
    - Generic HR announcements
    - Routine operational updates
    - Marketing fluff
  
  Scoring: 6/10

Investment_Funding: # LOW PRIORITY (Weight: 0.3x)
  Keywords_Required:
    - "funding", "investment", "Series C/D/E", "IPO"
    - "$XXM", "valuation", "raise", "venture capital"
  
  Strict_Filters:
    - Amount ≥ $100 million (mandatory)
    - Company must have shipped products (not pure R&D)
    - Strategic significance beyond money
  
  Exclusions:
    - Series A/B rounds (unless breakthrough tech)
    - Routine venture rounds
    - Acquisition rumors (confirmed only)
  
  Scoring: 3/10 (lowest priority)
```

### Classification Algorithm

```python
def classify_content_type(item):
    """
    Classify news item into content type categories
    Returns: (category, score, confidence)
    """
    title = item['title'].lower()
    content = item['content'].lower() if item.get('content') else ''
    source = item['source']
    
    # Check Product Launch
    product_keywords = ['launch', 'release', 'unveil', 'announce', 'introduces', 'available now']
    product_nouns = ['model', 'tool', 'app', 'api', 'sdk', 'feature', 'version', 'gpt', 'claude', 'gemini']
    
    if any(kw in title for kw in product_keywords) and any(noun in title for noun in product_nouns):
        if not any(excl in content for excl in ['coming soon', 'concept', 'preview']):
            return ('Product_Launch', 10, 0.9)
    
    # Check Trending Product
    if source in ['producthunt.com', 'news.ycombinator.com', 'github.com/trending']:
        engagement = item.get('engagement', {})
        if engagement.get('upvotes', 0) > 100 or engagement.get('stars', 0) > 100:
            return ('Trending_Product', 9, 0.85)
    
    # Check Research Activity
    research_keywords = ['research', 'paper', 'study', 'breakthrough', 'arxiv', 'conference']
    if any(kw in title for kw in research_keywords):
        if 'arxiv.org' in source or any(conf in content for conf in ['neurips', 'icml', 'cvpr']):
            return ('Research_Activity', 8, 0.8)
    
    # Check Event Activity
    event_keywords = ['conference', 'summit', 'keynote', 'demo day', 'partnership']
    if any(kw in title for kw in event_keywords):
        return ('Event_Activity', 7, 0.75)
    
    # Check Investment Funding
    funding_keywords = ['funding', 'investment', 'series', 'raise', '$', 'million', 'valuation']
    if any(kw in title for kw in funding_keywords):
        amount = extract_funding_amount(content)
        if amount and amount >= 100:  # $100M minimum
            return ('Investment_Funding', 3, 0.7)
        else:
            return ('Investment_Funding', 1, 0.5)  # Below threshold, very low priority
    
    # Default: Business News
    return ('Business_News', 6, 0.6)

def extract_funding_amount(text):
    """Extract funding amount in millions"""
    import re
    patterns = [
        r'\$(\d+(?:\.\d+)?)\s*(?:million|M)',
        r'\$(\d+(?:\.\d+)?)\s*(?:billion|B)',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            amount = float(match.group(1))
            if 'billion' in match.group(0).lower() or 'B' in match.group(0):
                amount *= 1000  # Convert to millions
            return amount
    return None
```

### Weighted Scoring System

```python
def apply_content_type_weights(items):
    """
    Apply weight multipliers based on content type
    Returns: sorted list with weighted scores
    """
    weighted_items = []
    
    for item in items:
        category, base_score, confidence = classify_content_type(item)
        
        # Get weight multiplier
        weights = {
            'Product_Launch': 1.0,
            'Trending_Product': 1.0,
            'Research_Activity': 0.8,
            'Event_Activity': 0.7,
            'Business_News': 0.5,
            'Investment_Funding': 0.3
        }
        
        weight = weights.get(category, 0.5)
        final_score = base_score * weight * confidence
        
        item['content_type'] = category
        item['content_score'] = final_score
        item['content_weight'] = weight
        weighted_items.append(item)
    
    # Sort by weighted score (descending)
    weighted_items.sort(key=lambda x: x['content_score'], reverse=True)
    
    return weighted_items
```

### Selection Strategy (60/30/10 Ratio)

```python
def select_balanced_items(weighted_items, target_count=45):
    """
    Select items maintaining 60/30/10 ratio
    
    Target distribution:
    - High Priority (Product + Trending): 60% (~27 items)
    - Medium Priority (Research + Events + Business): 30% (~13 items)
    - Low Priority (Investment): 10% (~4-5 items)
    """
    selected = []
    
    # High Priority: 27 items
    high_priority = [item for item in weighted_items 
                     if item['content_type'] in ['Product_Launch', 'Trending_Product']]
    selected.extend(high_priority[:27])
    
    # Medium Priority: 13 items
    medium_priority = [item for item in weighted_items 
                       if item['content_type'] in ['Research_Activity', 'Event_Activity', 'Business_News']]
    selected.extend(medium_priority[:13])
    
    # Low Priority: 5 items (investment only if ≥$100M)
    low_priority = [item for item in weighted_items 
                    if item['content_type'] == 'Investment_Funding']
    low_priority_filtered = [item for item in low_priority 
                             if extract_funding_amount(item.get('content', '')) >= 100]
    selected.extend(low_priority_filtered[:5])
    
    # If we don't have enough items, backfill with next best
    if len(selected) < target_count:
        remaining = [item for item in weighted_items if item not in selected]
        needed = target_count - len(selected)
        selected.extend(remaining[:needed])
    
    return selected[:target_count]
```

### Quality Gate for Round 6

```yaml
Minimum_Requirements:
  High_Priority_Count: ≥ 24 items (products + trending)
  Medium_Priority_Count: ≥ 10 items (research + events + business)
  Low_Priority_Count: ≤ 6 items (investment)
  
  Content_Type_Balance:
    - No single type > 50% of total
    - Product types must be ≥ 40% of total
    - Investment must be ≤ 15% of total

Pass_Criteria:
  - High priority count ≥ 24 → ✅ PASS
  - Investment count ≤ 6 → ✅ PASS
  - Product ratio ≥ 40% → ✅ PASS
  
Fail_Actions:
  - High priority < 24 → Request more product-focused searches
  - Investment > 6 → Drop lowest-scored investment items
  - Product ratio < 40% → Increase product weight, re-sort
```

### Round 6 Output

```markdown
## Round 6: Content Type Classification

**Content Distribution**:
- 🚀 Product Launches: 18 items (40%)
- 🎯 Trending Products: 9 items (20%)
- 📊 Research & Papers: 7 items (15%)
- 🤝 Events & Activities: 4 items (9%)
- 💼 Business News: 3 items (7%)
- 💰 Investment (≥$100M): 4 items (9%)

**Total**: 45 items
**Ratio**: 60% high priority / 30% medium / 10% low ✅

**Quality Gate**: PASS
- Product focus ≥ 40%: ✅ 60%
- Investment ≤ 15%: ✅ 9%
- Balance maintained: ✅

**Top Products Identified**:
1. [Product Name] - [Company] - [Launch Date] - Score: 9.5/10
2. [Trending Tool] - [Source: Product Hunt] - 250 upvotes - Score: 9.2/10
...

**Investment Items (Deprioritized)**:
1. [Company] raises $150M Series C - Score: 2.1/10 (included for significance)
2. [Company] IPO valued at $5B - Score: 2.5/10
...
```

---

**Version**: 4.1.0 - Round 6 Added
**Purpose**: Product-focused content curation with quantitative ratio enforcement
**Impact**: Reduces investment news from ~30% to ~10%, increases product coverage to ~60%
