---
name: daily-tech-news-formatter
description: Multi-round content optimization engine for WeChat compliance, grammar refinement, punctuation normalization, and title enhancement. Generates format_report.md with before/after comparisons.
---

# Daily Tech News Formatter

> **🎨 Multi-Round Optimization Engine**: 5-8 rounds of systematic content refinement with quality tracking

## When to Use This Skill

Use this skill when you need to:
- Optimize WeChat article content for compliance and readability
- Apply 100+ sensitive keyword substitutions automatically
- Normalize all Chinese punctuation marks (，。：（）！etc.)
- Enhance headlines and section titles for engagement
- Perform grammar and semantic improvements
- Generate comprehensive formatting reports with before/after comparisons

**IMPORTANT**: This skill is designed to run automatically in the workflow pipeline after writing. It MUST generate `format_report.md` - the workflow will check for this file's existence and completeness.

## Quick Start

```bash
使用 daily-tech-news-formatter skill [input-file]
```

**Execution Time**: 4-6 minutes
**Input**: `tech_news_[YYYYMMDD]_wechat_draft.md` (from daily-tech-news-writer)
**Output**: `format_report_[YYYYMMDD].md` + `tech_news_[YYYYMMDD]_wechat_final.md`

## Core Optimization Rounds (Mandatory)

### Round 1: Compliance Optimization (合规性优化)

**Purpose**: Apply sensitive keyword substitutions to ensure WeChat publication safety

**Hardcoded Rules**:
```yaml
Risk_Tier_High: # 🔴 Must neutralize
  Military_Defense:
    - "五角大楼" → "美国国防部" / "美国政府"
    - "军事合同" → "政府研发合作" / "国防项目合作"
    - "军用" → "政府应用" / "特殊领域应用"
    - "国防部" → "政府部门" (when in negative context)

  US_China_Confrontation:
    - "中美对抗" → "中美关系调整" / "国际格局变化"
    - "中美科技战" → "中美科技政策差异"
    - "制裁" → "政策限制" / "出口管控"
    - "禁令" → "限制措施" / "政策调整"
    - "芯片战" → "半导体政策调整"
    - "封锁" → "限制" / "管控"

  Minor_Related: # Extremely sensitive
    - Avoid any negative framing of minor-related incidents
    - If unavoidable, focus on solutions/improvements only
    - Never use: "未成年人沉迷", "青少年问题"
    - Prefer: "青少年保护措施", "家长监护功能"

Risk_Tier_Medium: # 🟡 Add disclaimers
  Financial_Data:
    - ANY funding amount → Add: "（根据公开报道，未经官方确认）"
    - Stock prices → Add: "（数据来源：[source]，仅供参考）"
    - Revenue/profit → Add: "（以公司财报为准）"
    - Valuation → Add: "（市场估算，非官方数据）"

  Policy_Changes:
    - Government regulations → Add: "（具体政策以官方公告为准）"
    - Regulatory actions → Use neutral tone, cite official sources
    - Policy predictions → Add: "（基于当前信息分析，实际情况可能变化）"

  Market_Speculation:
    - Avoid: "暴涨"、"狂跌"、"崩盘"
    - Use: "显著增长"、"大幅下降"、"市场调整"
    - Any prediction → Add disclaimer

Risk_Tier_Low: # 🟢 Normal reporting
  Product_Launches:
    - Standard reporting, no special treatment
    - Verify product names and specs accuracy

  Funding_News:
    - Report as announced
    - Always cite source

  Technical_Progress:
    - Celebrate achievements objectively
    - No excessive superlatives
```

