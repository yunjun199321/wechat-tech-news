---
name: wechat-tech-news-writer
description: Pure content writing engine that transforms validated news data into WeChat article structure. Creates engaging narratives with focus highlights, geographic categorization, and proper structure. No formatting - delegates to daily-tech-news-formatter.
---

# WeChat Tech News Writer

> **✍️ Version 4.0**: Pure writing engine - formatting and optimization delegated to dedicated formatter skill

## When to Use This Skill

Use this skill when you need to:
- Transform validated news data into WeChat article structure
- Create engaging narratives from technical news items
- Generate "48小时焦点" (focus highlights) section
- Organize content by geography (国内/国外) or themes
- Write clear, accessible summaries for general tech audience
- **Focus on content and structure** - compliance/formatting done by formatter

## Quick Start

```bash
使用 wechat-tech-news-writer skill [validated-json-file]
```

**Execution Time**: 5-8 minutes
**Input**: `tech_news_[YYYYMMDD]_validated.json` (from daily-tech-news-validator)
**Output**: `tech_news_[YYYYMMDD]_wechat_draft.md`
**Next Phase**: Pass to daily-tech-news-formatter for optimization

## Core Writing Process (v4.0 - Content Only)

1. **Load Validated Data** - Parse JSON from validator skill
2. **Generate Focus Highlights** - Select 5 most important items for "48小时焦点"
3. **Categorize Content** - Organize by geography or theme
4. **Write Engaging Summaries** - Transform technical data into readable narratives
5. **Structure Document** - Create standard WeChat article sections
6. **Generate Draft** - Output markdown with complete structure

## Content Structure Options

### Option 1: Geographic Categorization (国内/国外分类) - **Recommended**

```markdown
# 48小时科技新闻汇总 | [Date]

> [引导语 - Engaging 2-3 sentence summary of the week]

## 🌟 48小时焦点

> 快速浏览48小时最重要的科技动态

1. **🇺🇸 [地域标识] [简短标题]**
   一句话核心信息，突出影响和意义

2. **🇨🇳 [地域标识] [简短标题]**
   一句话核心信息，突出影响和意义

[... 5 items total ...]

## 🇨🇳 国内科技动态

### AI投资热潮
[Chinese AI company news, funding, etc.]

### 研发进展
[Chinese AI research and development]

### 人才与战略
[Talent movements, strategic partnerships in China]

## 🌍 国际科技动态

### AI前沿突破
[International AI breakthroughs and model launches]

### 科技巨头财报
[US tech giants' earnings and performance]

### 芯片与半导体
[AI chip news - NVIDIA, AMD, etc.]

### 投资并购
[International funding and M&A]

## 📜 全球政策监管 (独立板块)

[Policy and regulatory news affecting both regions]

## 📋 免责声明

[Standardized disclaimer from ending_template.md]

---

**📅 下期预告**

重点关注：
- [即将发生的重要活动1]
- [即将发生的重要活动2]

---

**🔔 订阅提示**

关注本公众号，每日获取精选AI科技新闻，不错过重要动态！
```

### Option 2: Theme-Based Categorization (主题分类) - Alternative

```markdown
## 🤖 AI模型与技术

### 大模型发布
[Model launches from all companies]

### 技术突破
[Technical breakthroughs and research]

## 💰 融资与投资

### 大额融资
[Funding rounds >$100M]

### 战略投资
[Strategic investments and partnerships]

## 📱 产品与应用

### 新产品发布
[Product launches and features]

### 应用落地
[Real-world AI applications]

## 🏢 企业动态

### 财报业绩
[Earnings and financial performance]

### 战略调整
[Corporate strategy and organizational changes]

## 📜 政策与监管

[Policy, regulation, and governance]
```

## Focus Highlights Selection ("48小时焦点")

### Selection Criteria

```yaml
Must_Have_3_Attributes:
  1. High Impact: Affects industry direction or multiple stakeholders
  2. Timeliness: Recent news (prefer Layer 0, today's news)
  3. Reader Interest: Appeals to broad tech audience, not overly technical

Scoring_Factors:
  Company_Prominence: OpenAI/Google/Microsoft > smaller startups
  News_Type: Model launch/Major funding > routine updates
  Financial_Scale: >$1B news > <$100M news
  Innovation_Level: Breakthrough > Incremental improvement
  Geographic_Relevance: Mix of international + domestic
  Cross-Domain_Impact: AI + chips > pure software

Target_Distribution:
  - 2-3 international (🇺🇸 🌍)
  - 1-2 domestic China (🇨🇳)
  - 1 policy/regulation (📜) if significant
  - Minimum 3, Maximum 5 items
```

### Example Selection Process

Given 45 validated items:

