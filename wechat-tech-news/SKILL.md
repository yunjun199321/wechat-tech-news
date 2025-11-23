---
name: wechat-tech-news
description: Complete 5-phase automated workflow for daily tech news - collection, validation, writing, formatting, and export. Orchestrates all skills with quality gates between phases. One-command solution from search to publication-ready content with Word export.
---

# Tech News Workflow

> **🔄 Version 4.0**: 5-phase pipeline with dedicated validation and formatting phases

## When to Use This Skill

Use this skill when you need:
- Complete daily tech news workflow (collection → validation → writing → formatting → export)
- Publication-ready WeChat Official Account content
- Hardcoded quality gates between all phases
- Systematic validation and optimization
- Multi-format output (Markdown + Word document)
- One-command automation with minimal manual intervention

## Quick Start

```bash
使用 wechat-tech-news skill
```

**Execution Time**: 30-45 minutes (average: 35 min)
**Output Files**:
- `tech_news_[DATE]_raw.md` - Raw collection (45-55 items)
- `validation_report_[DATE].md` - Validation details
- `tech_news_[DATE]_validated.json` - Validated data (40-45 items)
- `tech_news_[DATE]_wechat_draft.md` - Content draft (unoptimized)
- `format_report_[DATE].md` - Formatting details
- `tech_news_[DATE]_wechat_final.md` - Final article (publication-ready)
- `tech_news_[DATE]_wechat_final.docx` - Word document (optional)
- `workflow_[DATE].json` - Execution metadata

## Workflow Architecture (v4.0)

```
┌──────────────────────────────────────────────────────────────────┐
│                     wechat-tech-news v4.0                        │
│                                                                  │
│  Phase 1      Phase 2       Phase 3      Phase 4      Phase 5  │
│  ─────────→  ─────────→   ─────────→   ─────────→   ────────  │
│  Collection  Validation    Writing      Formatting   Export     │
│  15-20 min   3-5 min       5-8 min      4-6 min      1-2 min   │
│                                                                  │
│  Skills:                                                         │
│  1. daily-tech-news-search    (Pure collection)                │
│  2. daily-tech-news-validator (Hardcoded validation)           │
│  3. daily-tech-news-writer    (Pure writing)                   │
│  4. daily-tech-news-formatter (Multi-round optimization)       │
│  5. document-exporter         (Word generation)                │
│                                                                  │
│  Quality Gates: ✓ After each phase (mandatory)                 │
│  Reports: validation_report.md + format_report.md              │
│  Error Recovery: ✓ Phase-specific retry strategies            │
│  Metadata: Complete execution tracking in workflow_[DATE].json │
└──────────────────────────────────────────────────────────────────┘
```

## Five-Phase Pipeline

### Phase 1: Collection (15-20 minutes)

**Skill**: `daily-tech-news-search`

**Responsibilities**:
- Execute AI-focused web searches via `/sc:research`
- Collect 45-55 raw news items
- Prioritize 24h content, supplement with 48h if needed
- Basic AI relevance filtering (keyword-based)
- Structure data in markdown format

**Output**:
- `tech_news_[DATE]_raw.md` (45-55 unvalidated items)

**Quality Gate 1**:
```yaml
Checks:
  - Item count ≥45 → ✅ Pass to Phase 2
  - Item count <45 → ❌ Retry with adjusted parameters

Retry_Strategy:
  - Extend search to tier-2 companies
  - Include smaller funding rounds (>$50M)
  - Search additional Chinese sources
  - Max retries: 2
```

---

### Phase 2: Validation (3-5 minutes)

**Skill**: `daily-tech-news-validator`

**Responsibilities**:
- Round 1: Source credibility check (domain whitelist/blacklist)
- Round 2: Time accuracy validation (strict 48h, double-verification)
- Round 3: AI relevance validation (keyword matching + exclusion patterns)
- Round 4: Deduplication (fingerprinting + merge strategy)
- Round 5: Completeness check (required fields + content quality)
- Generate `validation_report.md` (always, even on failure)

**Output**:
- `validation_report_[DATE].md` (complete validation details)
- `tech_news_[DATE]_validated.json` (40-45 validated items)

**Quality Gate 2**:
```yaml
Mandatory_Checks:
  - Source credibility ≥7.0/10 → Required
  - Time compliance 100% within 48h → Required
  - AI relevance ≥95% → Required
  - Deduplication rate ≥95% → Required
  - Completeness ≥7.0/10 → Required
  - Final item count 40-45 → Required

Action_On_Fail:
  IF validation_status == "PASS":
    → Proceed to Phase 3
  ELSE:
    → Display validation_report.md failure section
    → Offer retry options
    → TERMINATE workflow until resolved
```

