---
name: tech-news-workflow
description: End-to-end automated workflow for daily tech news: searches for ~50 items using daily-tech-news-search, then transforms them into WeChat-optimized articles using wechat-tech-news-writer. One-command solution from raw search to publication-ready content.
---

# Tech News Workflow

## Overview

Comprehensive automation workflow that combines deep tech news research with WeChat Official Account optimization. Executes the complete pipeline from search to publication-ready content in a single command.

## When to Use This Skill

Invoke this skill when:
- You need a complete daily tech news workflow (search → format → publish)
- Want publication-ready WeChat Official Account content
- Require automated quality control and compliance checking
- Need consistent daily tech news production
- Want to minimize manual intervention in news gathering

## Workflow Architecture

```
┌──────────────────────────────────────────────────────┐
│            tech-news-workflow                        │
│                                                      │
│  ┌────────────────┐         ┌──────────────────┐   │
│  │                │         │                  │   │
│  │  Phase 1:      │ ──────> │  Phase 2:        │   │
│  │  Research      │         │  Optimization    │   │
│  │                │         │                  │   │
│  └────────────────┘         └──────────────────┘   │
│                                                      │
│  Uses:                      Uses:                   │
│  - daily-tech-news-search   - wechat-tech-news-     │
│                               writer                │
│                                                      │
│  Output:                    Output:                 │
│  - Raw research results     - WeChat-optimized      │
│  - 50 verified items        - Compliance-checked    │
│  - Quality metrics          - Publication-ready     │
└──────────────────────────────────────────────────────┘
```

## Core Capabilities

### 1. Automated Two-Phase Pipeline

#### Phase 1: Research (daily-tech-news-search)
**Automatically executes**:
- Calculate China timezone current date
- Run deep research with `/sc:research --depth exhaustive --strategy unified`
- Search ~50 news items about major AI and tech companies
- Execute 5-round verification:
  1. Source credibility check
  2. Date and freshness validation
  3. Content deduplication
  4. Completeness and detail check
  5. Final quality gate with balance validation

**Phase 1 Output**:
```markdown
# [Date] Tech News Research Results

> **Total Items**: 50
> **Verification**: 5/5 rounds completed
> **Quality Score**: 8.2/10

## Coverage Summary
- AI Companies: 18 items
- Tech Giants: 12 items
- Chips & Hardware: 8 items
- Funding & Investment: 6 items
- Policy & Regulation: 4 items
- Other: 2 items

[Structured news items with metadata...]
```

#### Phase 2: Optimization (wechat-tech-news-writer)
**Automatically transforms**:
- Analyzes research output
- Selects optimal structure (domestic/international OR theme-based)
- Creates 本周焦点 (focus highlights) - 5 headline items
- Optimizes sensitive language for compliance
- Adds WeChat-specific elements:
  - 引导语 (opening hook)
  - 目录 (table of contents)
  - 免责声明 (disclaimers)
  - 互动引导 (engagement prompts)
  - 相关阅读 (related reading)
- Generates publication-ready markdown

**Phase 2 Output**:
```markdown
# 本周科技新闻汇总 | [Date]

> [引导语]

## 🌟 本周焦点
[5 精选新闻]

## 🇨🇳 国内科技动态
[国内新闻,合规优化]

## 🌍 国际科技动态
[国际新闻,合规优化]

## 📜 全球政策监管
[政策新闻,独立板块]

[免责声明 + 互动引导 + 相关阅读]
```

### 2. Intelligent File Management

**Automatic file organization**:

```
daily_news/
├── docs/
│   └── research/
│       ├── tech_news_20251107_raw.md      # Phase 1 output
│       └── tech_news_20251107_wechat.md   # Phase 2 output
└── metadata/
    └── workflow_20251107.json              # Execution metadata
```

**Metadata tracked**:
```json
{
  "execution_date": "2025-11-07T15:30:00+08:00",
  "china_timezone_date": "2025-11-07",
  "phase1": {
    "status": "completed",
    "duration_minutes": 18,
    "items_found": 50,
    "quality_score": 8.2,
    "verification_rounds": 5
  },
  "phase2": {
    "status": "completed",
    "duration_minutes": 5,
    "structure_selected": "domestic_international",
    "compliance_flags": 6,
    "word_count": 7245
  },
  "total_duration_minutes": 23,
  "recommendation": "Ready for publication"
}
```