```python
def select_focus_highlights(validated_items):
    """
    Select 5 most important items for focus section
    """
    scored_items = []

    for item in validated_items:
        score = 0

        # Company prominence (0-30 points)
        if item['company'] in ['OpenAI', 'Anthropic', 'Google', 'Microsoft']:
            score += 30
        elif item['company'] in ['Meta', 'Amazon', 'NVIDIA', 'xAI']:
            score += 25
        else:
            score += 10

        # News type (0-25 points)
        if item['category'] == 'Model Launch':
            score += 25
        elif item['category'] == 'Major Funding' and item['amount'] > 1000000000:
            score += 23
        elif item['category'] == 'Breakthrough Research':
            score += 22
        elif item['category'] == 'Financial Results':
            score += 18
        else:
            score += 10

        # Timeliness (0-20 points)
        if item['time_layer'] == 0:  # Today
            score += 20
        elif item['time_layer'] == 1:  # Yesterday
            score += 15
        else:
            score += 5

        # Innovation level (0-15 points)
        innovation_keywords = ['breakthrough', 'first', 'record', 'largest', 'unprecedented']
        if any(kw in item['summary'].lower() for kw in innovation_keywords):
            score += 15
        else:
            score += 5

        # Cross-domain impact (0-10 points)
        if has_multiple_tags(item):
            score += 10
        else:
            score += 3

        scored_items.append({'item': item, 'score': score})

    # Sort by score descending
    scored_items.sort(key=lambda x: x['score'], reverse=True)

    # Take top items ensuring geographic diversity
    selected = []
    international_count = 0
    domestic_count = 0

    for scored_item in scored_items:
        item = scored_item['item']

        # Ensure balance
        if item['region'] == 'International' and international_count < 3:
            selected.append(item)
            international_count += 1
        elif item['region'] == 'China' and domestic_count < 2:
            selected.append(item)
            domestic_count += 1

        if len(selected) >= 5:
            break

    return selected
```

## Writing Guidelines

### Summary Writing

**For Each News Item**:
```yaml
Structure:
  - Headline: 20-40 characters, company + action + key point
  - Summary: 2-3 sentences, 150-250 characters
    * Sentence 1: What happened (facts)
    * Sentence 2: Key details (numbers, timeline, specs)
    * Sentence 3: Why it matters (impact, significance)

Tone:
  - Professional but accessible
  - Objective and factual
  - Engaging without hype
  - Technical accuracy with layman explanations

Example_Good:
  **OpenAI发布GPT-5，参数规模达10万亿**

  OpenAI正式推出第五代大语言模型GPT-5，参数量达到10万亿，较GPT-4提升50倍，支持文本、图像、音频和视频的多模态处理。该模型将于2025年第二季度通过API向开发者开放，定价为每1000个token 0.03美元。CEO Sam Altman表示，GPT-5在推理能力和实时交互方面实现了重大突破，标志着向AGI迈出重要一步。

Example_Bad:
  **OpenAI新模型**

  OpenAI发布了新模型。这个模型很厉害。
```

### 引导语 (Opening Hook)

**Purpose**: Engage readers immediately with week's highlights

```yaml
Structure:
  - 2-3 sentences
  - Mention 1-2 biggest stories
  - Create sense of momentum/progress
  - Invite reader to explore details

Good_Example:
  > 本周AI领域迎来重磅消息：OpenAI发布GPT-5，参数规模突破10万亿；NVIDIA第三季度营收创历史新高，同比增长206%；国内百度文心一言用户突破1亿。从技术突破到商业化加速，AI行业正在经历前所未有的变革期。

Bad_Example:
  > 本周有很多科技新闻。请阅读下面的内容。
```

### Section Transitions

Add natural transitions between sections:

```markdown
Good:
## 🇨🇳 国内科技动态

在国际AI巨头加速创新的同时，中国AI产业同样展现出强劲增长势头。本周国内焦点集中在...

## 🌍 国际科技动态

### AI前沿突破

Bad:
## 🇨🇳 国内科技动态

[Immediately starts listing news items]
```

## Responsibilities (v4.0)

**This Skill Does**:
- ✅ Load validated.json data
- ✅ Select 5 focus highlights based on scoring algorithm
- ✅ Categorize items by geography or theme
- ✅ Write engaging, accessible summaries
- ✅ Generate article structure (sections, headings)
- ✅ Create opening hook (引导语)
- ✅ Add ending sections (disclaimer, preview, subscription) from template
- ✅ Output well-structured markdown draft

**This Skill Does NOT Do**:
- ❌ Compliance optimization (→ formatter)
- ❌ Sensitive keyword substitution (→ formatter)
- ❌ Punctuation normalization (→ formatter)
- ❌ Grammar/semantic refinement (→ formatter)
- ❌ Title optimization (→ formatter)
- ❌ Final quality checks (→ formatter)

## Output Format