**Substitution Process**:
```python
def apply_compliance_substitutions(content):
    """
    Apply 100+ keyword substitutions with context awareness
    """
    substitutions = load_substitution_rules()
    changes_log = []

    for pattern, replacement, risk_level, context_rules in substitutions:
        # Context-aware replacement
        matches = find_with_context(content, pattern, context_window=50)

        for match in matches:
            # Check context rules
            if should_replace(match, context_rules):
                before = match.text
                after = apply_replacement(match, replacement)

                content = content.replace(before, after)
                changes_log.append({
                    'pattern': pattern,
                    'before': before,
                    'after': after,
                    'risk_level': risk_level,
                    'location': match.line_number
                })

    return content, changes_log

def should_replace(match, context_rules):
    """
    Determine if replacement should be applied based on context
    """
    # Some words are OK in positive contexts
    if context_rules.get('allow_positive'):
        if is_positive_context(match.surrounding_text):
            return False

    # Some words always replace in certain sections
    if context_rules.get('section_blacklist'):
        if match.section in context_rules['section_blacklist']:
            return True

    return True  # Default: replace
```

**Output**:
```markdown
### Round 1: Compliance Optimization

**Changes Applied**: 23 substitutions

#### High-Risk Changes (🔴)
1. Line 45: "五角大楼合同" → "美国政府研发合作"
2. Line 102: "中美科技战升级" → "中美科技政策差异加大"
3. Line 156: "芯片禁令" → "芯片出口限制措施"
[... 8 more high-risk changes ...]

#### Medium-Risk Enhancements (🟡)
1. Line 78: Added disclaimer to "$500M funding round"
   → "$500M融资（根据公开报道，未经官方确认）"
2. Line 134: Added disclaimer to "stock price surge"
   → "股价显著上涨（数据来源：Bloomberg，仅供参考）"
[... 7 more medium-risk changes ...]

#### Low-Risk Improvements (🟢)
1. Line 210: "暴涨" → "显著增长"
2. Line 287: "狂跌" → "大幅下降"
[... 5 more low-risk changes ...]

**Compliance Score**: ✅ 95/100 (Excellent - ready for publication)
```

### Round 2: Punctuation Normalization (标点符号标准化)

**Purpose**: Convert all English punctuation in Chinese content to Chinese punctuation

**Hardcoded Rules**:
```yaml
English_to_Chinese:
  - "," → "，" (comma, when in Chinese context)
  - "." → "。" (period, when end of Chinese sentence)
  - ":" → "：" (colon, when followed by Chinese)
  - ";" → "；" (semicolon, in Chinese context)
  - "!" → "！" (exclamation, in Chinese context)
  - "?" → "？" (question mark, in Chinese context)
  - "(" → "（" (left paren, in Chinese context)
  - ")" → "）" (right paren, in Chinese context)
  - "\"" → """ (left quote) or """ (right quote)
  - "'" → "'" (left single) or "'" (right single)

Context_Rules:
  Preserve_English_Punctuation:
    - Inside English words/phrases
    - URLs and technical identifiers
    - Code snippets
    - Product version numbers (e.g., "GPT-4.5")
    - Email addresses
    - Abbreviations (e.g., "U.S.", "Ph.D.")

  Smart_Quote_Matching:
    - Track quote depth for nested quotes
    - Use " " for outer quotes, ' ' for inner quotes
    - Example: 他说："她回答'我不知道'。"

  Mixed_Content:
    - "OpenAI发布GPT-5" (preserve hyphen in GPT-5)
    - "CEO说，这是重大突破" (use Chinese comma after Chinese text)
    - "根据TechCrunch报道，..." (Chinese comma after source name)
```