---

### Phase 3: Writing (5-8 minutes)

**Skill**: `daily-tech-news-writer`

**Responsibilities**:
- Load `tech_news_[DATE]_validated.json`
- Select 5 focus highlights (scoring algorithm)
- Categorize by geography (国内/国外) or theme
- Write engaging, accessible summaries
- Generate article structure with proper sections
- Create opening hook (引导语)
- Add ending sections from template

**Output**:
- `tech_news_[DATE]_wechat_draft.md` (6500-7500 words, unoptimized)

**Quality Gate 3**:
```yaml
Checks:
  - Article structure complete → Required
  - Focus highlights = 5 items → Required
  - Word count 6000-8000 → Recommended (warn if outside)
  - All required sections present → Required

Action_On_Fail:
  IF structure_incomplete:
    → Regenerate missing sections
  IF focus_highlights != 5:
    → Re-run selection algorithm
  ELSE:
    → Proceed to Phase 4
```

---

### Phase 4: Formatting (4-6 minutes)

**Skill**: `daily-tech-news-formatter`

**Responsibilities**:
- Round 1: Compliance optimization (100+ keyword substitutions)
- Round 2: Punctuation normalization (English → Chinese in Chinese context)
- Round 3: Grammar and semantic refinement
- Round 4: Title and headline enhancement
- Round 5: Final quality assurance
- Generate `format_report.md` (always, even on failure)

**Output**:
- `format_report_[DATE].md` (complete optimization details)
- `tech_news_[DATE]_wechat_final.md` (6000-8000 words, publication-ready)

**Quality Gate 4**:
```yaml
Mandatory_Checks:
  - Compliance score ≥85/100 → Required
  - Punctuation 100% Chinese in Chinese text → Required
  - Grammar score ≥85/100 → Required
  - Final quality score ≥85/100 → Required

Action_On_Fail:
  IF format_status == "PASS":
    → Proceed to Phase 5
  ELIF format_status == "WARNING":
    → Proceed with user notification (quality 85-89)
  ELSE:
    → Display format_report.md failure section
    → Require manual review
```

---

### Phase 5: Export (1-2 minutes) - Optional

**Skill**: `document-exporter` (external or built-in docx library)

**Responsibilities**:
- Convert `tech_news_[DATE]_wechat_final.md` to Word format
- Apply standard formatting (fonts, spacing, styles)
- Preserve emoji and special characters
- Generate table of contents
- Add metadata (date, version, author)

**Output**:
- `tech_news_[DATE]_wechat_final.docx`

**Quality Gate 5**:
```yaml
Checks:
  - Word document generated → Required
  - Content matches markdown → Required
  - Formatting preserved → Required

Action_On_Fail:
  IF export_failed:
    → Log error but DO NOT terminate workflow
    → User can still use markdown version
```

---

## Execution Flow

