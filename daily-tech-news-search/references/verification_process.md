# Five-Round Verification Process

## Overview

This document details the systematic 5-round verification process used to ensure quality, accuracy, and compliance of collected tech news items.

---

## Verification Philosophy

**Core Principles**:
1. **Trust but Verify**: Start with reputable sources but confirm facts
2. **Multi-Source Triangulation**: Cross-reference important claims
3. **Systematic Filtering**: Each round has clear pass/fail criteria
4. **Progressive Refinement**: Each round builds on previous improvements
5. **Quality over Quantity**: Better to have 45 excellent items than 60 mediocre ones

**Quality Targets**:
- Source credibility: ≥7/10 average
- Content completeness: ≥7/10 average
- Date accuracy: 100% compliance
- Deduplication rate: ≥95% unique
- Final count: 45-55 items

---

## Round 1: Source Credibility Check

### Objective
Filter out low-quality, unreliable, or unverifiable sources to establish a foundation of trustworthy information.

### Scoring Criteria (1-10 scale)

#### Score 10/10: Official Primary Sources
- Company press releases and blog posts
- SEC filings and investor relations pages
- Government agency announcements
- Official social media accounts (verified)

**Examples**:
- blog.openai.com
- investor.google.com
- sec.gov filings
- @OpenAI (verified Twitter)

#### Score 9/10: Top-Tier Media
- Bloomberg, Reuters, Wall Street Journal
- TechCrunch, The Verge, Ars Technica
- Financial Times, CNBC

**Criteria**:
- Established editorial standards
- Fact-checking processes
- Named journalists/authors
- Clear publication dates

#### Score 8/10: Reputable Industry Sources
- MIT Technology Review
- IEEE Spectrum
- VentureBeat
- InfoQ (for technical content)

**Criteria**:
- Domain expertise
- Regular publication schedule
- Cited sources
- Professional presentation

#### Score 7/10: Acceptable with Verification
- Well-known tech blogs
- Major news aggregators with attribution
- Industry analyst reports
- Verified LinkedIn company posts

**Criteria**:
- Attribution to original source
- Author credentials visible
- No sensationalist language
- Can be cross-referenced

#### Score 6/10 and Below: Reject
- Personal blogs (unless expert-verified)
- Unverified social media posts
- Content farms
- Sites with no about/contact info
- AI-generated content without disclosure

### Process Steps

**Step 1: Initial Source Scoring**
```
For each news item:
1. Identify source domain
2. Check against known source database
3. Assign preliminary score
4. Flag items scoring <7
```

**Step 2: Flagged Item Review**
```
For items scoring 6 or below:
1. Search for same story from better source
2. If found, replace source and re-score
3. If not found, mark for removal
```

**Step 3: Cross-Reference High-Impact Items**
```
For items scoring ≥8 with major claims:
1. Verify on official company site
2. Check multiple tier-1 sources
3. Confirm key facts (amounts, dates, names)
```

**Step 4: Author and Byline Check**
```
For tier-2 and tier-3 sources:
1. Verify author exists and has credentials
2. Check for previous quality work
3. Ensure article has proper attribution
```

### Output Metrics

**After Round 1**:
- Starting items: ~80-120
- Items rejected: ~15-20
- Items upgraded (better source found): ~10-15
- Items passing to Round 2: ~60-70
- Average credibility score: Should be ≥7.5

### Decision Tree

```
Source identified
    ↓
Is it score ≥7?
    ├─ Yes → Pass to Round 2
    └─ No → Can we find better source?
            ├─ Yes → Replace source, re-score
            └─ No → Reject item
```

---

## Round 2: Time Validation & Strict 48h Enforcement

> **⚡ Version 3.0 Update**: Strict 48-hour hard limit with double verification (replaces 7-day progressive search from v2.0)

### Objective
Enforce strict 48-hour freshness requirement with enhanced validation to ensure all news items are recent and timely.

### Time Layer System (v3.0 - Strict 48h Mode)

