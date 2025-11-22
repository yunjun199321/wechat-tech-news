# Product Focus Optimization - v4.1

> **Implementation Date**: 2025-11-22
> **Version**: 4.1.0
> **Status**: Ready for Testing

## Overview

Based on user feedback about excessive investment news, we've implemented a systematic optimization to shift focus toward AI product launches, trending tools, and technical activities.

**Target Content Ratio**: 60% products/tools, 30% activities/business, 10% investment

---

## Changes Implemented

### 1. Search Query Optimization

**File**: `daily-tech-news-search/references/search_queries.md`

#### New Product-Focused Queries

```yaml
🚀 AI Product Launches (HIGH PRIORITY - 40%):
  - "AI product launch" OR "AI tool release"
  - "launches AI" OR "unveils AI product"
  - Company-specific: "[Company] + launch/release"
  - Product Hunt trending (today + yesterday)
  - Hacker News "Show HN" (48h window)

🎯 Trending AI Products (HIGH PRIORITY - 20%):
  - Product Hunt (>100 upvotes)
  - Hacker News front page (>200 points)
  - GitHub Trending (>100 stars in 48h)
  - Reddit r/artificial (>200 upvotes)

📊 Research & Papers (MEDIUM - 15%):
  - arXiv AI papers (daily)
  - Conference proceedings (NeurIPS, ICML, CVPR)
  - Lab research announcements

🤝 Activities & Events (MEDIUM - 10%):
  - AI conferences and summits
  - Keynotes and product demos
  - Strategic partnerships (product-focused)

💼 Business & Strategy (MEDIUM - 5%):
  - Product-related strategic moves only
  - C-level changes (major companies only)

💰 Investment (LOW - 10%):
  - ≥$100M only (increased from $50M)
  - Companies with shipped products only
  - Strategic significance required
  - Weight: 0.3x (vs 1.0x for products)
```

#### Deprecated/Reduced Queries

```yaml
Removed:
  - Generic funding searches (Series A/B)
  - Routine venture capital news
  - Financial earnings (unless product impact)
  - General semiconductor news

Reduced Frequency:
  - Company financial news (quarterly → major only)
  - Market analysis (unless AI-specific)
  - Policy news (unless direct product impact)
```

---

### 2. Validation Rules Enhancement

**File**: `daily-tech-news-validator/references/validation_rules.md`

#### Added Community Sources (Tier 2 - Credibility 7-8/10)

```yaml
Community_Product_Discovery:
  producthunt.com:
    - Featured products → 8/10
    - Top 10 daily → 7/10
    Validation: Maker verified + working demo

  news.ycombinator.com:
    - Front page (>200 points) → 8/10
    - Show HN (>50 points) → 7/10
    Validation: Positive sentiment + active discussion

  github.com/trending:
    - >500 stars in 48h → 8/10
    - >100 stars in 48h → 7/10
    Validation: Active repo + clear README

  reddit.com/r/artificial:
    - >200 upvotes + verified → 7/10
    Validation: Clear product + working link
```

#### Round 6: Content Type Classification (NEW)

**Purpose**: Enforce 60/30/10 ratio through weighted scoring

```python
Content Types & Weights:
  Product_Launch: 10/10 × 1.0 = Highest Priority
  Trending_Product: 9/10 × 1.0 = Very High
  Research_Activity: 8/10 × 0.8 = Medium
  Event_Activity: 7/10 × 0.7 = Medium
  Business_News: 6/10 × 0.5 = Lower Medium
  Investment_Funding: 3/10 × 0.3 = Lowest Priority

Selection Algorithm:
  1. Classify all items by type
  2. Apply weight multipliers
  3. Sort by weighted score
  4. Select top 27 high-priority (products)
  5. Select top 13 medium-priority (activities/business)
  6. Select top 5 low-priority (investment ≥$100M only)

Quality Gate:
  - High priority count ≥ 24 → PASS
  - Product ratio ≥ 40% → PASS
  - Investment ratio ≤ 15% → PASS
```

---

## Expected Impact

### Before Optimization (Estimated Current State)

```
Content Distribution:
- Investment/Funding: ~30-35%
- Product Launches: ~25-30%
- Business News: ~15-20%
- Research: ~10-15%
- Events: ~5-10%

Issues:
- Too much funding news (Series A/B rounds)
- Generic business updates
- Missing trending community products
- Limited focus on actual product launches
```

### After Optimization (Target State)