### 3. Quality Control Gates

**Between-Phase Validation**:

After Phase 1, before Phase 2:
```
Quality Gate Checklist:
- [ ] Item count: 45-55 ✓
- [ ] Average quality score: ≥7.0 ✓
- [ ] Geographic balance: Within spec ✓
- [ ] Topic diversity: ≥6 categories ✓
- [ ] All verification rounds complete ✓

If any check fails:
  → Halt workflow
  → Report issue
  → Request manual review
```

**Final Output Validation**:

After Phase 2:
```
Publication Readiness Checklist:
- [ ] 本周焦点: 5 items selected ✓
- [ ] Compliance: All flags addressed ✓
- [ ] Word count: 6000-8000 words ✓
- [ ] WeChat elements: All present ✓
- [ ] Format: Valid markdown ✓

Recommendation: [Ready / Needs Review / Requires Changes]
```

### 4. Error Handling and Recovery

**Phase 1 Failure Scenarios**:

```
Scenario 1: Insufficient items found (<40)
  → Extend search scope
  → Lower completeness threshold
  → Retry verification Round 4-5

Scenario 2: Poor quality average (<6.5)
  → Review source selection
  → Enhance completeness
  → Re-run verification Round 4

Scenario 3: Research timeout
  → Save partial results
  → Report progress
  → Allow manual continuation
```

**Phase 2 Failure Scenarios**:

```
Scenario 1: Structure selection ambiguity
  → Default to domestic/international
  → Note ambiguity in metadata
  → Continue processing

Scenario 2: Compliance flag overload (>30%)
  → Increase manual review threshold
  → Generate detailed compliance report
  → Recommend editorial review

Scenario 3: Output file conflict
  → Backup existing file
  → Generate new filename with timestamp
  → Continue processing
```

### 5. Customization Options

**User can specify**:

```
使用 tech-news-workflow skill [options]

Options:
  --date DATE           Override auto-calculated China date
  --count N             Target item count (default: 50)
  --structure TYPE      Force structure: domestic_international | theme_based
  --skip-phase1         Use existing research file
  --output-dir PATH     Custom output directory
  --compliance LEVEL    Compliance strictness: strict | normal | lenient
```

**Examples**:

```
# Basic usage (auto date)
使用 tech-news-workflow skill

# Custom date
使用 tech-news-workflow skill --date 2025-11-08

# Use existing research, only run Phase 2
使用 tech-news-workflow skill --skip-phase1 --input tech_news_20251107_raw.md

# Force theme-based structure
使用 tech-news-workflow skill --structure theme_based

# Strict compliance mode
使用 tech-news-workflow skill --compliance strict
```

## Workflow Execution

### Standard Execution Flow

```
1. Initialize
   ├─ Parse user options
   ├─ Calculate China timezone date
   ├─ Create output directories
   └─ Initialize metadata

2. Phase 1: Research
   ├─ Invoke daily-tech-news-search skill
   ├─ Monitor execution progress
   ├─ Save raw results
   └─ Run quality gate validation

3. Quality Gate
   ├─ Check item count
   ├─ Verify quality scores
   ├─ Validate balance metrics
   └─ Decide: Proceed / Retry / Abort

4. Phase 2: Optimization
   ├─ Invoke wechat-tech-news-writer skill
   ├─ Pass research results
   ├─ Monitor optimization progress
   └─ Save WeChat-optimized output

5. Final Validation
   ├─ Check publication readiness
   ├─ Verify compliance handling
   ├─ Generate metadata report
   └─ Provide recommendation

6. Completion
   ├─ Save all outputs
   ├─ Generate execution summary
   ├─ Clean up temporary files
   └─ Return file paths and recommendation
```

### Detailed Step-by-Step

#### Step 1: Initialize (1 minute)

