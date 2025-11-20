---
name: daily-tech-news-validator
description: Mandatory multi-round data validation engine with hardcoded rules for source credibility, time accuracy, AI relevance, deduplication, and quality assurance. Generates validation_report.md with pass/fail gates.
---

# Daily Tech News Validator

> **🔒 Hardcoded Validation Engine**: Mandatory 5-10 round validation with rule-based checks and quality gates

## When to Use This Skill

Use this skill when you need to:
- Validate raw search results from `daily-tech-news-search` before content writing
- Ensure data accuracy, source credibility, and time freshness with hardcoded rules
- Generate mandatory validation reports that workflow can verify
- Implement quality gates that terminate workflow on failure
- Provide audit trail for data quality assurance

**IMPORTANT**: This skill is designed to run automatically in the workflow pipeline. It MUST generate `validation_report.md` - the workflow will check for this file's existence and completeness.

## Quick Start

```bash
使用 daily-tech-news-validator skill [input-file]
```

**Execution Time**: 3-5 minutes
**Input**: `tech_news_[YYYYMMDD]_raw.md` (from daily-tech-news-search)
**Output**: `validation_report_[YYYYMMDD].md` + `tech_news_[YYYYMMDD]_validated.json`

## Core Validation Rounds (Mandatory)

### Round 1: Source Credibility Validation

**Hardcoded Rules**:
```yaml
Domain_Whitelist_Tier1: # Credibility 9-10/10
  - techcrunch.com
  - bloomberg.com
  - reuters.com
  - theverge.com
  - arstechnica.com
  - venturebeat.com
  - cnbc.com
  - wsj.com
  - ft.com
  - economist.com

Domain_Whitelist_Tier2: # Credibility 7-8/10
  - wired.com
  - zdnet.com
  - cnet.com
  - techtarget.com
  - siliconangle.com
  - 36kr.com
  - tmtpost.com
  - caixin.com
  - yicai.com

Domain_Blacklist: # Auto-reject
  - reddit.com (除非官方公告链接)
  - twitter.com/x.com (除非官方公司账号)
  - 个人博客（除非verified tech blogger）
  - Medium（除非official company blog）
  - 自媒体平台（小红书、知乎专栏等，除非官方账号）

Validation_Logic:
  IF domain IN Tier1:
    credibility_score = 9-10
  ELIF domain IN Tier2:
    credibility_score = 7-8
  ELIF domain IN Blacklist:
    credibility_score = 0, ❌ Auto-reject
  ELSE:
    credibility_score = LLM评估（5-8分）+ manual review flag

Quality_Gate:
  - Average credibility ≥7.0/10 → ✅ PASS
  - Average credibility <7.0/10 → ❌ FAIL, terminate workflow
  - Items from blacklist >5% → ❌ FAIL, terminate workflow
```

**Report Output**:
```markdown
## Round 1: Source Credibility

- Total Items: 50
- Tier 1 Sources: 35 (70%)
- Tier 2 Sources: 12 (24%)
- Unverified Sources: 3 (6%, flagged for review)
- Blacklisted Sources: 0 (0%)
- Average Credibility: 8.2/10

✅ PASS - Meets minimum threshold (≥7.0/10)
```

### Round 2: Time Accuracy Validation (Strict 48h Mode)