```python
def execute_workflow(date=None):
    """
    Execute complete 5-phase workflow
    """
    # Initialize
    if date is None:
        date = calculate_china_date()

    metadata = {
        'date': date,
        'start_time': datetime.now(),
        'version': '4.0.0',
        'phases': []
    }

    # Phase 1: Collection
    print("Phase 1/5: Collection (15-20 min)")
    collection_result = execute_skill(
        'daily-tech-news-search',
        date=date
    )

    if collection_result['item_count'] < 45:
        # Retry with adjusted parameters
        collection_result = retry_collection(date)

    if collection_result['status'] != 'SUCCESS':
        return terminate_workflow('Phase 1 failed', metadata)

    metadata['phases'].append({
        'name': 'Collection',
        'status': 'SUCCESS',
        'output': collection_result['output_file'],
        'duration': collection_result['duration']
    })

    # Phase 2: Validation
    print("Phase 2/5: Validation (3-5 min)")
    validation_result = execute_skill(
        'daily-tech-news-validator',
        input_file=collection_result['output_file']
    )

    # Check validation report
    validation_status = parse_validation_status(
        validation_result['report_file']
    )

    if validation_status != 'PASS':
        return terminate_workflow(
            'Phase 2 failed - validation quality gate not met',
            metadata,
            details=validation_result['failure_reason']
        )

    metadata['phases'].append({
        'name': 'Validation',
        'status': 'SUCCESS',
        'output': validation_result['validated_json'],
        'report': validation_result['report_file'],
        'duration': validation_result['duration'],
        'metrics': validation_result['quality_metrics']
    })

    # Phase 3: Writing
    print("Phase 3/5: Writing (5-8 min)")
    writing_result = execute_skill(
        'daily-tech-news-writer',
        input_file=validation_result['validated_json']
    )

    if writing_result['status'] != 'SUCCESS':
        return terminate_workflow('Phase 3 failed', metadata)

    metadata['phases'].append({
        'name': 'Writing',
        'status': 'SUCCESS',
        'output': writing_result['draft_file'],
        'duration': writing_result['duration'],
        'word_count': writing_result['word_count']
    })

    # Phase 4: Formatting
    print("Phase 4/5: Formatting (4-6 min)")
    formatting_result = execute_skill(
        'daily-tech-news-formatter',
        input_file=writing_result['draft_file']
    )

    # Check format report
    format_status = parse_format_status(
        formatting_result['report_file']
    )

    if format_status == 'FAIL':
        return terminate_workflow(
            'Phase 4 failed - formatting quality gate not met',
            metadata,
            details=formatting_result['failure_reason']
        )
    elif format_status == 'WARNING':
        print("⚠️ Warning: Quality score 85-89, proceeding with caution")

    metadata['phases'].append({
        'name': 'Formatting',
        'status': 'SUCCESS' if format_status == 'PASS' else 'WARNING',
        'output': formatting_result['final_file'],
        'report': formatting_result['report_file'],
        'duration': formatting_result['duration'],
        'quality_score': formatting_result['quality_score']
    })

    # Phase 5: Export (Optional)
    print("Phase 5/5: Export (1-2 min)")
    try:
        export_result = execute_skill(
            'document-exporter',
            input_file=formatting_result['final_file'],
            output_format='docx'
        )
        metadata['phases'].append({
            'name': 'Export',
            'status': 'SUCCESS',
            'output': export_result['docx_file'],
            'duration': export_result['duration']
        })
    except Exception as e:
        print(f"⚠️ Export failed: {e}")
        print("   Markdown version still available")
        metadata['phases'].append({
            'name': 'Export',
            'status': 'FAILED',
            'error': str(e)
        })

    # Complete workflow
    metadata['end_time'] = datetime.now()
    metadata['total_duration'] = (
        metadata['end_time'] - metadata['start_time']
    ).total_seconds()
    metadata['status'] = 'SUCCESS'

    # Save metadata
    save_workflow_metadata(metadata, date)

    # Summary
    print("\n" + "="*60)
    print("✅ Workflow Complete!")
    print("="*60)
    print(f"Date: {date}")
    print(f"Total Duration: {metadata['total_duration']//60:.0f} minutes")
    print(f"\nOutput Files:")
    print(f"  - Raw: {collection_result['output_file']}")
    print(f"  - Validated: {validation_result['validated_json']}")
    print(f"  - Final MD: {formatting_result['final_file']}")
    if 'docx_file' in export_result:
        print(f"  - Final DOCX: {export_result['docx_file']}")
    print(f"\nReports:")
    print(f"  - Validation: {validation_result['report_file']}")
    print(f"  - Formatting: {formatting_result['report_file']}")
    print(f"  - Workflow: workflow_{date}.json")
    print(f"\nRecommendation: Ready for publication ✅")

    return metadata
```

## Error Recovery Strategies

### Phase 1 Failure: Insufficient Items

```yaml
Scenario: <45 items collected
Actions:
  1. Retry with extended search scope
     - Add tier-2 companies
     - Include smaller funding (>$50M)
     - Search more Chinese sources
  2. If retry succeeds → Continue
  3. If retry fails → Manual review required
```

### Phase 2 Failure: Validation Quality Gate

```yaml
Scenario: Validation status = FAIL
Actions:
  1. Display validation_report.md
  2. Identify failure reason
  3. Offer options:
     a. Re-run Phase 1 with adjusted parameters
     b. Lower validation thresholds (with warnings)
     c. Manual review and override
  4. User decision required
```

### Phase 3 Failure: Writing Error

```yaml
Scenario: Article structure incomplete
Actions:
  1. Identify missing sections
  2. Regenerate missing parts
  3. If persistent → Check validated.json integrity
  4. Retry Phase 3
```

### Phase 4 Failure: Formatting Quality Gate