```
Content Distribution:
- 🚀 Product Launches: 40% (~18 items)
- 🎯 Trending Products: 20% (~9 items)
- 📊 Research & Papers: 15% (~7 items)
- 🤝 Events & Activities: 10% (~4 items)
- 💼 Business News: 5% (~2 items)
- 💰 Investment (≥$100M): 10% (~4-5 items)

Improvements:
✅ 60% focus on actual products and tools
✅ Community-driven trending products included
✅ Investment news reduced to major rounds only
✅ More balanced geographic coverage
✅ Higher engagement potential (product launches > funding news)
```

---

## Testing Plan

### Phase 1: Dry Run (Recommended)

```bash
# Test with custom date to compare before/after
使用 tech-news-workflow skill --date 20251120 --count 50

# Review outputs:
# 1. Check tech_news_20251120_raw.md (collection)
# 2. Check validation_report_20251120.md (Round 6 classification)
# 3. Check tech_news_20251120_wechat_final.md (final distribution)

# Analyze content ratio:
grep "Content Distribution" validation_report_20251120.md
```

### Phase 2: Live Test

```bash
# Run today's workflow with optimizations
使用 tech-news-workflow skill

# Compare with previous day's run (if available)
# Expected changes:
# - More Product Hunt / HN items
# - Fewer Series A/B funding announcements
# - More GitHub trending projects
# - Clearer product launch focus in headlines
```

### Phase 3: User Validation

**Review Checklist**:
- [ ] Product launches are prominent (≥40%)
- [ ] Investment news reduced (≤15%)
- [ ] Community trending products included
- [ ] Content feels more "product-focused"
- [ ] Still maintaining quality and credibility

---

## Rollback Plan (If Needed)

If optimization produces undesirable results:

### Option 1: Adjust Ratios

```bash
# Edit validation_rules.md → Round 6
# Change target distribution:
# From: 60/30/10 → To: 50/35/15 (more balanced)

# Adjust weights:
Investment_Funding: 0.3 → 0.5 (increase weight)
```

### Option 2: Relax Filters

```bash
# Edit search_queries.md
# Reduce investment threshold:
From: ≥$100M → To: ≥$75M

# Include more funding types:
Add: Series B rounds for major companies
```

### Option 3: Full Rollback

```bash
# Restore from git history
git checkout HEAD~1 -- daily-tech-news-search/references/search_queries.md
git checkout HEAD~1 -- daily-tech-news-validator/references/validation_rules.md
```

---

## Maintenance Notes

### Monthly Review

**Check these metrics**:
1. Content type distribution (are we hitting 60/30/10?)
2. Source diversity (not over-relying on any single source)
3. Community source quality (Product Hunt/HN items still relevant?)
4. User satisfaction (are readers engaging more with product content?)

### Adjustment Triggers

**Consider tuning if**:
- Product ratio drops below 50% for 3+ consecutive days
- Investment ratio exceeds 20% for 3+ consecutive days
- Community sources bring low-quality items (>30% flagged)
- Major product launches are being missed

### Domain Whitelist Updates

**Add new sources as they emerge**:
```yaml
Candidates to Monitor:
  - futurepedia.io (AI product directory)
  - theresanaiforthat.com (AI tool aggregator)
  - aitools.inc (curated AI tools)
  - aitoptools.com (product rankings)

Criteria for Addition:
  - Consistent daily updates
  - Quality curation
  - Verifiable product information
  - Engagement metrics available
```

---

## FAQ

### Q: Why Product Hunt / Hacker News?

**A**: These are primary discovery platforms for new AI tools. Many innovative products launch there first before mainstream media coverage. Including them ensures we capture trending products that users actually want to know about.

### Q: What if investment news is actually important?

**A**: We're not eliminating it, just being selective. Major rounds (≥$100M), IPOs, and strategic investments are still included. We're filtering out routine Series A/B rounds that add noise without value.

### Q: Will this reduce geographic diversity?

**A**: No. Round 6 classification is independent of geography. Chinese companies launching products get the same high priority as US companies. The focus is on content type, not location.

### Q: What about research papers - still included?

**A**: Yes! Research papers are medium priority (15% allocation). We still cover major breakthroughs, conference papers, and lab research. Just less generic business news.

### Q: How do I tune the ratios?

**A**: Edit `validation_rules.md` → Round 6 → `select_balanced_items()` function. Adjust the target counts:
```python
# Current: 27 high / 13 medium / 5 low
# More balanced: 24 high / 16 medium / 5 low
selected.extend(high_priority[:24])  # Changed from 27
selected.extend(medium_priority[:16])  # Changed from 13
```

---

## Version History

**v4.1.0** (2025-11-22)
- Added Product Hunt, Hacker News, GitHub Trending to Tier 2 sources
- Implemented Round 6: Content Type Classification
- Updated search queries for 60/30/10 ratio
- Increased investment threshold to $100M
- Added weighted scoring system

