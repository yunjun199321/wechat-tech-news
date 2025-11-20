# Validation Report Template

> **Standard format for validation_report_[DATE].md output**

## Complete Report Structure

```markdown
# Tech News Validation Report | [YYYY-MM-DD]

> **Execution Time**: [YYYY-MM-DD HH:MM:SS CST]
> **Input File**: tech_news_[YYYYMMDD]_raw.md
> **Initial Items**: [N]
> **Final Items**: [M]
> **Overall Status**: ✅ PASS | ❌ FAIL

---

## Executive Summary

- Source Credibility: [X.X]/10 [✅|❌]
- Time Accuracy: [X]% within 48h [✅|❌]
- AI Relevance: [X]% [✅|❌]
- Deduplication: [X.X]% [✅|❌]
- Completeness: [X.X]/10 [✅|❌]
- **Final Verdict**: [READY FOR WRITING PHASE | VALIDATION FAILED]

---

## Round 1: Source Credibility

### Summary
- Total Items: [N]
- Tier 1 Sources: [N] ([X]%)
- Tier 2 Sources: [N] ([X]%)
- Unverified Sources: [N] ([X]%)
- Blacklisted Sources: [N] ([X]%)
- Average Credibility: [X.X]/10

### Breakdown by Source
| Source | Items | Tier | Avg Credibility |
|--------|-------|------|-----------------|
| TechCrunch | 8 | 1 | 10.0 |
| Bloomberg | 6 | 1 | 9.5 |
| [... more sources ...] |

### Quality Gate
[✅ PASS | ❌ FAIL] - [Meets|Does not meet] minimum threshold (≥7.0/10)

[If FAIL:]
**Failure Reason**: Average credibility [X.X]/10 below minimum 7.0/10
**Recommendation**:
- Remove [N] low-credibility items
- Re-run search with better sources
- Manual review of [specific items]

---

## Round 2: Time Accuracy

### Summary
- Total Items: [N]
- Layer 0 (0-24h): [N] items ([X]%)
- Layer 1 (24-48h): [N] items ([X]%)
- Layer 2 (>48h): [N] items ([X]%)
- Average Age: [X.X] hours

### Time Distribution Chart
```
0-6h   : ████████████████████ 20 items (40%)
6-12h  : ██████████████ 14 items (28%)
12-24h : ██████ 6 items (12%)
24-36h : ████ 4 items (8%)
36-48h : ██ 2 items (4%)
>48h   : ██ 2 items (4%, flagged)
```

### Time Validation Details
- Successfully parsed timestamps: [N]/[N] ([X]%)
- Manual time estimation: [N]/[N] ([X]%)
- Cross-validation inconsistencies: [N]/[N] ([X]%, flagged)

### Inconsistency Details
[If any inconsistencies:]
| Item # | Title | Metadata Age | Content Age | Delta | Status |
|--------|-------|--------------|-------------|-------|--------|
| 23 | "OpenAI announces..." | 8h | 20h | 12h | 🚨 Flagged |

### Quality Gate
[✅ PASS | ❌ FAIL] - [All|Some] items within 48h window

[If items >48h:]
**Items Exceeding 48h**:
1. [Item #X] - "[Title]" - Age: [X]h - Importance: [X]/10 - [APPROVED|REJECTED]
   Reason: [High-impact announcement | Manual approval | etc.]

---

## Round 3: AI Relevance

### Summary
- Total Items: [N]
- Direct AI Keywords: [N] items ([X]%)
- Company + AI Context: [N] items ([X]%)
- Non-AI Items Rejected: [N]
- AI Relevance: [X]% (after rejection)

### Keyword Match Statistics
| Keyword Category | Matches |
|------------------|---------|
| Core AI Terms (GPT, LLM, AI model) | 25 |
| Model Names (ChatGPT, Claude) | 12 |
| Technical Terms (transformer, RLHF) | 8 |
| AI Infrastructure (AI chip, H100) | 10 |
| Company + Context | 5 |

### Rejected Items
[List all non-AI rejected items:]
1. ❌ "[Title]" - [Source] - [Age]h
   **Rejection Reason**: [Detailed explanation]
   **Matched Pattern**: [Exclusion pattern that triggered rejection]
   **Decision**: Final rejection after [keyword search | context analysis]

2. ❌ "[Title]" - [Source] - [Age]h
   [... same structure ...]

### Quality Gate
[✅ PASS | ❌ FAIL] - AI relevance [X]% [≥|<] 95% threshold

---

## Round 4: Deduplication

### Summary
- Initial Items: [N]
- Exact Duplicates: [N] (removed)
- Similar Stories Merged: [N] (into [M] items)
- Final Items: [N]
- Deduplication Rate: [X.X]%

### Deduplication Details

#### Exact Duplicates Removed
1. "[Title]" ([Source 1]) = "[Title]" ([Source 2])
   - Kept: [Source 1] (Tier [X], more recent)
   - Removed: [Source 2]

#### Merged Items
1. **Primary**: "[Title]" - [Source 1] (Tier [X], [age]h)
   **Merged with**: "[Similar Title]" - [Source 2] (Tier [X], [age]h)
   **Merge Reason**: [Same company, same event, similar timestamp]
   **Combined Summary**: [Enhanced summary with details from both sources]
   **Sources Cited**: [Source 1], [Source 2]

2. [... more merged items ...]

### URL Deduplication
- Duplicate URLs detected: [N]
- Normalized and merged: [N]

### Quality Gate
[✅ PASS | ❌ FAIL] - Deduplication rate [X.X]% [≥|<] 95% threshold

---

## Round 5: Completeness

### Summary
- Total Items: [N]
- Complete (≥8.0/10): [N] items ([X]%)
- Acceptable (7.0-7.9/10): [N] items ([X]%)
- Incomplete (<7.0/10): [N] items ([X]%, rejected)
- Average Completeness: [X.X]/10

### Field Coverage
| Field Category | Coverage |
|----------------|----------|
| Essential fields (title, source, date, summary) | [N]/[N] (100%) |
| Important fields (company, category, key_data) | [N]/[N] ([X]%) |
| Optional fields (author, tags, images) | [N]/[N] ([X]%) |

### Content Quality Analysis
- Summary length appropriate: [N]/[N] items ([X]%)
- Key data present: [N]/[N] items ([X]%)
- Impact statement provided: [N]/[N] items ([X]%)
- Quotes included: [N]/[N] items ([X]%)

### Category-Specific Completeness
| Category | Count | Avg Score | Missing Data |
|----------|-------|-----------|--------------|
| Funding | 12 | 8.5/10 | 2 missing round type |
| Product Launch | 15 | 8.2/10 | 3 missing release date |
| Financial Results | 8 | 7.9/10 | 1 missing YoY change |
| Partnership | 6 | 8.0/10 | None |
| Research | 4 | 7.5/10 | 2 missing key findings |

### Rejected Items
[If any rejected for incompleteness:]
1. ❌ "[Title]" - [Source] - Score: [X.X]/10
   **Missing**: [Essential field name]
   **Impact**: Cannot proceed without this information
   **Recommendation**: [Contact source | Search for alternate coverage | Skip item]

### Quality Gate
[✅ PASS | ❌ FAIL] - Average completeness [X.X]/10 [≥|<] 7.0/10 threshold

---

## Rejected Items Summary

Total Rejected: [N] items ([X.X]%)

### By Rejection Reason
| Reason | Count | Percentage |
|--------|-------|------------|
| Non-AI content | [N] | [X]% |
| Low credibility source | [N] | [X]% |
| Time >48h (unapproved) | [N] | [X]% |
| Duplicate | [N] | [X]% |
| Incomplete data | [N] | [X]% |
| Blacklisted source | [N] | [X]% |

### Complete Rejection List
[Numbered list of all rejected items with full details:]

1. ❌ "[Full Title]" - [Source Name] - [Credibility X/10] - [Age Xh]
   - **Rejection Round**: [N]
   - **Rejection Reason**: [Detailed explanation]
   - **Key Issue**: [Specific problem that caused rejection]
   - **Recommendation**: [What could be done if this item is important]

[Repeat for all rejected items]

---

## Quality Metrics Dashboard

```
┌──────────────────────────┬──────────┬──────────────┬────────────┐
│ Metric                   │ Score    │ Threshold    │ Status     │
├──────────────────────────┼──────────┼──────────────┼────────────┤
│ Source Credibility       │ [X.X]/10 │ ≥7.0         │ [✅|❌] [STATUS] │
│ Time Compliance          │ [X]%     │ 100%         │ [✅|❌] [STATUS] │
│ AI Relevance             │ [X]%     │ ≥95%         │ [✅|❌] [STATUS] │
│ Deduplication Rate       │ [X.X]%   │ ≥95%         │ [✅|❌] [STATUS] │
│ Completeness             │ [X.X]/10 │ ≥7.0         │ [✅|❌] [STATUS] │
│ Final Item Count         │ [N]      │ 40-50        │ [✅|❌] [STATUS] │
├──────────────────────────┼──────────┼──────────────┼────────────┤
│ Composite Quality Score  │ [X.X]/10 │ ≥7.5         │ [✅|❌] [STATUS] │
│ Quality Grade            │ [Grade]  │ ≥B           │ [✅|❌] [STATUS] │
└──────────────────────────┴──────────┴──────────────┴────────────┘
```

### Additional Metrics (Informational)
- Tier 1 Source Rate: [X]% (target: ≥70%)
- Layer 0 (0-24h) Rate: [X]% (target: ≥75%)
- Average Article Age: [X.X] hours (target: <18h)
- Manual Review Flags: [N] items (target: <5%)

---

## Optional Rounds (If Executed)

### Round 6: Geographic Balance
[If executed]
- International: [N] items ([X]%)
- Domestic (China): [N] items ([X]%)
- Policy/Global: [N] items ([X]%)
- Balance Status: [✅ Balanced | ⚠️ Skewed toward [region]]

### Round 7: Topic Diversity
[If executed]
| Category | Count | Percentage |
|----------|-------|------------|
| AI Models | [N] | [X]% |
| Funding | [N] | [X]% |
| Product Launch | [N] | [X]% |
| Financial Results | [N] | [X]% |
| Partnership | [N] | [X]% |
| Research | [N] | [X]% |
| Policy/Regulation | [N] | [X]% |

Diversity Status: [✅ Well-balanced | ⚠️ Over-concentrated in [category]]

### Round 8: Compliance Pre-Check
[If executed]
Sensitive content flagged: [N] items ([X]%)
- 🔴 High Risk: [N] items (military, US-China conflict)
- 🟡 Medium Risk: [N] items (financial, policy)
- 🟢 Low Risk: [N] items (normal reporting)

All flagged items forwarded to formatter skill for neutralization.

### Round 9: Engagement Potential
[If executed]
Top 5 candidates for "本周焦点" (Focus Highlights):
1. "[Title]" - Engagement Score: [X]/10 - Reason: [Impact|Novelty|Cross-domain]
2. [... more items ...]

### Round 10: Cross-Reference Validation
[If executed]
- Items cross-referenced: [N]/[N] ([X]%)
- Corroborated by multiple sources: [N] items
- Uncorroborated claims flagged: [N] items
- Contradictory information detected: [N] items (manual review required)

---

## Workflow Integration

### Validation Status
[✅ PASS | ❌ FAIL]

### Output Files Generated
- ✅ validation_report_[YYYYMMDD].md (this file)
- [✅|❌] tech_news_[YYYYMMDD]_validated.json

### Next Phase
[IF PASS:]
- ✅ Proceed to: daily-tech-news-writer
- Input: tech_news_[YYYYMMDD]_validated.json
- Expected items: [N] validated, publication-ready items
- Estimated time: 5-8 minutes

[IF FAIL:]
- ❌ Workflow TERMINATED
- Reason: [Specific failure reason(s)]
- Recommended Actions:
  1. [Specific action based on failure type]
  2. [Alternative approach]
  3. [Manual review steps]
- Manual Intervention Required: [YES|NO]
- After fixes, re-run: daily-tech-news-validator skill [input-file]

### Execution Metadata
- Validator Version: 4.0.0
- Execution Time: [X] minutes [Y] seconds
- Validation Engine: Hardcoded rules ([X]%) + LLM judgment ([Y]%)
- Total Rule Checks: [N] checks performed
- Errors Encountered: [N] (see error log below if >0)

[If errors occurred:]
### Error Log
1. [ERROR TYPE]: [Description] - Status: [Recovered|Failed]
   [Details and resolution]

---

## Appendix: Validation Configuration

### Thresholds Used
- Source credibility minimum: 7.0/10
- Time window: 48 hours strict
- AI relevance minimum: 95%
- Deduplication minimum: 95%
- Completeness minimum: 7.0/10
- Item count range: 40-50

### Domain Whitelists Applied
- Tier 1: [N] domains
- Tier 2: [N] domains
- Blacklist: [N] patterns

### Keyword Libraries Used
- Primary AI keywords: [N] patterns
- Secondary AI keywords: [N] patterns
- Exclusion patterns: [N] patterns
- Company-specific rules: [N] companies

### Validation Rules Version
- Rules file: validation_rules.md v4.0.0
- Last updated: [YYYY-MM-DD]
- Custom overrides: [None | See list below]

---

**Report Generated**: [YYYY-MM-DD HH:MM:SS CST]
**Generator**: daily-tech-news-validator v4.0.0
**Report Format**: v4.0-standard
**Validation Engine**: Hybrid (hardcoded rules + LLM-assisted judgment)
```