```
Action: Setup execution environment

Tasks:
1. Parse command-line options (if any)
2. Calculate current date in China timezone (UTC+8)
3. Create output file paths:
   - tech_news_[DATE]_raw.md
   - tech_news_[DATE]_wechat.md
   - workflow_[DATE].json
4. Check for existing files (prevent overwrite)
5. Initialize execution metadata
```

#### Step 2: Phase 1 - Research (15-25 minutes)

```
Action: Execute daily-tech-news-search skill

Process:
1. Invoke skill with calculated date
2. Monitor progress:
   - Search query execution
   - Verification round 1/5
   - Verification round 2/5
   - Verification round 3/5
   - Verification round 4/5
   - Verification round 5/5
3. Capture output
4. Save to tech_news_[DATE]_raw.md
5. Extract metadata:
   - Item count
   - Quality scores
   - Verification status
   - Compliance flags
```

#### Step 3: Quality Gate (2-3 minutes)

```
Action: Validate Phase 1 output

Checks:
1. Item count in range (45-55)
   ├─ Pass → Continue
   └─ Fail → Retry Phase 1 with adjusted parameters

2. Average quality score ≥7.0
   ├─ Pass → Continue
   └─ Fail → Enhanced verification, retry Round 4-5

3. Geographic balance within spec
   ├─ Pass → Continue
   └─ Fail → Adjust selection, retry Round 5

4. Topic diversity ≥6 categories
   ├─ Pass → Continue
   └─ Fail → Expand search scope

5. All verification rounds complete
   ├─ Pass → Proceed to Phase 2
   └─ Fail → Halt, report error

Decision:
  All checks pass → Phase 2
  Any check fails → Retry/Abort with reason
```

#### Step 4: Phase 2 - Optimization (5-8 minutes)

```
Action: Execute wechat-tech-news-writer skill

Process:
1. Load tech_news_[DATE]_raw.md
2. Invoke wechat-tech-news-writer skill
3. Skill automatically:
   a. Analyzes content structure
   b. Selects optimization strategy
   c. Creates 本周焦点 (5 items)
   d. Reorganizes to domestic/international OR theme-based
   e. Optimizes compliance language
   f. Adds WeChat elements
4. Capture optimized output
5. Save to tech_news_[DATE]_wechat.md
6. Extract metadata:
   - Structure selected
   - Compliance changes made
   - Word count
   - Readability score
```

#### Step 5: Final Validation (1-2 minutes)

```
Action: Verify publication readiness

Checks:
1. 本周焦点 present with 5 items ✓
2. All compliance flags addressed ✓
3. Word count 6000-8000 ✓
4. Required WeChat elements present:
   - 引导语 ✓
   - 目录 ✓
   - 免责声明 ✓
   - 互动引导 ✓
   - 相关阅读 ✓
5. Valid markdown formatting ✓

Recommendation:
  All pass → "Ready for publication"
  Minor issues → "Needs review: [specific issues]"
  Major issues → "Requires changes: [specific issues]"
```

#### Step 6: Completion (1 minute)

```
Action: Finalize and report

Tasks:
1. Save workflow metadata to workflow_[DATE].json
2. Generate execution summary
3. Clean up temporary files
4. Display results:
   - File locations
   - Quality metrics
   - Execution time
   - Recommendation

Output example:
✓ Research completed: 50 items found (quality: 8.2/10)
✓ Optimization completed: WeChat format applied
✓ Files saved:
  - Raw results: daily_news/docs/research/tech_news_20251107_raw.md
  - WeChat version: daily_news/docs/research/tech_news_20251107_wechat.md
  - Metadata: daily_news/metadata/workflow_20251107.json
✓ Total execution time: 23 minutes
✓ Recommendation: Ready for publication
```

## Integration Points

### Input
- **Automatic**: Current date (China timezone UTC+8)
- **Optional**: User-specified date, count target, structure preference

### Output Files

**File 1: tech_news_[DATE]_raw.md**
```
Purpose: Research results with full verification details
Content: 50 verified news items with metadata
Use: Archive, analysis, alternative formatting
```