**Detection and Replacement**:
```python
def normalize_punctuation(content):
    """
    Intelligently replace English punctuation with Chinese equivalents
    """
    changes_log = []
    char_contexts = analyze_character_contexts(content)

    for i, char in enumerate(content):
        if char not in ENGLISH_PUNCTUATION:
            continue

        context = char_contexts[i]

        # Skip if in English context
        if is_english_context(context):
            continue

        # Skip if in preserved context
        if is_preserved_context(context):
            continue

        # Apply replacement
        chinese_equiv = get_chinese_equivalent(char, context)
        if chinese_equiv:
            before = content[max(0, i-10):min(len(content), i+10)]
            content = content[:i] + chinese_equiv + content[i+1:]
            after = content[max(0, i-10):min(len(content), i+10)]

            changes_log.append({
                'position': i,
                'before': char,
                'after': chinese_equiv,
                'context': before + ' → ' + after
            })

    return content, changes_log

def is_english_context(context):
    """
    Check if surrounding text is primarily English
    """
    surrounding = context['before'] + context['after']
    ascii_ratio = sum(ord(c) < 128 for c in surrounding) / len(surrounding)
    return ascii_ratio > 0.7

def is_preserved_context(context):
    """
    Check if this is a special context where English punctuation should be preserved
    """
    # URL detection
    if 'http' in context['before'] or '.com' in context['after']:
        return True

    # Version number detection (e.g., GPT-4.5)
    if re.match(r'[A-Za-z]+-?\d+\.?\d*', context['before'] + context['current'] + context['after']):
        return True

    # Code snippet detection
    if context['section_type'] == 'code':
        return True

    return False
```

**Output**:
```markdown
### Round 2: Punctuation Normalization

**Changes Applied**: 187 punctuation marks normalized

#### By Punctuation Type
| Type | English | Chinese | Count |
|------|---------|---------|-------|
| Comma | , | ，| 65 |
| Period | . | 。| 48 |
| Colon | : | ：| 23 |
| Parentheses | () | （）| 18 pairs |
| Quotes | "" | ""| 15 pairs |
| Exclamation | ! | ！| 12 |
| Question | ? | ？| 6 |

#### Preserved Contexts
- URLs: 34 instances
- Product versions: 12 instances (e.g., "GPT-4", "Claude-3.5")
- Technical terms: 8 instances
- English phrases: 15 instances

#### Sample Changes
1. Line 23: "OpenAI宣布, 新模型将..." → "OpenAI宣布，新模型将..."
2. Line 67: "CEO表示: \"这是突破\"" → "CEO表示："这是突破""
3. Line 143: "三个主要特点(性能, 成本, 效率)" → "三个主要特点（性能，成本，效率）"

**Normalization Score**: ✅ 100% Chinese punctuation in Chinese content
```

### Round 3: Grammar and Semantic Optimization (语法语义优化)

**Purpose**: Improve sentence structure, fix grammar errors, enhance clarity and flow

**Optimization Categories**:
```yaml
Sentence_Structure:
  - Fix run-on sentences (split into 2-3 shorter sentences)
  - Eliminate dangling modifiers
  - Improve parallel structure in lists
  - Reduce nested clauses (max 2 levels)

Word_Choice:
  - Replace vague terms with specific ones
  - Eliminate redundancy (e.g., "过去的历史" → "历史")
  - Use active voice instead of passive (when appropriate)
  - Improve transitions between paragraphs

Clarity:
  - Simplify complex technical jargon (add brief explanations)
  - Define acronyms on first use
  - Add context for unfamiliar company names
  - Clarify ambiguous pronoun references

Tone:
  - Maintain professional, objective tone
  - Remove overly promotional language
  - Balance enthusiasm with factual reporting
  - Consistent voice throughout article

Flow:
  - Improve topic sentences
  - Add transitional phrases
  - Ensure logical paragraph progression
  - Smooth section transitions
```

**Optimization Process**:
```python
def optimize_grammar_semantics(content):
    """
    Multi-pass optimization for grammar and meaning
    """
    changes_log = []

    # Pass 1: Sentence-level fixes
    sentences = split_into_sentences(content)
    for i, sent in enumerate(sentences):
        # Check sentence length
        if len(sent) > 100:  # Too long
            shorter_sents, reason = split_long_sentence(sent)
            sentences[i:i+1] = shorter_sents
            changes_log.append({
                'type': 'sentence_split',
                'before': sent,
                'after': shorter_sents,
                'reason': reason
            })

        # Fix common grammar issues
        fixed, grammar_changes = fix_grammar_issues(sent)
        if fixed != sent:
            sentences[i] = fixed
            changes_log.extend(grammar_changes)

    # Pass 2: Paragraph-level improvements
    paragraphs = group_into_paragraphs(sentences)
    for para in paragraphs:
        # Improve transitions
        improved, transition_changes = improve_transitions(para)
        if improved != para:
            changes_log.extend(transition_changes)

        # Enhance topic sentences
        improved, topic_changes = enhance_topic_sentence(para)
        if improved != para:
            changes_log.extend(topic_changes)

    # Pass 3: Document-level consistency
    final_content = '\n\n'.join(paragraphs)
    final_content, consistency_changes = ensure_consistency(final_content)
    changes_log.extend(consistency_changes)

    return final_content, changes_log
```