**Hardcoded Rules**:
```yaml
Timestamp_Formats: # Auto-parse these formats
  - ISO8601: "2025-11-20T14:30:00Z"
  - RFC2822: "Wed, 20 Nov 2025 14:30:00 GMT"
  - Unix: 1732115400
  - HTML5: "2025-11-20T14:30:00+08:00"
  - Natural: "2 hours ago", "yesterday", "Nov 20, 2025"

Extraction_Sources:
  1. <meta property="article:published_time">
  2. <time datetime="">
  3. JSON-LD datePublished
  4. og:published_time
  5. Content text patterns ("Published: ...", "Updated: ...")

Double_Verification:
  Check1_Metadata:
    - Parse timestamp from HTML metadata
    - Calculate age in hours

  Check2_Content:
    - Scan article text for time indicators
    - Extract relative time ("3 hours ago", "yesterday")
    - Convert to absolute timestamp

  Cross_Validation:
    IF |metadata_age - content_age| > 12 hours:
      🚨 FLAG inconsistency, require manual review

Time_Layers:
  Layer0_Today: # 0-24h
    - Priority: Highest
    - Weight: 1.00
    - Action: Auto-include all

  Layer1_Yesterday: # 24-48h
    - Priority: High
    - Weight: 0.90
    - Action: Include only if needed for balance

  Layer2_Older: # >48h
    - Priority: Reject
    - Action: Auto-reject unless importance ≥9.5/10 + manual approval

Quality_Gate:
  - 100% items within 48h → ✅ PASS
  - Any item >48h without manual approval → ❌ FAIL
  - >20% timestamp inconsistencies → ❌ FAIL
  - Average age >36h → ⚠️ WARNING (still pass but flag)
```

**Report Output**:
```markdown
## Round 2: Time Accuracy

- Total Items: 50
- Layer 0 (0-24h): 38 items (76%)
- Layer 1 (24-48h): 12 items (24%)
- Average Age: 14.2 hours

Time Validation Details:
- Successfully parsed timestamps: 48/50 (96%)
- Manual time estimation: 2/50 (4%)
- Cross-validation inconsistencies: 1/50 (2%, flagged)

✅ PASS - All items within 48h window
```

### Round 3: AI Relevance Validation

**Hardcoded Rules**:
```yaml
AI_Keywords_Required: # Must contain at least ONE
  Primary:
    - artificial intelligence
    - AI model
    - large language model
    - LLM
    - machine learning
    - deep learning
    - neural network
    - generative AI
    - ChatGPT
    - GPT-4/GPT-5
    - Claude
    - Gemini
    - training data
    - inference
    - AI chip
    - AI accelerator
    - data center AI

  Secondary:
    - transformer
    - attention mechanism
    - reinforcement learning
    - computer vision
    - natural language processing
    - NLP
    - AI safety
    - alignment
    - AGI
    - multimodal

Company_AI_Context: # Company + AI keyword required
  - OpenAI
  - Anthropic
  - Google (+ AI/DeepMind/Gemini)
  - Microsoft (+ Azure AI/Copilot)
  - Meta (+ AI/LLaMA/PyTorch)
  - Amazon (+ AWS AI/Bedrock)
  - Apple (+ Intelligence/ML)
  - NVIDIA (+ H100/A100/AI chip)
  - AMD (+ MI300/AI accelerator)
  - xAI
  - Mistral AI
  - Cohere
  - Stability AI
  - Midjourney

Exclusion_Patterns: # Auto-reject if matched
  Non_AI_Topics:
    - "semiconductor manufacturing" WITHOUT "AI chip"
    - "rare earth" OR "lithography" OR "EUV"
    - "quantum computing" WITHOUT "AI application"
    - "cryptocurrency" OR "blockchain" WITHOUT "AI"
    - "5G" OR "6G" WITHOUT "AI network"
    - "autonomous vehicle" WITHOUT "AI" OR "perception"
    - "gaming GPU" WITHOUT "AI training"
    - "crypto mining"
    - "metaverse" WITHOUT "AI"

Validation_Logic:
  FOR each item:
    IF contains_ai_keyword(item.title OR item.summary):
      ai_relevance = TRUE
    ELIF item.company IN Company_AI_Context AND contains_ai_context(item.content):
      ai_relevance = TRUE
    ELIF matches_exclusion_pattern(item.content):
      ai_relevance = FALSE, ❌ Auto-reject
    ELSE:
      ai_relevance = LLM判断 + manual review flag

Quality_Gate:
  - AI relevance ≥95% → ✅ PASS
  - AI relevance <95% → ❌ FAIL, remove non-AI items and revalidate
  - Excluded patterns found >5% → ❌ FAIL, review search queries
```