**File 2: tech_news_[DATE]_wechat.md**
```
Purpose: Publication-ready WeChat article
Content: Optimized content with all WeChat elements
Use: Direct copy-paste to WeChat Official Account editor
```

**File 3: workflow_[DATE].json**
```
Purpose: Execution metadata and quality metrics
Content: Timestamps, scores, flags, recommendation
Use: Quality tracking, continuous improvement, auditing
```

### Downstream Integration

**Can be consumed by**:
- WeChat Official Account editor (direct copy-paste)
- Content management systems (import markdown)
- Analytics tools (quality metrics)
- Archive systems (long-term storage)

## Best Practices

### Do's ✅

1. **Run daily at consistent time** (e.g., 9 AM China time)
2. **Review quality gate failures** before retrying
3. **Check compliance flags** in Phase 2 output
4. **Archive both raw and optimized versions**
5. **Track quality metrics over time**
6. **Use metadata for continuous improvement**
7. **Test workflow with --skip-phase1 for Phase 2 changes**

### Don'ts ❌

1. **Don't skip quality gates** to save time
2. **Don't ignore compliance flags**
3. **Don't delete raw results** (needed for debugging)
4. **Don't run multiple times same date** (causes file conflicts)
5. **Don't override existing files** without backup
6. **Don't bypass verification rounds**

## Performance Metrics

### Typical Execution Times

```
Component                   Time Range
────────────────────────────────────────
Initialization              1-2 min
Phase 1: Research           15-25 min
  - Search execution        8-12 min
  - Verification rounds     7-13 min
Quality Gate                2-3 min
Phase 2: Optimization       5-8 min
  - Structure selection     1-2 min
  - Content reorganization  2-3 min
  - Compliance optimization 1-2 min
  - WeChat formatting       1-2 min
Final Validation            1-2 min
Completion & Cleanup        1 min
────────────────────────────────────────
Total                       25-40 min
Average                     30 min
```

### Resource Usage

```
Network:
  - Search queries: ~30
  - URLs fetched: ~80-100
  - Data transferred: ~50-100 MB

Storage:
  - Raw results: ~150-250 KB
  - WeChat version: ~180-300 KB
  - Metadata: ~5-10 KB
  - Total per day: ~350-550 KB

Memory:
  - Peak usage: ~200-300 MB
  - Average: ~150 MB
```

## Error Recovery

### Common Issues and Solutions

#### Issue 1: Phase 1 Insufficient Items

```
Error: Only 35 items found after verification

Solution:
1. Extend search scope to include tier-2 companies
2. Lower completeness threshold from 7 to 6.5
3. Expand time window from 24h to 30h
4. Include smaller funding rounds (>$50M instead of >$100M)

Automated: Yes (workflow retries with adjusted parameters)
```

#### Issue 2: Quality Gate Failure

```
Error: Geographic balance failed (US 65%, China 20%)

Solution:
1. Review Round 5 selection criteria
2. Manually add 2-3 high-quality China items
3. Remove lowest-scoring US items
4. Re-run Phase 1 Round 5 only

Automated: Partial (workflow suggests, requires manual confirmation)
```

#### Issue 3: Compliance Flag Overload

```
Error: 18 items flagged (36% > 30% threshold)

Solution:
1. Review flagged items individually
2. Ensure all have neutral alternatives
3. Consider splitting to separate compliance section
4. Add extra editorial review step

Automated: No (requires manual review)
Workflow action: Generate detailed compliance report, halt for review
```

#### Issue 4: File Conflict

```
Error: tech_news_20251107_wechat.md already exists

Solution:
1. Check if existing file is from today's run
2. If yes, append timestamp: tech_news_20251107_wechat_1530.md
3. If no, backup existing and overwrite

Automated: Yes (workflow creates timestamped filename)
```

## Quality Tracking

### Daily Quality Dashboard

Track these metrics over time:

```
Date       Items  Qual.  Geo.Bal  Topic.Div  Compl.Flags  Status
──────────────────────────────────────────────────────────────────
2025-11-07  50    8.2    PASS     PASS       6 (12%)      ✓ Ready
2025-11-06  51    8.0    PASS     PASS       8 (16%)      ✓ Ready
2025-11-05  48    7.8    FAIL     PASS       12 (25%)     ⚠ Review
2025-11-04  50    8.5    PASS     PASS       4 (8%)       ✓ Ready
──────────────────────────────────────────────────────────────────
7-day avg   49.8  8.1    75% pass 100% pass  7.5 (15%)
```

### Continuous Improvement

**Weekly Review**:
1. Analyze quality trends
2. Identify common compliance flags
3. Refine search queries for better results
4. Adjust verification thresholds if needed
5. Update source credibility database

## Examples

### Example 1: Basic Daily Run

**Command**:
```
使用 tech-news-workflow skill
```

**Execution**:
```
[15:00 CST] Initializing workflow for 2025-11-07...
[15:01 CST] Phase 1: Starting research...
[15:03 CST] - Executing search queries...
[15:10 CST] - Verification Round 1: Source credibility (73/85 passed)
[15:13 CST] - Verification Round 2: Date validation (63/73 passed)
[15:16 CST] - Verification Round 3: Deduplication (52/63 unique)
[15:20 CST] - Verification Round 4: Completeness (51/52 enhanced)
[15:23 CST] - Verification Round 5: Final selection (50 selected)
[15:24 CST] ✓ Phase 1 complete: 50 items, quality 8.2/10

[15:24 CST] Quality Gate: Checking...
[15:25 CST] ✓ All checks passed

[15:25 CST] Phase 2: Starting optimization...
[15:26 CST] - Analyzing structure... (domestic/international selected)
[15:27 CST] - Creating 本周焦点... (5 items selected)
[15:28 CST] - Optimizing compliance... (6 flags addressed)
[15:29 CST] - Adding WeChat elements...
[15:30 CST] ✓ Phase 2 complete: 7245 words, ready for publication

[15:30 CST] Final Validation: All checks passed ✓

[15:31 CST] ═══════════════════════════════════════
[15:31 CST] Workflow Complete!
[15:31 CST]
[15:31 CST] Files saved:
[15:31 CST]   📄 daily_news/docs/research/tech_news_20251107_raw.md
[15:31 CST]   📱 daily_news/docs/research/tech_news_20251107_wechat.md
[15:31 CST]   📊 daily_news/metadata/workflow_20251107.json
[15:31 CST]
[15:31 CST] Quality Metrics:
[15:31 CST]   Items: 50
[15:31 CST]   Quality Score: 8.2/10
[15:31 CST]   Compliance Flags: 6 (addressed)
[15:31 CST]   Execution Time: 31 minutes
[15:31 CST]
[15:31 CST] ✅ Recommendation: Ready for publication
[15:31 CST] ═══════════════════════════════════════
```

### Example 2: Custom Date with Strict Compliance

**Command**:
```
使用 tech-news-workflow skill --date 2025-11-08 --compliance strict
```

**Effect**:
- Search for November 8, 2025 news
- Apply stricter compliance filtering:
  - Reject any military-related content (vs. neutralize)
  - Require disclaimers for all financial data (vs. major data only)
  - Flag any US-China mentions (vs. only confrontational language)
- May result in fewer items but higher compliance confidence

### Example 3: Retry Phase 2 Only

**Command**:
```
使用 tech-news-workflow skill --skip-phase1 --structure theme_based
```

**Effect**:
- Skip research (use existing tech_news_20251107_raw.md)
- Force theme-based structure instead of domestic/international
- Useful for testing different formatting approaches

## Technical Requirements

### Dependencies
- **Skills**: daily-tech-news-search, wechat-tech-news-writer
- **Commands**: /sc:research
- **MCP Servers**: Tavily (or equivalent for web search)
- **File System**: Write access to daily_news/ directory

### System Requirements
- **Execution Time**: Allow 30-40 minutes for complete workflow
- **Network**: Stable connection for search queries
- **Storage**: ~1 MB per day (includes outputs and metadata)

---

**Version**: 1.0
**Last Updated**: 2025-01-07
**Skill Type**: Workflow automation and orchestration
**Dependencies**: daily-tech-news-search, wechat-tech-news-writer