**Output**:
```markdown
### Round 3: Grammar and Semantic Optimization

**Changes Applied**: 42 improvements

#### Sentence Structure (15 changes)
1. Line 34: Split long sentence (125 chars → 2 sentences of 68 + 57 chars)
   **Before**: "OpenAI发布了GPT-5模型，这个模型具有10万亿参数，支持多模态能力包括文本、图像、音频和视频，并且能够进行高级推理和实时交互，预计将在2025年第二季度通过API向开发者开放。"
   **After**: "OpenAI发布了GPT-5模型，这个模型具有10万亿参数，支持文本、图像、音频和视频等多模态能力。该模型能够进行高级推理和实时交互，预计将在2025年第二季度通过API向开发者开放。"

2. Line 89: Fixed dangling modifier
   **Before**: "作为AI领域的领导者，该公司的新产品备受期待。"
   **After**: "OpenAI作为AI领域的领导者，其新产品备受期待。"

[... 13 more sentence structure improvements ...]

#### Word Choice (12 changes)
1. Line 45: Replaced vague term with specific one
   **Before**: "取得了很大的进展"
   **After**: "在模型性能上提升了40%"

2. Line 103: Eliminated redundancy
   **Before**: "过去的历史数据显示"
   **After**: "历史数据显示"

[... 10 more word choice improvements ...]

#### Clarity Enhancements (10 changes)
1. Line 67: Defined acronym on first use
   **Before**: "RLHF技术显著提升了模型表现"
   **After**: "RLHF（基于人类反馈的强化学习）技术显著提升了模型表现"

2. Line 145: Added context for company name
   **Before**: "Cohere宣布新一轮融资"
   **After**: "AI初创公司Cohere宣布新一轮融资"

[... 8 more clarity enhancements ...]

#### Tone Adjustments (5 changes)
1. Line 78: Removed overly promotional language
   **Before**: "这款革命性的产品将彻底改变行业"
   **After**: "这款产品有望为行业带来重要变革"

[... 4 more tone adjustments ...]

**Optimization Score**: ✅ 92/100 (Significant improvements in readability and clarity)
```

### Round 4: Title and Headline Enhancement (标题优化)

**Purpose**: Optimize main title, section headings, and item headlines for engagement and clarity

**Optimization Strategies**:
```yaml
Main_Title_Rules:
  Length: 15-30 characters (optimal for WeChat feed)
  Pattern: "[时间范围] + [核心主题] + [吸引点]"
  Examples:
    - "本周AI科技动态 | OpenAI发布GPT-5"
    - "11月科技新闻汇总 | 五大AI突破"
    - "48小时焦点 | AI投资创历史新高"

  Avoid:
    - Generic titles ("科技新闻")
    - Clickbait ("震惊！")
    - ALL CAPS
    - Excessive punctuation ("!!!")

Section_Heading_Rules:
  Format: "Emoji + Category Name"
  Length: 5-12 characters
  Clear hierarchy: Use ## for main sections, ### for subsections

  Examples:
    - "🇨🇳 国内科技动态"
    - "🤖 AI公司新闻"
    - "💰 融资与投资"
    - "📱 产品发布"

Item_Headline_Rules:
  Pattern: "[Company] + [Action Verb] + [Key Point]"
  Length: 20-40 characters
  Include key data when relevant

  Good Examples:
    - "OpenAI发布GPT-5，参数达10万亿"
    - "Anthropic获50亿美元融资，估值翻倍"
    - "NVIDIA推出Blackwell架构，AI性能提升5倍"

  Avoid:
    - Vague headlines ("OpenAI有新动作")
    - Missing key data ("融资成功")
    - Overly long (>50 chars)
```