**Overview**: News items classified into 2 active layers + auto-reject zone

```
Layer 0: Today (0-24h)        | 🟢 Tier 1 | Priority: Highest  | Weight: 1.00 | **Auto-include all**
Layer 1: Yesterday (24-48h)   | 🟡 Tier 2 | Priority: High     | Weight: 0.90 | **Supplement only**
Layer 2+: Older (>48h)        | 🔴 Reject | **Auto-reject** unless importance ≥9.5/10 + manual approval

Hard Limit: 48 hours
Target Output: ~40-45 items (reduced from 50 due to stricter time filter)
Freshness Priority: >80% from Layer 0 preferred
```

**Key Changes from v2.0**:
- ❌ Removed Layers 2-7 (48h-7 days) - now auto-rejected
- ✅ Layer 1 is now "supplement only" (triggered when Layer 0 < 35 items)
- ✅ Added manual approval exception for critical news (importance ≥9.5)

### Timestamp Extraction & Validation

#### Priority 1: Publication Timestamp
- Original article publication date/time
- Use this when available
- Most accurate representation

#### Priority 2: Last Updated Timestamp
- Use only if publication date unavailable
- Verify content is genuinely new (not just formatting update)
- Flag for extra scrutiny

#### Priority 3: Source Date Estimation
- When no explicit timestamp exists
- Use page meta tags, URL patterns
- Flag as "estimated" in verification notes

#### Reject: No Date Information OR >7 days old
- Cannot verify timeliness
- Remove from results

### Process Steps

**Step 1: Timestamp Extraction & Normalization**
```
For each item:
1. Extract publication date from source
2. Convert to UTC+8 (China time)
3. Calculate age in hours
4. Handle multiple timezone formats:
   - ISO 8601: "2025-11-07T10:30:00Z"
   - Unix timestamp: 1730973000
   - Human readable: "November 7, 2025, 10:30 AM EST"
5. Normalize to: "2025-11-07 18:30 CST"
```

**Step 2: Time Layer Assignment (v3.0)**
```
Based on age in hours (strict 48h mode):
  0-24h    → Layer 0 (🟢) - Auto-include
  24-48h   → Layer 1 (🟡) - Supplement only
  >48h     → Reject (🔴) - Auto-reject unless exception applies

Exception Criteria for >48h items:
  - Importance score ≥9.5/10 (breakthrough/major announcement)
  - Flagged for manual review
  - User explicitly approves
  - Logged in metadata as "overtime_approved"
```

**Step 3: Enhanced Double Verification (v3.0 New)**
```
Purpose: Prevent occasional time errors through multi-source validation

Check 1 - Metadata Timestamp:
  - Extract from <published>, og:published_time, datePublished
  - Calculate age vs current China time
  - Result: timestamp_age_hours

Check 2 - Content Analysis:
  - Scan article text for time indicators:
    - "today", "今天", "this morning" → likely 0-12h
    - "yesterday", "昨天" → likely 24-36h
    - Specific dates like "November 20, 2025"
  - Result: content_age_estimate

Check 3 - Cross-Validation:
  IF |timestamp_age - content_age| > 12 hours:
    🚨 FLAG for manual review
    Reason: "Timestamp mismatch detected"
    Action: Check source manually or reject if uncertain

Check 4 - Sanity Check:
  IF timestamp_age > 48 hours:
    IF importance < 9.5:
      ❌ Auto-reject, log reason
    ELSE:
      🚨 Pause workflow, ask user:
      "Found high-importance item but >48h old. Include? [Y/N]"
      "[Title], [Source], [Age: 73h], [Importance: 9.7/10]"
```

**Step 4: Fuzzy Date Handling (v3.0 New)**
```
IF no clear timestamp found:
  - Mark as "⚠️ Time unverified"
  - Apply credibility penalty: -2.0 points
  - IF final credibility < 6.0:
      ❌ Reject item
  - ELSE:
      Include but flag in output
      Note: "Publication time estimated from context"
```