**Report Output**:
```markdown
## Round 3: AI Relevance

- Total Items: 50
- Direct AI Keywords: 42 items (84%)
- Company + AI Context: 8 items (16%)
- Non-AI Items Rejected: 3 (semiconductor manufacturing, rare earth)
- AI Relevance: 100% (after rejection)

Rejected Items:
1. ❌ "TSMC expands 3nm production capacity" - General semiconductor, no AI context
2. ❌ "Rare earth prices surge in China" - Materials only, no tech application
3. ❌ "Intel announces new desktop CPU lineup" - Traditional computing, no AI

✅ PASS - All remaining items AI-focused
```

### Round 4: Deduplication Validation

**Hardcoded Rules**:
```yaml
Similarity_Detection:
  Title_Match:
    - Exact match → Duplicate
    - Levenshtein distance <3 → Likely duplicate
    - 80%+ word overlap → Check content similarity

  Content_Fingerprint:
    - Extract key entities (company, product, amount, date)
    - Hash fingerprint: "OpenAI|GPT-5|announcement|2025-11-20"
    - Compare fingerprints across items

  URL_Dedup:
    - Same URL → Exact duplicate
    - Same domain + similar path → Likely same story

Merge_Strategy:
  IF duplicate_detected:
    Priority_Ranking:
      1. Tier 1 source > Tier 2 source
      2. More recent timestamp
      3. More complete content (longer summary)
      4. Higher credibility score

    Action:
      - Keep highest priority item
      - Merge key details from duplicates
      - Note all sources in metadata
      - Remove duplicate items

Quality_Gate:
  - Deduplication rate ≥95% → ✅ PASS
  - Deduplication rate <95% (>5% duplicates remain) → ❌ FAIL
  - Total items after dedup <40 → ⚠️ WARNING, may need more search
```

**Report Output**:
```markdown
## Round 4: Deduplication

- Initial Items: 53
- Exact Duplicates: 2 (removed)
- Similar Stories Merged: 4 (into 2 items)
- Final Items: 47
- Deduplication Rate: 96.6%

Merged Examples:
1. "OpenAI announces GPT-5" (TechCrunch) + "GPT-5 launch details" (Bloomberg)
   → Merged into single item with both sources cited

2. "Meta AI revenue hits $10B" (Reuters) + "Meta reports AI earnings" (CNBC)
   → Kept Reuters (higher credibility), noted CNBC as secondary source

✅ PASS - <5% duplicates remaining
```

### Round 5: Completeness Validation

**Hardcoded Rules**:
```yaml
Required_Fields:
  Essential: # Missing any → reject item
    - title
    - source_url
    - source_name
    - published_date
    - summary (≥50 characters)

  Important: # Missing → lower score
    - company_name
    - category
    - key_data (amounts, metrics)

  Optional: # Missing → no penalty
    - author
    - tags
    - images

Content_Quality_Checks:
  Summary_Length:
    - <50 chars → ❌ Reject (too brief)
    - 50-150 chars → ⚠️ Marginal (acceptable but improve)
    - 150-300 chars → ✅ Good
    - >300 chars → ⚠️ Too long (should be concise)

  Key_Data_Presence:
    Financial_News:
      - MUST include: amount, currency, round type
      - Example: "$100M Series C funding"

    Product_Launch:
      - MUST include: product name, key feature, release date
      - Example: "GPT-5 with 10T parameters, launching Q2 2025"

    Company_Performance:
      - MUST include: metric, value, change percentage
      - Example: "Revenue $50B, up 25% YoY"

  Context_Completeness:
    - Why this matters (impact statement)
    - Background if needed (for complex topics)
    - Quote from official source (if available)

Scoring_Formula:
  completeness_score = (
    essential_fields * 0.4 +
    important_fields * 0.3 +
    content_quality * 0.2 +
    context_depth * 0.1
  )

Quality_Gate:
  - Average completeness ≥7.0/10 → ✅ PASS
  - Average completeness <7.0/10 → ❌ FAIL
  - Any item missing essential fields → ❌ Reject that item
  - >20% items missing important fields → ⚠️ WARNING
```