**Enhancement Process**:
```python
def enhance_titles(content):
    """
    Optimize all titles and headlines for engagement
    """
    changes_log = []

    # Main title optimization
    main_title = extract_main_title(content)
    if not is_optimal_title(main_title):
        enhanced_title, reason = optimize_main_title(main_title, content)
        content = content.replace(main_title, enhanced_title, 1)
        changes_log.append({
            'type': 'main_title',
            'before': main_title,
            'after': enhanced_title,
            'reason': reason,
            'improvement_score': calculate_title_score(enhanced_title)
        })

    # Section headings optimization
    section_headings = extract_section_headings(content)
    for heading in section_headings:
        if not has_emoji(heading) or not is_clear(heading):
            enhanced_heading = optimize_section_heading(heading)
            content = content.replace(heading, enhanced_heading)
            changes_log.append({
                'type': 'section_heading',
                'before': heading,
                'after': enhanced_heading
            })

    # Item headlines optimization
    item_headlines = extract_item_headlines(content)
    for headline in item_headlines:
        score = score_headline(headline)
        if score < 7.0:  # Below acceptable threshold
            enhanced_headline = optimize_item_headline(headline)
            content = content.replace(headline, enhanced_headline)
            changes_log.append({
                'type': 'item_headline',
                'before': headline,
                'after': enhanced_headline,
                'score_before': score,
                'score_after': score_headline(enhanced_headline)
            })

    return content, changes_log

def optimize_main_title(title, content):
    """
    Create engaging main title based on content highlights
    """
    # Extract date range
    date_range = extract_date_range(content)

    # Identify top highlight (most important/engaging item)
    top_item = identify_top_highlight(content)

    # Generate title pattern
    if top_item:
        new_title = f"{date_range} | {top_item['company']}{top_item['action']}"
        reason = f"Highlighted top story: {top_item['headline']}"
    else:
        new_title = f"{date_range} | AI科技动态汇总"
        reason = "Generic title with clear time range"

    return new_title, reason

def score_headline(headline):
    """
    Score headline quality (0-10)
    """
    score = 5.0  # Start with baseline

    # Length check
    length = len(headline)
    if 20 <= length <= 40:
        score += 2.0
    elif length < 20 or length > 50:
        score -= 1.0

    # Has company name
    if has_company_name(headline):
        score += 1.0

    # Has action verb
    if has_action_verb(headline):
        score += 1.0

    # Has key data
    if has_key_data(headline):
        score += 1.0

    # Clarity (no vague terms)
    if not has_vague_terms(headline):
        score += 0.5

    return min(10.0, max(0.0, score))
```

**Output**:
```markdown
### Round 4: Title and Headline Enhancement

**Changes Applied**: 28 improvements

#### Main Title
**Before**: "科技新闻汇总"
**After**: "本周AI焦点 | OpenAI发布GPT-5，NVIDIA业绩创新高"
**Reason**: Added specific highlights and time context
**Score**: 3.5/10 → 8.5/10

#### Section Headings (8 improvements)
1. "国内新闻" → "🇨🇳 国内科技动态"
2. "AI公司" → "🤖 AI公司新闻"
3. "融资消息" → "💰 融资与投资"
[... 5 more section heading improvements ...]

#### Item Headlines (19 improvements)
1. Line 45:
   **Before**: "OpenAI发布新模型"
   **After**: "OpenAI发布GPT-5，参数规模达10万亿"
   **Score**: 4.0/10 → 8.5/10
   **Improvement**: Added specific product name and key metric

2. Line 89:
   **Before**: "Anthropic获得融资"
   **After**: "Anthropic获Amazon 50亿美元投资，估值达200亿"
   **Score**: 3.5/10 → 9.0/10
   **Improvement**: Added investor, amount, and valuation

3. Line 134:
   **Before**: "NVIDIA业绩表现良好"
   **After**: "NVIDIA Q3营收181亿美元，同比增长206%"
   **Score**: 4.5/10 → 8.0/10
   **Improvement**: Replaced vague term with specific metrics

[... 16 more item headline improvements ...]

**Average Headline Score**: 4.2/10 → 8.3/10 (+4.1 improvement)
```