## Report Generation Logic

```python
def generate_validation_report(
    input_file,
    initial_items,
    validated_items,
    rejected_items,
    metrics,
    execution_time,
    status
):
    """
    Generates standardized validation report

    Args:
        input_file: Path to tech_news_[DATE]_raw.md
        initial_items: List of items before validation
        validated_items: List of items after validation
        rejected_items: List of rejected items with reasons
        metrics: Dict of all quality metrics
        execution_time: Float, seconds taken
        status: "PASS" or "FAIL"

    Returns:
        report_path: Path to generated validation_report_[DATE].md
    """
    date = extract_date_from_filename(input_file)
    report_path = f"validation_report_{date}.md"

    # Fill template with actual data
    report = REPORT_TEMPLATE.format(
        date=format_date(date),
        execution_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S CST"),
        input_file=input_file,
        initial_count=len(initial_items),
        final_count=len(validated_items),
        status=status,
        **metrics,  # Unpack all metric values
        rejected_summary=format_rejected_summary(rejected_items),
        quality_dashboard=generate_dashboard(metrics),
        # ... more formatting ...
    )

    # Write to file
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return report_path

def format_rejected_summary(rejected_items):
    """Format rejected items section"""
    summary = []

    # Group by reason
    by_reason = defaultdict(list)
    for item in rejected_items:
        by_reason[item['rejection_reason']].append(item)

    # Create table
    table = "| Reason | Count | Percentage |\n"
    table += "|--------|-------|------------|\n"
    total = len(rejected_items)

    for reason, items in by_reason.items():
        count = len(items)
        pct = (count / total * 100) if total > 0 else 0
        table += f"| {reason} | {count} | {pct:.1f}% |\n"

    # Detailed list
    details = "\n\n### Complete Rejection List\n\n"
    for i, item in enumerate(rejected_items, 1):
        details += f"{i}. ❌ \"{item['title']}\" - {item['source']}\n"
        details += f"   - **Rejection Round**: {item['rejection_round']}\n"
        details += f"   - **Rejection Reason**: {item['rejection_reason']}\n"
        details += f"   - **Key Issue**: {item['key_issue']}\n\n"

    return table + details
```

## Usage in Workflow

```python
# After validation completes
report_path = generate_validation_report(
    input_file=input_file,
    initial_items=initial_items,
    validated_items=validated_items,
    rejected_items=rejected_items,
    metrics=all_metrics,
    execution_time=time.time() - start_time,
    status="PASS" if all_gates_passed else "FAIL"
)

# Workflow checks for report existence
assert os.path.exists(report_path), "Validation report not generated!"

# Workflow reads status from report
with open(report_path) as f:
    content = f.read()
    status = extract_status(content)  # Parse "Overall Status: ✅ PASS"

if status == "PASS":
    proceed_to_next_phase()
else:
    terminate_workflow_with_message(extract_failure_reason(content))
```

---

**Template Version**: 4.0.0
**Compatibility**: daily-tech-news-validator v4.0.0+
**Format**: Markdown with embedded tables and code blocks
**Encoding**: UTF-8
