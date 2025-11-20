# Validation Rules Reference

> **Complete specification of hardcoded validation rules for daily-tech-news-validator v4.0**

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

**Version**: 4.0.0
**Rule Type**: Hardcoded (70%) + LLM-assisted (30%)
**Update Frequency**: Monthly or as needed based on validation failures
**Maintenance**: Add new domains/patterns as they emerge in real-world usage