### Round 5: Final Quality Assurance (最终质量检查)

**Purpose**: Comprehensive final check for consistency, accuracy, and publication readiness

**Verification Checklist**:
```yaml
Content_Verification:
  - All company names spelled consistently
  - All product names accurate and up-to-date
  - All numbers and metrics formatted consistently (e.g., "10万亿" vs "10trillion")
  - All dates in same format (YYYY年MM月DD日)
  - All currencies properly labeled (美元, 人民币)

Structure_Verification:
  - Table of contents matches actual sections
  - All internal links working (if any)
  - Consistent heading hierarchy (no skipped levels)
  - Balanced section lengths (no 10-line section next to 200-line section)
  - "48小时焦点" has exactly 5 items

Compliance_Final_Check:
  - No high-risk keywords remain
  - All disclaimers present where required
  - Financial data properly qualified
  - Policy content neutral and sourced

Formatting_Final_Check:
  - No English punctuation in Chinese text
  - No stray formatting characters
  - Consistent bullet/numbering style
  - Proper emoji usage (not excessive)
  - Line breaks appropriate (not too many blank lines)

Metadata_Verification:
  - Article date correct
  - Word count within range (6000-8000)
  - All required sections present:
    * 引导语 (Opening hook)
    * 48小时焦点 (Focus highlights)
    * 主要内容 (Main sections)
    * 免责声明 (Disclaimer)
    * 下期预告 (Preview)
    * 订阅提示 (Subscription prompt)
```

**Verification Process**:
```python
def final_quality_assurance(content):
    """
    Comprehensive final verification before publication
    """
    issues = []
    fixes_applied = []

    # Content verification
    content, content_issues = verify_content_accuracy(content)
    issues.extend(content_issues)

    # Structure verification
    structure_issues = verify_structure(content)
    issues.extend(structure_issues)

    # Compliance final check
    compliance_issues = final_compliance_check(content)
    if compliance_issues:
        issues.extend(compliance_issues)
        # Critical: terminate if compliance issues found in final check
        return content, issues, fixes_applied, "FAIL"

    # Formatting final check
    content, format_fixes = final_format_check(content)
    fixes_applied.extend(format_fixes)

    # Metadata verification
    metadata_issues = verify_metadata(content)
    issues.extend(metadata_issues)

    # Generate quality score
    quality_score = calculate_final_quality_score(content, issues)

    status = "PASS" if quality_score >= 85 else "WARNING"
    if len([i for i in issues if i['severity'] == 'critical']) > 0:
        status = "FAIL"

    return content, issues, fixes_applied, status

def verify_content_accuracy(content):
    """
    Check for consistency and accuracy issues
    """
    issues = []

    # Company name consistency
    company_variations = detect_company_name_variations(content)
    if company_variations:
        # Standardize to most common variation
        content = standardize_company_names(content, company_variations)
        for variation in company_variations:
            issues.append({
                'type': 'consistency',
                'severity': 'minor',
                'description': f"Company name variations: {variation['variations']}",
                'fixed': True
            })

    # Number formatting consistency
    number_inconsistencies = detect_number_format_inconsistencies(content)
    if number_inconsistencies:
        content = standardize_number_format(content)
        issues.append({
            'type': 'consistency',
            'severity': 'minor',
            'description': 'Number format inconsistencies detected and fixed',
            'fixed': True
        })

    return content, issues
```

