---
name: wechat-tech-news-writer
description: Transform tech news into WeChat Official Account articles with compliance optimization, headline selection, and geographic categorization. Use when creating WeChat publication content, especially handling sensitive topics like government policies, US-China tech competition, or financial data.
---

# WeChat Tech News Writer

## When to Use This Skill

Use this skill when you need to:
- Transform raw tech news into WeChat Official Account articles
- Optimize content for Chinese social media compliance
- Handle sensitive content (政策监管、芯片禁令、中美科技竞争)
- Add engagement elements (焦点板块、引导语、互动元素)
- Convert company-based structure to geographic/theme-based organization

## Quick Start

```bash
使用 wechat-tech-news-writer skill [input-file]
```

**Execution Time**: 5-8 minutes
**Output**: `daily_news/docs/research/tech_news_[YYYYMMDD]_wechat.md`
**Word Count**: 6000-8000 words (publication-ready)

## Core Transformations

### 1. Structure Optimization

**Geographic Categorization** (国内/国外分类) - Recommended:
```markdown
## 🇨🇳 国内科技动态
### AI投资热潮 / 研发支出 / 人才争夺战 / 市场表现

## 🌍 国际科技动态
### AI前沿 / 科技巨头财报 / 芯片与半导体 / 创业投资

## 📜 全球政策监管 (独立板块)
```

**Theme-Based** (主题分类) - Alternative:
```markdown
## 🤖 AI公司动态
### 政府与企业合作 / 企业营收 / 产品发布 / 融资投资 / 监管争议
```

### 2. Focus Highlights (本周焦点)

Creates 3-5 headline news items at article beginning:

```markdown
## 🌟 本周焦点

> 快速浏览本周最重要的科技动态

1. **🇺🇸 [地域标识] [简短标题]**
   一句话核心信息,突出影响和意义。

2. **🇨🇳 [地域标识] [简短标题]**
   一句话核心信息,突出影响和意义。
```

**Selection Criteria**: High impact, cross-domain influence, reader interest, geographic balance

### 3. Compliance Optimization

**Risk Tiers**:

| Risk | Category | Action | Example |
|------|----------|--------|---------|
| 🔴 High | Military/Defense, US-China Confrontation | Must neutralize | 五角大楼 → 美国政府<br>中美对抗 → 国际格局调整 |
| 🟡 Medium | Financial Data, Policy Changes | Add disclaimers | 添加免责声明、注明来源 |
| 🟢 Low | Product Launches, Tech Progress | Normal reporting | 正常报道 |

**100+ Keyword Substitutions** - See [sensitive_keywords.md](references/sensitive_keywords.md)

### 4. WeChat-Specific Elements

**Required Components**:
1. **引导语** (Opening Hook) - Engaging 2-3 sentence summary
2. **目录** (Table of Contents) - Anchor links with emoji icons
3. **免责声明** (Disclaimer) - For financial data and policy content
4. **互动引导** (Engagement) - End-of-article prompts for comments/sharing
5. **相关阅读** (Related Reading) - Links to previous articles

## Compliance Checklist

Before publishing, verify:
- [ ] 敏感词汇已中性化 (Sensitive keywords neutralized)
- [ ] 军事相关内容已淡化 (Military content toned down)
- [ ] 未成年人相关内容平衡报道 (Minor-related content balanced)
- [ ] 金融数据已添加免责声明 (Financial disclaimers added)
- [ ] 政策内容保持客观中立 (Policy content neutral)
- [ ] 避免情绪化词汇 (Avoid "暴涨""狂跌" etc.)
- [ ] 数据来源已标注 (Data sources cited)

## Output Format

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

**免责声明**
*本报告基于[DATE]的公开信息...*

**相关阅读推荐**
- [上周科技新闻汇总](链接)
```

## Writing Principles

✅ **Good Practices**:
- 客观中立 (Objective, neutral tone)
- 简洁明了 (Concise, clear statements)
- 数据支持 (Data-driven)
- 中文表达 (Natural Chinese phrasing)

❌ **Avoid**:
- 情绪化语言 (Emotional language: "暴涨""狂跌")
- 对抗性表述 (Confrontational framing)
- 负面渲染 (Over-emphasizing negatives)
- 缺少来源 (Missing citations)

## Reference Documentation

- **[compliance_guidelines.md](references/compliance_guidelines.md)** - Complete WeChat compliance guide
- **[sensitive_keywords.md](references/sensitive_keywords.md)** - 100+ keyword substitution table
- **[engagement_tactics.md](references/engagement_tactics.md)** - Audience engagement strategies
- **[templates/domestic_international.md](assets/templates/domestic_international.md)** - Geographic structure template
- **[templates/theme_based.md](assets/templates/theme_based.md)** - Theme structure template
- **[templates/focus_highlights.md](assets/templates/focus_highlights.md)** - Focus section examples

## Integration

**Input**: Raw research output from `daily-tech-news-search` skill
**Output**: WeChat-optimized markdown ready for publication
**Handoff**: Final output for `tech-news-workflow` or direct use

---

**Version**: 1.0
**Performance**: 5-8 minutes processing, 6000-8000 words output
**Compliance**: 100+ keywords, 3-tier risk classification