**Step 5: Freshness Weight Calculation (v3.0 Simplified)**
```
For importance scoring in Round 5:
  Layer 0: base_importance × 1.00 (no penalty)
  Layer 1: base_importance × 0.90 (10% penalty)
  Layer 2+: Rejected (not applicable)
```

**Step 6: Metadata Enrichment (v3.0 Updated)**
```
Add to each item:
- time_layer: 0 | 1 (or "rejected" if >48h)
- layer_emoji: "🟢" | "🟡" | "🔴"
- hours_ago: 6.5
- publication_date_cst: "2025-11-20 14:30 CST"
- freshness_weight: 1.00 | 0.90
- time_verified: true | false (false if estimated)
- verification_method: "metadata" | "content_analysis" | "estimated"
```

### Output Format (Updated)

```markdown
**[#]. [Headline]**
- Source: TechCrunch | 9/10
- Date: 2025-11-17 14:30 CST | Layer 0 (6h ago) 🟢
- Summary: ...
- Key Data: ...

**[#]. [Headline]**
- Source: Bloomberg | 8/10
- Date: 2025-11-16 10:00 CST | Layer 1 (28h ago) 🟡
- Summary: ...
- Key Data: ...

**[#]. [Headline]**
- Source: Reuters | 9/10
- Date: 2025-11-14 16:00 CST | Layer 3 (74h ago) 🟠
- Summary: ...
- Supplement Reason: High-impact announcement (importance 9.2/10)
- Key Data: ...
```

### Special Cases

#### Scheduled Announcements
```
Example: Earnings calls at 4 PM EST

Publication time: 4:00 PM EST (Nov 7)
China time: 5:00 AM (Nov 8)
Calculation: Age = (Current CST - 5:00 AM Nov 8)
Assignment: Layer based on calculated age
```

#### Breaking News During Cutoff
```
Example: News published at 11:50 PM CST

If current time is 11:55 PM CST:
- Age: 5 minutes
- Layer: 0 (Today)
- Mark as "late-breaking" in notes
```

#### Weekend and Holiday Gaps
```
For Monday collections:
- May include Layer 2-3 items from Friday/Saturday
- Clearly label with layer emoji
- Document gap in metadata summary
- Example: "Weekend coverage: Layer 2-3 items included"
```

### Output Metrics (v3.0 Updated)

**After Round 2** (Strict 48h Mode):
- Items from Round 1: ~50-70
- Items beyond 48h: ~5-15 (auto-rejected, logged)
- Items without valid timestamp: ~2-5 (credibility penalized or rejected)
- Items flagged for manual review: ~1-3 (timestamp mismatch)
- Items by layer:
  - Layer 0 (Today): ~35-50 (target >80%)
  - Layer 1 (Yesterday): ~5-15 (supplement only)
  - Layer 2+ (>48h): 0 (rejected)