**Output**:
```markdown
### Round 5: Final Quality Assurance

**Verification Completed**: ✅ All checks passed

#### Content Verification
- Company name consistency: ✅ All standardized
- Product name accuracy: ✅ Verified against official sources
- Number formatting: ✅ Consistent (中文数字格式)
- Date formatting: ✅ Consistent (YYYY年MM月DD日)
- Currency labels: ✅ All properly marked

#### Structure Verification
- Table of contents: ✅ Matches sections
- Heading hierarchy: ✅ No skipped levels
- Section balance: ✅ Reasonable length distribution
- "48小时焦点": ✅ Exactly 5 items

#### Compliance Final Check
- High-risk keywords: ✅ 0 remaining (all neutralized)
- Disclaimers: ✅ Present in all required locations
- Financial qualifications: ✅ All properly marked
- Policy content: ✅ Neutral and sourced

#### Formatting Final Check
- Punctuation: ✅ 100% Chinese in Chinese text
- Formatting characters: ✅ Clean
- Bullet style: ✅ Consistent
- Emoji usage: ✅ Appropriate
- Line breaks: ✅ Proper spacing

#### Metadata Verification
- Article date: ✅ 2025-11-20
- Word count: ✅ 7,234 words (within 6000-8000 range)
- Required sections: ✅ All present

#### Minor Issues Fixed (Non-critical)
1. Standardized "OpenAI" (was: "OpenAI" and "Open AI")
2. Fixed number format: "1000亿" (was: "100billion")
3. Adjusted section break spacing (removed excessive blank lines)

**Final Quality Score**: 94/100 (Excellent - Ready for Publication)
**Status**: ✅ PASS
```

## Optional Enhancement Rounds

### Round 6: Engagement Optimization (Optional)

- Add rhetorical questions to engage readers
- Insert relevant analogies for complex concepts
- Enhance storytelling elements
- Optimize reading flow

### Round 7: SEO Optimization (Optional)

- Keyword density optimization
- Meta description generation
- Tag suggestions
- Related content recommendations

### Round 8: Visual Element Suggestions (Optional)

- Identify locations for infographics
- Suggest chart types for data visualization
- Recommend image placements
- Note sections that would benefit from visual aids

## Output Format

### 1. Format Report (format_report_[DATE].md)