**Report Output**:
```markdown
## Round 5: Completeness

- Total Items: 47
- Complete (≥8.0/10): 38 items (81%)
- Acceptable (7.0-7.9/10): 8 items (17%)
- Incomplete (<7.0/10): 1 item (2%, rejected)
- Average Completeness: 8.1/10

Field Coverage:
- Essential fields: 100% (all items)
- Important fields: 94% (44/47 items)
- Optional fields: 62% (29/47 items)

Content Quality:
- Summary length appropriate: 45/47 items (96%)
- Key data present: 41/47 items (87%)
- Context provided: 38/47 items (81%)

Rejected Items:
1. ❌ "AI startup raises funding" - Missing amount, round type, investor details

✅ PASS - Average completeness 8.1/10 (exceeds 7.0 threshold)
```

### Round 6-10: Optional Enhanced Validation

**Round 6: Geographic Balance** (Optional)
- Ensure no single region dominates (max 60%)
- Target: 40-50% international, 35-45% domestic, 10-20% policy

**Round 7: Topic Diversity** (Optional)
- Minimum 6 major categories represented
- No single category >30%

**Round 8: Compliance Pre-Check** (Optional)
- Flag sensitive content for formatter skill
- Identify high-risk keywords early

**Round 9: Engagement Potential** (Optional)
- Score items by expected reader interest
- Identify top 5 candidates for "48小时焦点"

**Round 10: Cross-Reference Validation** (Optional)
- Verify claims across multiple sources
- Flag uncorroborated information

## Final Quality Gate

**Master Validation Checklist**:
```yaml
Mandatory_Checks: # All must pass
  - ✅ Source credibility ≥7.0/10
  - ✅ 100% items within 48h window
  - ✅ AI relevance ≥95%
  - ✅ Deduplication rate ≥95%
  - ✅ Completeness ≥7.0/10
  - ✅ Item count 40-50 (after dedup/rejection)

Workflow_Actions:
  IF all_mandatory_pass:
    ✅ Generate validation_report.md
    ✅ Generate tech_news_[DATE]_validated.json
    ✅ Set workflow_status = "PASS"
    → Proceed to daily-tech-news-writer

  ELSE:
    ❌ Generate validation_report.md with failure details
    ❌ Set workflow_status = "FAIL"
    ❌ Log failure reasons
    → TERMINATE workflow, require manual review
```

## Output Format

### 1. Validation Report (validation_report_[DATE].md)

```markdown
# Tech News Validation Report | 2025-11-20

> **Execution Time**: 2025-11-20 15:30:00 CST
> **Input File**: tech_news_20251120_raw.md
> **Initial Items**: 53
> **Final Items**: 46
> **Overall Status**: ✅ PASS

---

## Executive Summary

- Source Credibility: 8.2/10 ✅
- Time Accuracy: 100% within 48h ✅
- AI Relevance: 100% ✅
- Deduplication: 96.6% ✅
- Completeness: 8.1/10 ✅
- **Final Verdict: READY FOR WRITING PHASE**

---

## Round 1: Source Credibility
[Detailed metrics as shown above]

## Round 2: Time Accuracy
[Detailed metrics as shown above]

## Round 3: AI Relevance
[Detailed metrics as shown above]

## Round 4: Deduplication
[Detailed metrics as shown above]

## Round 5: Completeness
[Detailed metrics as shown above]

---

## Rejected Items Summary

Total Rejected: 7 items (13.2%)

### By Reason:
- Non-AI content: 3 items (5.7%)
- Low credibility source: 2 items (3.8%)
- Duplicate: 1 item (1.9%)
- Incomplete data: 1 item (1.9%)

### Details:
1. ❌ "TSMC expands 3nm production" - Non-AI, general semiconductor
2. ❌ "Rare earth prices surge" - Materials only, no tech application
[... full list ...]

---

## Quality Metrics Dashboard

```
┌─────────────────────────┬─────────┬───────────┬────────┐
│ Metric                  │ Score   │ Threshold │ Status │
├─────────────────────────┼─────────┼───────────┼────────┤
│ Source Credibility      │ 8.2/10  │ ≥7.0      │ ✅ PASS│
│ Time Compliance         │ 100%    │ 100%      │ ✅ PASS│
│ AI Relevance            │ 100%    │ ≥95%      │ ✅ PASS│
│ Deduplication Rate      │ 96.6%   │ ≥95%      │ ✅ PASS│
│ Completeness            │ 8.1/10  │ ≥7.0      │ ✅ PASS│
│ Final Item Count        │ 46      │ 40-50     │ ✅ PASS│
└─────────────────────────┴─────────┴───────────┴────────┘
```

---

## Workflow Integration

- Validation Status: ✅ PASS
- Output File: tech_news_20251120_validated.json
- Next Phase: daily-tech-news-writer
- Estimated Writing Time: 5-8 minutes

---

**Generated by**: daily-tech-news-validator v4.0
**Validation Engine**: Hardcoded rules + LLM judgment
**Report Format**: v4.0-standard
```

