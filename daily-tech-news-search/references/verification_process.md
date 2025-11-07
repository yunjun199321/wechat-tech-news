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

## Round 2: Date and Freshness Validation

### Objective
Ensure all news items are from the target date (within 24 hours in China timezone) and remove outdated information.

### Date Requirements

**Primary Criterion**: Published within last 24 hours (China Standard Time, UTC+8)

**Calculation Example**:
```
Target date: November 7, 2025 (CST)
Valid timestamp range:
  Start: November 6, 2025 16:00 UTC (Nov 7, 00:00 CST)
  End: November 7, 2025 15:59 UTC (Nov 7, 23:59 CST)
```

### Timestamp Types

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

#### Reject: No Date Information
- Cannot verify timeliness
- Remove from results

### Process Steps

**Step 1: Timestamp Extraction**
```
For each item:
1. Extract publication date from source
2. Convert to UTC+8 (China time)
3. Calculate hours since publication
4. Flag if >24 hours old
```

**Step 2: Timezone Normalization**
```
Handle multiple timezone formats:
- ISO 8601: "2025-11-07T10:30:00Z"
- Unix timestamp: 1730973000
- Human readable: "November 7, 2025, 10:30 AM EST"

Convert all to: "2025-11-07 18:30 CST"
```

**Step 3: Freshness Scoring**
```
Age in hours (from current China time):
  0-6 hours: Breaking news (priority boost)
  6-12 hours: Very fresh
  12-18 hours: Fresh
  18-24 hours: Acceptable
  >24 hours: Reject
```

**Step 4: Update vs. Original Check**
```
For "updated" timestamps:
1. Check if original publication was within window
2. Verify update includes new information
3. If just formatting/correction, use original date
```

### Special Cases

#### Scheduled Announcements
```
Example: Earnings calls at 4 PM EST

Publication time: 4:00 PM EST (Nov 7)
China time: 5:00 AM (Nov 8)
Status: Accept if within overall 24h window
```

#### Breaking News During Cutoff
```
Example: News published at 11:50 PM CST

If current time is 11:55 PM CST:
- Accept (within 24h window)
- Mark as "late-breaking"
- May shift to next day's collection
```

#### Weekend and Holiday Delays
```
For Monday collections:
- Acceptable range may extend to Friday afternoon
- Flag weekend news separately
- Prioritize Monday morning announcements
```

### Output Metrics

**After Round 2**:
- Items from Round 1: ~60-70
- Items outside 24h window: ~5-10
- Items without valid timestamp: ~2-5
- Items passing to Round 3: ~55-65
- Average age: 12-18 hours

### Decision Tree

```
Timestamp extracted?
    ├─ No → Can we estimate reliably?
    │       ├─ Yes → Use estimate, flag, continue
    │       └─ No → Reject
    └─ Yes → Within 24h window (CST)?
            ├─ Yes → Pass to Round 3
            └─ No → Is it scheduled event just outside window?
                    ├─ Yes → Include with note
                    └─ No → Reject
```

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