- Items passing to Round 3: ~45-60
- Average age: 6-18 hours (🚀 3x fresher than v2.0's 18-36h)
- Layer 0 percentage: 80-90% (vs 60-80% in v2.0)

### Decision Tree (v3.0 - Strict 48h)

```
Timestamp extracted?
    ├─ No → Can we estimate reliably?
    │       ├─ Yes → Estimate, mark "unverified", credibility -2.0
    │       │        └─ Final credibility ≥6.0? Pass : Reject
    │       └─ No → Reject (cannot verify timeliness)
    └─ Yes → Calculate age in hours
            ├─ Double verification:
            │   └─ Content analysis matches timestamp? (±12h tolerance)
            │       ├─ Yes → Continue
            │       └─ No → 🚨 Flag for manual review
            ├─ 0-24h (Layer 0)?
            │   └─ Yes → ✅ Auto-include, weight 1.00
            ├─ 24-48h (Layer 1)?
            │   └─ Yes → ⚠️ Mark "supplement", weight 0.90
            │           └─ Use ONLY if Layer 0 count < 35
            └─ >48h (Layer 2+)?
                ├─ Importance ≥9.5?
                │   ├─ Yes → 🚨 Ask user approval
                │   │        └─ Approved? Include : Reject
                │   └─ No → ❌ Auto-reject, log reason
                └─ Log rejected item for transparency
```

### Progressive Search Integration (v3.0 - Simplified)

**How Round 2 Enforces 48h Strict Mode**:

```
Search Phase 1: Today (Layer 0)
├─ Search executed for current China date
├─ All items processed through Round 1
├─ Round 2: Validate timestamps, assign to Layer 0
├─ Enhanced verification: double-check + sanity check
├─ Expected yield: 35-50 items
└─ If count ≥ 35 → ✅ Skip Phase 2, proceed to Round 3
    If count < 35 → ⚠️ Trigger Phase 2

Search Phase 2: Yesterday (Layer 1) - Triggered only if needed
├─ Search executed for (China date - 1)
├─ All items processed through Round 1
├─ Round 2: Validate timestamps, assign to Layer 1
├─ Select high-importance items (≥8.0/10) for supplementation
├─ Target: Supplement to 40-45 total items
└─ If total count ≥ 40 → ✅ Proceed to Round 3
    If total count < 30 → 🚨 Warning: Insufficient recent news

Search Phase 3+: Extended Backfill (>48h)
❌ Disabled by default in v3.0
⚠️ Only activated if:
  - Phase 2 yields < 30 total items
  - User explicitly approves extended search
  - Items must have importance ≥9.5/10
```

---

**Version Note**: v3.0 replaces v2.0's 7-day progressive backfill with strict 48h mode. For scenarios requiring older news, users must manually approve exceptions.

---

## Round 3: Content Deduplication

### Objective
Identify and merge duplicate stories from different sources, keeping the highest-quality version.

### Duplication Types

#### Type 1: Exact Duplicates
- Same story from different aggregators
- Syndicated content
- Republished press releases

**Action**: Keep highest-credibility source version

#### Type 2: Overlapping Coverage
- Same event, different angles
- Different journalists covering same announcement
- Regional vs. global coverage of same story

**Action**: Merge into single comprehensive item

#### Type 3: Related but Distinct
- Follow-up coverage
- Different aspects of larger story
- Sequential developments

**Action**: Keep separate but note relationship

### Detection Methods

#### Method 1: Headline Similarity
```
Algorithm: Cosine similarity of headline text

Threshold:
  >95% similar → Likely exact duplicate
  80-95% similar → Likely overlapping
  60-80% similar → Possibly related
  <60% → Distinct stories
```

#### Method 2: Key Fact Matching
```
Extract and compare:
- Company names
- Dollar amounts
- Product names
- Executive names
- Dates and locations

Match criteria:
  All 5 match → Definite duplicate
  4/5 match → Likely duplicate
  3/5 match → Possibly related
  <3/5 match → Distinct
```

#### Method 3: Source Analysis
```
Check for:
- Wire service attribution (AP, Reuters)
- Press release source
- Original reporting vs. aggregation

If multiple items cite same press release:
  → Merge to single item with best analysis
```

### Process Steps

**Step 1: Cluster by Topic**
```
Group items by primary subject:
- OpenAI group
- NVIDIA group
- Funding news group
- Policy/regulation group
etc.
```

**Step 2: Within-Cluster Comparison**
```
For each cluster:
1. Compare headlines pairwise
2. Extract key facts
3. Calculate similarity scores
4. Flag potential duplicates
```

**Step 3: Human Review of Flagged Pairs**
```
For each flagged pair:
1. Read both items fully
2. Determine relationship type
3. Decide: merge, keep both, or remove one
```

**Step 4: Merge Execution**
```
For items to be merged:
1. Select highest-credibility source
2. Incorporate unique details from other sources
3. Note all original sources in references
4. Update completeness score
```

### Merging Strategy

#### Best-of-Both Approach
```markdown
**Final Item Structure**:

**Headline**: [Use most accurate/concise headline]

**Primary Source**: [Highest credibility source] | Score X/10

**Summary**: [Combine best elements from both]

**Key Data**:
- Fact 1 [Source A]
- Fact 2 [Source B]
- Fact 3 [Both sources confirm]

**Additional Sources**:
- [Source B] | Score Y/10
- [Source C] | Score Z/10

**Cross-Reference**: All sources agree on core facts
```

### Output Metrics

**After Round 3**:
- Items from Round 2: ~55-65
- Duplicate clusters identified: ~8-12
- Items merged: ~5-10
- Items passing to Round 4: ~50-58 (unique)
- Deduplication rate: ≥95%

### Decision Tree

```
Item A and Item B comparison
    ↓
Same core story?
    ├─ Yes → Which source is higher credibility?
    │        ├─ A > B → Keep A, merge unique facts from B
    │        ├─ B > A → Keep B, merge unique facts from A
    │        └─ A = B → Keep both if different angles
    └─ No → Related stories?
            ├─ Yes → Keep both, note relationship
            └─ No → Keep both as distinct items
```

---

## Round 4: Completeness and Detail Check

### Objective
Ensure each news item contains sufficient detail, context, and key facts for reader understanding.

### Completeness Scoring (1-10 scale)

#### Score 9-10: Comprehensive
- All 5 W's answered (Who, What, When, Where, Why)
- Quantitative data included
- Official quotes or statements
- Industry context provided
- Impact analysis included

#### Score 7-8: Complete
- All 5 W's answered
- Key numbers included
- At least one quote or official statement
- Basic context provided

#### Score 5-6: Adequate but improvable
- Core facts present
- Some missing details
- Limited context
- No quotes

**Action**: Enhance with additional research

#### Score <5: Insufficient
- Missing key facts
- Vague or unclear
- No context

**Action**: Intensive research or removal

### Required Elements Checklist

#### Category 1: Funding News
```
Required:
- [ ] Company name
- [ ] Funding amount (specific number)
- [ ] Funding round (Series A/B/C, etc.)
- [ ] Lead investors
- [ ] Valuation (if disclosed)
- [ ] Intended use of funds

Nice to have:
- [ ] Previous funding history
- [ ] Total raised to date
- [ ] Company founding date
- [ ] Employee count
```

#### Category 2: Product Launches
```
Required:
- [ ] Product name
- [ ] Company
- [ ] Key features (at least 3)
- [ ] Availability date
- [ ] Pricing (if applicable)

Nice to have:
- [ ] Target market
- [ ] Competitive comparison
- [ ] Technical specifications
- [ ] Demo or screenshots
```

#### Category 3: Financial Results
```
Required:
- [ ] Company name
- [ ] Period (Q3 2025, etc.)
- [ ] Revenue (absolute number)
- [ ] Growth rate (YoY %)
- [ ] Key metrics

Nice to have:
- [ ] Profit/loss
- [ ] Guidance for next quarter
- [ ] CEO quote
- [ ] Stock price reaction
```

#### Category 4: Policy/Regulation
```
Required:
- [ ] Policy name
- [ ] Jurisdiction (US, EU, China, etc.)
- [ ] Effective date
- [ ] Key requirements
- [ ] Affected parties

Nice to have:
- [ ] Penalties for non-compliance
- [ ] Industry reaction
- [ ] Implementation timeline
```

### Process Steps

**Step 1: Automated Completeness Scan**
```
For each item:
1. Check for required elements (category-specific)
2. Calculate completeness score
3. Flag items scoring <7
```

**Step 2: Enhancement Research**
```
For flagged items:
1. Return to original source
2. Search for additional details
3. Check company official site
4. Find related coverage
```

**Step 3: Data Enrichment**
```
Add missing information:
- Quantitative data (amounts, percentages, dates)
- Official quotes from source articles
- Background context from company history
- Industry implications
```

**Step 4: Context Addition**
```
For each item, add:
- Brief company background (if not widely known)
- Comparison to competitors (if relevant)
- Historical context (if significant milestone)
- Impact analysis (why this matters)
```

### Output Metrics

**After Round 4**:
- Items from Round 3: ~50-58
- Items scoring <7: ~10-15
- Items successfully enhanced: ~8-12
- Items removed (couldn't enhance): ~2-3
- Items passing to Round 5: ~48-55
- Average completeness score: ≥7.5

### Decision Tree

```
Item completeness score calculated
    ↓
Score ≥7?
    ├─ Yes → Pass to Round 5
    └─ No → Can we find missing details?
            ├─ Yes → Research and enhance
            │        ↓
            │        Score now ≥7?
            │        ├─ Yes → Pass to Round 5
            │        └─ No → Repeat research
            └─ No reliable source → Remove item
```

---

## Round 5: Final Quality Gate

### Objective
Final selection to meet target count (~50 items) while ensuring geographic balance, topic diversity, and compliance readiness.

### Selection Criteria

#### Importance Scoring (1-10)

**Score 9-10: Must Include**
- Major company announcements (new products, CEOs)
- Large funding rounds (>$500M)
- Significant policy changes
- Major acquisitions or partnerships
- Breaking technological breakthroughs

**Score 7-8: Should Include**
- Medium funding rounds ($100M-$500M)
- Important product updates
- Quarterly financial results (major companies)
- Industry trend indicators
- Notable research publications

**Score 5-6: Nice to Have**
- Smaller funding rounds ($50M-$100M)
- Minor product updates
- Executive appointments
- Conference announcements

**Score <5: Exclude if over target**

### Balance Requirements

#### Geographic Distribution
```
Target (for ~50 items):
- US companies: 18-22 items (36-44%)
- China companies: 12-18 items (24-36%)
- Europe companies: 4-8 items (8-16%)
- Global/Other: 4-8 items (8-16%)

Acceptable variance: ±5%
Reject if: Any region >55% or <15%
```

#### Topic Diversity
```
Target distribution:
- AI companies: 15-20 items (30-40%)
- Tech giants: 8-12 items (16-24%)
- Chips/hardware: 6-10 items (12-20%)
- Funding/investment: 5-8 items (10-16%)
- Policy/regulation: 4-6 items (8-12%)
- Other (quantum, security): 4-6 items (8-12%)

Reject if: Any single category >50%
```

### Compliance Scan

#### High-Priority Flags
```
Scan for sensitive topics:
1. Military/defense contracts
   → Flag for language neutralization

2. US-China trade restrictions
   → Flag for neutral framing

3. Minor-related AI incidents
   → Flag for solution-focused approach

4. Unverified financial speculation
   → Flag for disclaimer addition

5. Political statements
   → Flag for neutrality check
```

#### Flagging Process
```
For each flag:
1. Add compliance note to item metadata
2. Suggest neutral alternative language
3. Include in compliance summary
4. Pass to wechat-tech-news-writer for handling
```

### Process Steps

**Step 1: Importance Ranking**
```
1. Score all items for importance (1-10)
2. Sort by importance score (descending)
3. Create "must include" list (score ≥9)
```

**Step 2: Balance Check**
```
1. Calculate current geographic distribution
2. Calculate current topic distribution
3. Identify underrepresented categories
4. Identify overrepresented categories
```

**Step 3: Strategic Selection**
```
If count > 55:
  1. Remove lowest-scoring items first
  2. Maintain geographic balance
  3. Preserve topic diversity
  4. Keep at least one item per major company

If count < 45:
  1. Review Round 4 rejected items
  2. Consider lowering completeness threshold to 6.5
  3. Expand to secondary companies
  4. Include more funding news
```

**Step 4: Final Compliance Scan**
```
1. Run automated keyword scan
2. Flag sensitive topics
3. Generate compliance notes
4. Create compliance summary report
```

**Step 5: Output Generation**
```
1. Order items by category and importance
2. Add metadata (scores, sources, flags)
3. Generate verification summary
4. Calculate quality metrics
5. Format as structured markdown
```

### Output Metrics

**After Round 5 (Final)**:
- Target count: 45-55 items
- Actual count: [calculated]
- Geographic balance: Within spec (Y/N)
- Topic diversity: Within spec (Y/N)
- Average importance score: ≥7.0
- Average credibility score: ≥7.5
- Average completeness score: ≥7.5
- Compliance flags: [count]
- Recommendation: Ready / Needs Review / Requires Enhancement

### Decision Tree

```
Current count evaluated
    ↓
Is count 45-55?
    ├─ Yes → Check balance
    │        ↓
    │        Geographic & topic balance OK?
    │        ├─ Yes → Run compliance scan → Output
    │        └─ No → Adjust selection to improve balance
    └─ No → Too many (>55) or too few (<45)?
            ├─ Too many → Remove lowest-scoring items
            └─ Too few → Add items from Round 4 rejects
```

---

## Quality Assurance

### Final Checklist

Before output generation:

```
Verification Completeness:
- [ ] Round 1: Source credibility (avg ≥7/10)
- [ ] Round 2: Date validation (100% within 24h)
- [ ] Round 3: Deduplication (≥95% unique)
- [ ] Round 4: Completeness (avg ≥7/10)
- [ ] Round 5: Balance and compliance

Target Achievement:
- [ ] Item count: 45-55
- [ ] Geographic balance: Within spec
- [ ] Topic diversity: ≥6 categories
- [ ] Compliance: All flags documented

Output Quality:
- [ ] Structured markdown format
- [ ] All metadata included
- [ ] Verification summary complete
- [ ] Quality metrics calculated
- [ ] Recommendation provided
```

### Common Issues and Remedies

#### Issue 1: Insufficient Items After Round 4
```
Remedy:
1. Lower completeness threshold to 6.5
2. Include more tier-2 companies
3. Expand date window to 30 hours
4. Include more funding news (<$100M)
```

#### Issue 2: Geographic Imbalance
```
Remedy:
1. Add underrepresented region items
2. Remove excess from overrepresented region
3. Search specifically for missing region news
4. Adjust importance scores by region balance
```

#### Issue 3: Too Many Duplicates Found
```
Remedy:
1. Review deduplication criteria
2. May indicate major breaking story
3. Keep best coverage
4. Note story significance in metadata
```

#### Issue 4: High Compliance Flag Rate (>20%)
```
Remedy:
1. Review search query focus
2. May indicate geopolitically active period
3. Ensure all flags have neutral alternatives
4. Add extra compliance notes
5. Consider splitting sensitive items to separate section
```

---

## Performance Tracking

### Round-by-Round Metrics Template

```markdown
## Verification Metrics Report

### Round 1: Source Credibility
- Input items: 85
- Avg credibility score: 7.8/10
- Items rejected (score <7): 12
- Items enhanced (source upgraded): 8
- Output items: 73
- Pass rate: 85.9%

### Round 2: Date Validation
- Input items: 73
- Items outside 24h window: 7
- Items without valid timestamp: 3
- Output items: 63
- Pass rate: 86.3%

### Round 3: Deduplication
- Input items: 63
- Duplicate clusters found: 9
- Items merged: 11
- Output items (unique): 52
- Deduplication rate: 96.8%

### Round 4: Completeness
- Input items: 52
- Avg completeness score: 7.9/10
- Items enhanced: 9
- Items removed: 1
- Output items: 51
- Pass rate: 98.1%

### Round 5: Final Selection
- Input items: 51
- Target range: 45-55
- Final count: 50
- Geographic balance: PASS
- Topic diversity: PASS
- Compliance flags: 6 items
- Recommendation: Ready for publication

### Overall Pipeline
- Starting raw items: 85
- Final verified items: 50
- Overall retention rate: 58.8%
- Average quality improvement: +2.3 points
- Total verification time: ~18 minutes
```

---

**Version**: 1.0
**Last Updated**: 2025-01-07
**Purpose**: Systematic quality assurance for daily tech news collection