```markdown
# 本周AI科技动态 | 2025年11月12日-11月18日

> **引导语**
>
> 本周AI领域迎来重磅消息：OpenAI发布GPT-5，参数规模突破10万亿；NVIDIA第三季度营收创历史新高，同比增长206%；国内百度文心一言用户突破1亿。从技术突破到商业化加速，AI行业正在经历前所未有的变革期。

## 🌟 48小时焦点

> 快速浏览48小时最重要的科技动态

1. **🇺🇸 OpenAI发布GPT-5，参数达10万亿**
   OpenAI正式推出第五代大语言模型，多模态能力全面升级，预计Q2通过API开放，标志着向AGI迈出重要一步。

2. **🇺🇸 NVIDIA Q3营收181亿美元，同比增长206%**
   得益于AI芯片需求激增，NVIDIA第三季度业绩创历史新高，H100和Blackwell系列供不应求，数据中心业务占比达80%。

3. **🇨🇳 百度文心一言用户突破1亿**
   百度宣布文心一言注册用户超过1亿，日活跃用户达2000万，成为中国用户规模最大的AI应用，显著领先竞争对手。

4. **🌍 Anthropic获Amazon 50亿美元追加投资**
   Anthropic完成新一轮50亿美元融资，由Amazon领投，公司估值达200亿美元，资金将用于Claude模型训练和基础设施建设。

5. **📜 欧盟AI法案正式生效，全球首部综合性AI监管法规落地**
   欧盟人工智能法案正式实施，建立基于风险的分级监管体系，对高风险AI应用提出严格要求，预计将影响全球AI产业格局。

---

## 🇨🇳 国内科技动态

在国际AI巨头加速创新的同时，中国AI产业同样展现出强劲增长势头。本周国内焦点集中在商业化突破、技术进展和产业投资三大领域。

### AI应用商业化

**1. 百度文心一言用户突破1亿，日活2000万领跑国内**

[Detailed summary with 2-3 sentences, key data, impact]

**2. 阿里通义千问企业版发布，主打B端市场**

[Summary...]

### 技术研发进展

**3. 商汤发布"日日新5.5"大模型，性能提升40%**

[Summary...]

### 产业投资动态

**4. 深圳发布AI产业扶持政策，3年投入100亿**

[Summary...]

---

## 🌍 国际科技动态

### AI模型与技术突破

**1. OpenAI发布GPT-5，参数规模达10万亿**

[Full detailed summary with 3 sentences, all key data]

**2. Google Gemini 2.0发布，多模态性能显著提升**

[Summary...]

### 科技巨头财报与业绩

**3. NVIDIA Q3营收181亿美元，同比增长206%**

[Summary...]

**4. Microsoft Azure AI业务营收同比增长100%**

[Summary...]

### AI芯片与硬件

**5. NVIDIA发布Blackwell Ultra，性能再提升2倍**

[Summary...]

### 投资并购动态

**6. Anthropic获Amazon 50亿美元追加投资**

[Summary...]

---

## 📜 全球政策监管

**1. 欧盟AI法案正式生效，全球首部综合性AI监管法规落地**

[Summary with neutral tone, cite official sources]

**2. 美国政府发布AI安全框架，要求企业报告训练数据**

[Summary...]

---

## 📋 免责声明

本报告基于2025年11月12日至11月18日的公开信息整理，数据来源包括官方公告和主流科技媒体（TechCrunch、Bloomberg、Reuters等）。所有财务数据仅供参考，不构成投资建议。技术规格、产品信息及行业预测以公司官方最终公告为准，实际发展可能存在差异。

---

**📅 下期预告**

重点关注：
- Microsoft Ignite大会（11月18-21日）
- Alibaba Q2财报（11月25日）
- AI行业年终总结与2026展望

---

**🔔 订阅提示**

关注本公众号，每日获取精选AI科技新闻，不错过重要动态！

---

**生成信息**
- 来源: tech_news_20251120_validated.json
- 生成时间: 2025-11-20 17:00:00 CST
- 内容项: 42 (原始45，合并3组重复)
- 版本: wechat-tech-news-writer v4.0.0 (draft)
- 状态: DRAFT - Awaiting formatting optimization
- 下一步: daily-tech-news-formatter (合规、标点、语法、标题优化)
```

## Integration with v4.0 Workflow

### Workflow Handoff

```yaml
After_Writing:
  Output_File: tech_news_[DATE]_wechat_draft.md
  Word_Count: ~6500-7500 words (before optimization)
  Status: DRAFT - Content complete, formatting pending
  
  Next_Step:
    Skill: daily-tech-news-formatter
    Input: tech_news_[DATE]_wechat_draft.md
    Expected: Multi-round optimization (compliance, punctuation, grammar, titles)
    Final: tech_news_[DATE]_wechat_final.md
```

## Reference Documentation

- **[domestic_international.md](assets/templates/domestic_international.md)** - Geographic structure template
- **[theme_based.md](assets/templates/theme_based.md)** - Theme-based structure template
- **[focus_highlights.md](assets/templates/focus_highlights.md)** - Focus section examples

## Performance Expectations

```
Component                    Time        Output
─────────────────────────────────────────────────
Load validated data          ~30s        Parse JSON
Focus highlights selection   ~1 min      Score and select 5 items
Content categorization       ~1 min      Group by geography/theme
Summary writing              3-4 min     Write engaging narratives for 42 items
Structure generation         ~1 min      Format sections and headings
Add ending sections          ~30s        Apply template
─────────────────────────────────────────────────
Total                        5-8 min     6500-7500 word draft
```

---

**Version**: 4.0.0
**Role**: Pure content writing engine
**Input**: tech_news_[DATE]_validated.json
**Output**: tech_news_[DATE]_wechat_draft.md (unoptimized)
**Philosophy**: Focus on narrative and structure - let formatter handle compliance/optimization