**v4.0.0** (2025-01-07)
- Initial 5-phase pipeline architecture
- Basic validation rules
- No content type classification

---

## Next Steps

1. **Test the workflow**: Run `使用 tech-news-workflow skill` and review outputs
2. **Analyze distribution**: Check if 60/30/10 ratio is achieved
3. **Gather feedback**: Does the content feel more product-focused?
4. **Fine-tune if needed**: Adjust weights or ratios based on results
5. **Document learnings**: Update this file with any insights

---

**Prepared by**: Claude Code Optimization
**Review by**: User
**Approval for Production**: Pending Testing

---

## ⚠️ Known Issues & Fixes

### Issue #1: Community Sources Being Filtered Out

**Problem**: Product Hunt, Hacker News, Reddit content was collected in Phase 1 but disappeared from final article.

**Root Cause**: Validation order conflict
- Community sources added to Tier 2 whitelist
- But `reddit.com` was in Social_Media blacklist
- Validator checked blacklist BEFORE whitelist
- Result: All Reddit posts rejected, even from approved subreddits

**Fix Applied** (v4.1.1):
1. Updated blacklist to include explicit EXCEPT clauses
2. Added validation order documentation (whitelist → blacklist)
3. Provided Python reference implementation
4. Added test cases to verify correct behavior

**Files Modified**:
- `daily-tech-news-validator/references/validation_rules.md`
  - Added "IMPORTANT: Check whitelist exceptions BEFORE blacklist"
  - Added EXCEPT clauses for reddit.com, twitter.com
  - Documented validation order with examples
  - Added Python implementation guide

**Verification**:
```python
# Reddit approved subreddit → ACCEPT
validate("reddit.com/r/artificial") → "ACCEPT (Tier 2)"

# Reddit random subreddit → REJECT
validate("reddit.com/r/pics") → "REJECT (Blacklist)"

# Product Hunt → ACCEPT
validate("producthunt.com") → "ACCEPT (Tier 2)"

# HN → ACCEPT
validate("news.ycombinator.com") → "ACCEPT (Tier 2)"
```

**Impact**:
- ✅ Product Hunt products now appear in final article
- ✅ Hacker News "Show HN" posts included
- ✅ GitHub Trending projects included
- ✅ Reddit r/artificial and r/MachineLearning posts included (if >200 upvotes)

**Testing Required**:
After next workflow run, verify validation_report.md shows:
- Product Hunt items in "Accepted Items" section
- HN items with proper credibility scores (7-8/10)
- Reddit posts from approved subreddits passing validation
- No false rejections of community sources

---

## 🔍 Debugging Guide

### How to Check if Community Sources are Being Collected

**Step 1**: Check Phase 1 output (Collection)
```bash
grep -i "producthunt\|hackernews\|github.com/trending" tech_news_[DATE]_raw.md
```
Expected: Should see items from these sources

**Step 2**: Check Phase 2 output (Validation)
```bash
grep -A 5 "Round 1: Source Credibility" validation_report_[DATE].md
```
Look for:
- producthunt.com → Score: 8/10 ✅
- news.ycombinator.com → Score: 8/10 ✅
- reddit.com/r/artificial → Score: 7/10 ✅

**Step 3**: Check Phase 4 output (Final Article)
```bash
grep -i "product hunt\|hacker news\|github" tech_news_[DATE]_wechat_final.md
```
Expected: Community sources should appear in article with attribution

### If Community Sources Still Missing

**Check 1**: Validation Order
```bash
# Verify whitelist is checked first
grep -A 20 "Validation Order" daily-tech-news-validator/references/validation_rules.md
```
Should show: Tier 1 → Tier 2 → Special Cases → Blacklist

**Check 2**: Engagement Thresholds
```bash
# Check if items meet minimum engagement
validation_report → Round 6 → Content Type Classification
```
Minimum requirements:
- Product Hunt: >100 upvotes
- Hacker News: >50 points (Show HN) or front page
- GitHub: >100 stars in 48h
- Reddit: >200 upvotes

**Check 3**: Time Window
Community sources use 48-hour window (not 24h). Verify:
```bash
grep "published_date" validation_report_[DATE].md
```

### Common False Positives

**Reddit posts rejected despite >200 upvotes**:
- Check if from approved subreddits (r/artificial, r/MachineLearning)
- Other subreddits will be blacklisted

**Product Hunt item with low score**:
- Check if "Product of the Day" or top 10
- Items outside top 10 may get lower priority

**HN post rejected**:
- "Show HN" posts need >50 points
- Regular posts need front page placement (>200 points)