```markdown
# Tech News Formatting Report | 2025-11-20

> **Execution Time**: 2025-11-20 16:45:00 CST
> **Input File**: tech_news_20251120_wechat_draft.md
> **Output File**: tech_news_20251120_wechat_final.md
> **Overall Status**: ✅ PASS

---

## Executive Summary

- Total Optimization Rounds: 5 mandatory + 0 optional
- Total Changes Applied: 279 improvements
- Compliance Score: 95/100
- Grammar Score: 92/100
- Title Quality: 8.3/10
- Final Quality Score: 94/100
- **Verdict**: ✅ Ready for Publication

---

## Round-by-Round Summary

| Round | Focus | Changes | Score | Status |
|-------|-------|---------|-------|--------|
| 1 | Compliance | 23 | 95/100 | ✅ PASS |
| 2 | Punctuation | 187 | 100/100 | ✅ PASS |
| 3 | Grammar | 42 | 92/100 | ✅ PASS |
| 4 | Titles | 28 | 8.3/10 | ✅ PASS |
| 5 | QA | 3 fixes | 94/100 | ✅ PASS |

---

[Detailed output from each round as shown above]

---

## Before/After Comparison

### Key Improvements Showcase

#### Example 1: High-Risk Compliance Fix
**Before**: "美国五角大楼宣布新的军事AI合同，价值20亿美元，引发中美科技战升级担忧。"

**After**: "美国政府部门宣布新的AI研发合作项目，价值20亿美元（根据公开报道，未经官方确认）。这一举措反映了中美在科技政策方面的差异。"

**Changes**:
- "五角大楼" → "政府部门"
- "军事AI合同" → "AI研发合作项目"
- "中美科技战" → "中美科技政策差异"
- Added financial disclaimer

#### Example 2: Punctuation and Grammar Combined
**Before**: "OpenAI的CEO Sam Altman表示:\"GPT-5将会彻底改变整个行业, 它的能力是前所未有的.\""

**After**: "OpenAI首席执行官Sam Altman表示："GPT-5有望为行业带来重要变革，其能力显著超越此前的模型。""

**Changes**:
- "OpenAI的CEO" → "OpenAI首席执行官"
- English colon → Chinese colon
- English quotes → Chinese quotes
- English comma → Chinese comma
- English period → Chinese period
- "彻底改变" → "带来重要变革" (toned down)
- "前所未有" → "显著超越此前" (more specific)

#### Example 3: Headline Enhancement
**Before**: "Anthropic获得投资"

**After**: "Anthropic获Amazon 50亿美元投资，估值达200亿美元"

**Changes**:
- Added investor name (Amazon)
- Added specific amount (50亿美元)
- Added valuation (200亿美元)
- Headline score: 3.5/10 → 9.0/10

---

## Publication Readiness Checklist

✅ Content Quality
  - ✅ All facts verified and sourced
  - ✅ Grammar and spelling correct
  - ✅ Consistent terminology throughout
  - ✅ Clear and engaging writing

✅ Compliance
  - ✅ All sensitive keywords neutralized
  - ✅ Disclaimers added where required
  - ✅ Tone appropriate for Chinese market
  - ✅ No policy violations

✅ Formatting
  - ✅ Chinese punctuation throughout
  - ✅ Consistent structure and hierarchy
  - ✅ Proper emoji usage
  - ✅ Clean formatting (no artifacts)

✅ WeChat Requirements
  - ✅ Word count: 6,000-8,000 ✓ (7,234)
  - ✅ Engaging title and opening
  - ✅ Clear table of contents
  - ✅ "48小时焦点" section with 5 items
  - ✅ Proper ending (disclaimer + preview + subscription)

---

## Workflow Integration

- Format Status: ✅ PASS
- Output Files:
  - ✅ format_report_20251120.md (this file)
  - ✅ tech_news_20251120_wechat_final.md
- Next Phase: Publication / Export to Word
- Manual Review: Not required (quality score >90)

---

**Generated by**: daily-tech-news-formatter v4.0.0
**Execution Time**: 4 minutes 32 seconds
**Optimization Engine**: Rule-based (60%) + LLM-assisted (40%)
**Report Format**: v4.0-standard
```

### 2. Final Formatted Article (tech_news_[DATE]_wechat_final.md)

Standard WeChat-ready markdown with all optimizations applied.

## Integration with Workflow

### Input Requirements
- **File**: `tech_news_[YYYYMMDD]_wechat_draft.md` from daily-tech-news-writer
- **Format**: Markdown with WeChat structure
- **Status**: Must pass validator and writer phases

### Output Guarantees
- **Report**: `format_report_[YYYYMMDD].md` ALWAYS generated
- **Article**: `tech_news_[YYYYMMDD]_wechat_final.md` only if formatting succeeds
- **Status**: Explicit PASS/WARNING/FAIL in report

## Reference Documentation

- **[optimization_rules.md](references/optimization_rules.md)** - Complete optimization rule specifications
- **[sensitive_keywords.md](references/sensitive_keywords.md)** - 100+ keyword substitution rules (inherited from writer skill)
- **[punctuation_guide.md](references/punctuation_guide.md)** - Chinese/English punctuation usage rules
- **[title_patterns.md](references/title_patterns.md)** - Headline and title best practices

---

**Version**: 4.0.0
**Optimization Engine**: Rule-based (60%) + LLM-assisted (40%)
**Rounds**: 5 mandatory + 3 optional
**Quality Gate**: 85/100 minimum for publication approval
**Report Generation**: Always (even on failure)