### 2. Validated Data (tech_news_[DATE]_validated.json)

```json
{
  "metadata": {
    "validation_date": "2025-11-20T15:30:00+08:00",
    "validator_version": "4.0.0",
    "input_file": "tech_news_20251120_raw.md",
    "workflow_status": "PASS",
    "execution_time_seconds": 180
  },
  "quality_metrics": {
    "source_credibility": {
      "average": 8.2,
      "tier1_count": 35,
      "tier2_count": 11,
      "threshold": 7.0,
      "status": "PASS"
    },
    "time_accuracy": {
      "layer0_count": 38,
      "layer1_count": 8,
      "layer2_count": 0,
      "average_age_hours": 14.2,
      "compliance_rate": 1.0,
      "status": "PASS"
    },
    "ai_relevance": {
      "ai_focused_count": 46,
      "non_ai_rejected": 3,
      "relevance_rate": 1.0,
      "status": "PASS"
    },
    "deduplication": {
      "initial_count": 53,
      "final_count": 46,
      "duplicate_rate": 0.132,
      "dedup_rate": 0.966,
      "status": "PASS"
    },
    "completeness": {
      "average": 8.1,
      "complete_count": 38,
      "acceptable_count": 8,
      "incomplete_rejected": 1,
      "status": "PASS"
    }
  },
  "validated_items": [
    {
      "id": "item_001",
      "title": "OpenAI announces GPT-5 with 10 trillion parameters",
      "source": {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/2025/11/20/openai-gpt5-announcement",
        "credibility": 10,
        "tier": 1
      },
      "timestamp": {
        "published": "2025-11-20T08:00:00Z",
        "parsed_method": "ISO8601",
        "age_hours": 7.5,
        "layer": 0
      },
      "ai_validation": {
        "primary_keywords": ["GPT-5", "large language model", "AI model"],
        "company": "OpenAI",
        "relevance_score": 10
      },
      "completeness": {
        "score": 9.2,
        "has_essential_fields": true,
        "has_key_data": true,
        "summary_length": 245
      },
      "summary": "OpenAI announced GPT-5, featuring 10 trillion parameters and multimodal capabilities including advanced reasoning, real-time vision, and voice interaction. The model will be available via API in Q2 2025, with pricing starting at $0.03 per 1K tokens. CEO Sam Altman stated this represents a major leap toward AGI capabilities.",
      "key_data": {
        "product": "GPT-5",
        "parameters": "10 trillion",
        "release": "Q2 2025",
        "pricing": "$0.03/1K tokens"
      },
      "category": "AI Models",
      "compliance_flags": []
    }
    // ... 45 more validated items
  ],
  "rejected_items": [
    {
      "original_title": "TSMC expands 3nm production capacity",
      "rejection_reason": "Non-AI content - general semiconductor manufacturing",
      "rejection_round": 3,
      "details": "No AI context found in title or summary despite multiple searches"
    }
    // ... 6 more rejected items
  ]
}
```

## Integration with Workflow