```yaml
Scenario: Format status = FAIL (quality <85)
Actions:
  1. Display format_report.md
  2. Identify low-scoring areas
  3. Re-run specific optimization rounds
  4. If compliance issues → Must resolve
  5. If grammar/style only → Manual review option
```

### Phase 5 Failure: Export Error

```yaml
Scenario: Word document generation failed
Actions:
  1. Log error (non-critical)
  2. Provide markdown version
  3. Workflow continues to completion
  4. User can manually export if needed
```

## Workflow Metadata (workflow_[DATE].json)

```json
{
  "date": "2025-11-20",
  "version": "4.0.0",
  "status": "SUCCESS",
  "start_time": "2025-11-20T14:00:00+08:00",
  "end_time": "2025-11-20T14:35:23+08:00",
  "total_duration_seconds": 2123,
  "phases": [
    {
      "name": "Collection",
      "status": "SUCCESS",
      "output": "tech_news_20251120_raw.md",
      "duration_seconds": 1087,
      "item_count": 52,
      "retry_count": 0
    },
    {
      "name": "Validation",
      "status": "SUCCESS",
      "output": "tech_news_20251120_validated.json",
      "report": "validation_report_20251120.md",
      "duration_seconds": 235,
      "metrics": {
        "initial_items": 52,
        "validated_items": 46,
        "rejected_items": 6,
        "source_credibility": 8.2,
        "time_compliance": 1.0,
        "ai_relevance": 1.0,
        "deduplication_rate": 0.966,
        "completeness": 8.1,
        "composite_quality": 8.5
      }
    },
    {
      "name": "Writing",
      "status": "SUCCESS",
      "output": "tech_news_20251120_wechat_draft.md",
      "duration_seconds": 387,
      "word_count": 7234,
      "focus_highlights_count": 5
    },
    {
      "name": "Formatting",
      "status": "SUCCESS",
      "output": "tech_news_20251120_wechat_final.md",
      "report": "format_report_20251120.md",
      "duration_seconds": 312,
      "optimization_changes": 279,
      "quality_score": 94
    },
    {
      "name": "Export",
      "status": "SUCCESS",
      "output": "tech_news_20251120_wechat_final.docx",
      "duration_seconds": 102
    }
  ],
  "outputs": {
    "raw_markdown": "tech_news_20251120_raw.md",
    "validated_json": "tech_news_20251120_validated.json",
    "draft_markdown": "tech_news_20251120_wechat_draft.md",
    "final_markdown": "tech_news_20251120_wechat_final.md",
    "final_docx": "tech_news_20251120_wechat_final.docx",
    "validation_report": "validation_report_20251120.md",
    "format_report": "format_report_20251120.md",
    "workflow_metadata": "workflow_20251120.json"
  },
  "quality_summary": {
    "collection_item_count": 52,
    "validated_item_count": 46,
    "final_word_count": 7234,
    "validation_composite_score": 8.5,
    "formatting_quality_score": 94,
    "overall_recommendation": "Ready for publication"
  }
}
```

## Customization Options

```bash
# Basic usage (auto date, default settings)
使用 wechat-tech-news skill

# Custom date
使用 wechat-tech-news skill --date 2025-11-21

# Skip Phase 5 (export)
使用 wechat-tech-news skill --skip-export

# Skip Phase 1 (use existing raw file)
使用 wechat-tech-news skill --skip-collection --raw-file tech_news_20251120_raw.md

# Force validation thresholds (advanced)
使用 wechat-tech-news skill --validation-threshold 6.5

# Custom output directory
使用 wechat-tech-news skill --output-dir /path/to/output
```

## Performance Benchmarks

```
Phase                    Target       Typical      Notes
──────────────────────────────────────────────────────────
1. Collection            15-20 min    18 min       Depends on search API
2. Validation            3-5 min      4 min        Hardcoded rules fast
3. Writing               5-8 min      6 min        Content generation
4. Formatting            4-6 min      5 min        Multi-round optimization
5. Export                1-2 min      1.5 min      Document conversion
──────────────────────────────────────────────────────────
Total                    30-45 min    35 min       End-to-end automation
```

---

**Version**: 4.0.0
**Architecture**: 5-phase pipeline with quality gates
**Skills**: 5 specialized skills + 1 orchestrator
**Reports**: validation_report.md + format_report.md
**Outputs**: Markdown + Word document
**Automation**: One command, minimal manual intervention