### Input Requirements
- **File**: `tech_news_[YYYYMMDD]_raw.md` from daily-tech-news-search
- **Format**: Markdown with structured sections
- **Minimum Items**: 45 items (before validation)

### Output Guarantees
- **Report**: `validation_report_[YYYYMMDD].md` ALWAYS generated (even on failure)
- **Data**: `tech_news_[YYYYMMDD]_validated.json` only if validation passes
- **Status**: Explicit PASS/FAIL in both files

### Workflow Integration Points
```yaml
After_Validation:
  IF validation_status == "PASS":
    - Load validated.json
    - Pass to daily-tech-news-writer
    - Log success

  ELIF validation_status == "FAIL":
    - Display validation_report.md failure section
    - Offer retry options:
      1. Adjust search parameters and re-run search
      2. Lower validation thresholds (with warnings)
      3. Manual review and override
    - TERMINATE workflow until resolved
```

## Reference Documentation

- **[validation_rules.md](references/validation_rules.md)** - Complete hardcoded rule specifications
- **[report_template.md](references/report_template.md)** - Validation report structure and format
- **[quality_gates.md](references/quality_gates.md)** - Detailed quality gate thresholds and logic
- **[error_handling.md](references/error_handling.md)** - Validation failure scenarios and recovery strategies

## Best Practices

### For Developers

1. **Never Skip Validation**: Even if search results "look good", run full validation
2. **Check Report Existence**: Workflow should verify validation_report.md exists before proceeding
3. **Respect Quality Gates**: Do not lower thresholds without documenting justification
4. **Preserve Metadata**: validated.json contains critical traceability information
5. **Handle Failures Gracefully**: Validation failure is NOT a bug, it's a feature

### For Content Editors

1. **Review Rejected Items**: Sometimes valuable content is rejected for fixable reasons
2. **Manual Override Protocol**: Document all manual overrides in validation_report.md
3. **Track Patterns**: If specific sources consistently fail, update search queries
4. **Validation Tuning**: Adjust thresholds based on historical data, not individual cases

## Error Scenarios

### Insufficient Items After Rejection
```yaml
Scenario: Final item count <40 after validation
Root_Cause: Too many items rejected for quality/relevance issues
Action:
  1. Review rejection reasons in validation_report.md
  3. If mostly AI relevance → refine search queries in daily-tech-news-search
  4. If mostly credibility → add more Tier 1/2 sources to search
  5. Re-run search with adjusted parameters
  6. Re-validate with updated dataset
```

### Validation Report Not Generated
```yaml
Scenario: Workflow cannot find validation_report.md
Root_Cause: Validator skill crashed or was interrupted
Action:
  1. Check validator execution logs
  2. Verify input file integrity (tech_news_raw.md)
  3. Re-run validator skill manually
  4. If persistent failure → investigate code bugs in validation logic
```

### Cross-Validation Inconsistencies
```yaml
Scenario: >20% items have timestamp inconsistencies
Root_Cause: Poor timestamp parsing or misleading content
Action:
  1. Review flagged items in Round 2 details
  2. Improve timestamp extraction logic for problematic sources
  3. Add manual time verification for flagged items
  4. Document sources with known timestamp issues
```

## Performance Expectations

```
Component                    Time        Operations
────────────────────────────────────────────────────
Round 1: Credibility         30-45s      Domain lookup, scoring
Round 2: Time Accuracy       45-60s      Timestamp parsing, cross-check
Round 3: AI Relevance        60-90s      Keyword matching, pattern detection
Round 4: Deduplication       30-45s      Fingerprinting, similarity calc
Round 5: Completeness        45-60s      Field validation, scoring
Report Generation            15-30s      Markdown formatting, JSON export
───────────────────────────────────────────────────
Total                        3-5 min     ~50 items validated
```

---

**Version**: 4.0.0
**Validation Engine**: Hardcoded rules (70%) + LLM judgment (30%)
**Quality Gates**: 5 mandatory rounds, all must pass
**Report Generation**: Always (even on failure)
**Workflow Integration**: Phase 2 of 5-phase pipeline
