---
name: wechat-tech-news-writer
description: Transform tech news into WeChat Official Account articles with compliance optimization, headline selection, domestic/international categorization, and focus highlights. Use when creating or optimizing tech news content for WeChat publication, especially when handling sensitive content like government policies, US-China tech competition, or financial data.
---

# WeChat Tech News Writer

## Overview

Transform raw tech news into polished WeChat Official Account articles optimized for Chinese readers. Automatically handles content structure, compliance filtering, and engagement optimization while maintaining journalistic standards.

## When to Use This Skill

Invoke this skill when:
- Creating WeChat Official Account tech news articles
- Optimizing tech news for Chinese social media platforms
- Handling sensitive content (政策监管、芯片禁令、中美科技竞争)
- Converting company-categorized news to theme-based or geographic structure
- Adding engagement elements (焦点板块、引导语、互动元素)

## Core Capabilities

### 1. Content Structure Optimization

**Geographic Categorization (国内/国外分类)**

Reorganize news from company-based structure to geographic structure:

```markdown
## 🇨🇳 国内科技动态
### AI投资热潮
### 研发支出
### 人才争夺战
### 市场表现
### 行业趋势

## 🌍 国际科技动态
### AI前沿
### 科技巨头财报
### 芯片与半导体
### 创业投资
### 量子计算

## 📜 全球政策监管（独立板块）
```

**Benefits:**
- Matches Chinese reader preferences
- Easier geographic news navigation
- Clearer domestic-international comparison
- Better sensitive content management

**Theme-Based Categorization (主题分类)**

Alternative structure focusing on topics rather than companies:

```markdown
## 🤖 AI公司动态
### 政府与企业合作
### 企业营收与市场表现
### 产品与技术发布
### AI应用与普及
### 融资与投资
### 监管与争议
```

**Benefits:**
- Cross-company collaborations highlighted
- Industry trends more visible
- Easier to follow technology evolution

### 2. Focus Highlights (本周焦点)

Create 3-5 headline news items at the article beginning:

**Format:**
```markdown
## 🌟 本周焦点

> 快速浏览本周最重要的科技动态

1. **🇺🇸 [地域标识] [简短标题]**
   一句话核心信息，突出影响和意义。

2. **🇨🇳 [地域标识] [简短标题]**
   一句话核心信息，突出影响和意义。
```

**Selection Criteria:**
- High impact (政策变化、重大投资、技术突破)
- Cross-domain influence (影响多个行业)
- Reader interest (中国读者关注度高)
- Geographic balance (国内外各半)
- Controversy level (适度争议提高传播)

**Examples:**
- 政府AI投资计划（高影响 + 政策性）
- 万亿级企业投资（高金额 + 行业影响）
- 技术突破（量子计算商用、芯片制程突破）
- 市值里程碑（NVIDIA 5万亿、马斯克财富）
- 监管新规（AI未成年人保护、隐私法案）

### 3. Compliance Optimization (合规性优化)

#### Sensitive Content Categories

**🔴 High Risk (需要重点调整):**

| 原表述 | 优化表述 | 原因 |
|--------|----------|------|
| "五角大楼AI合同" | "美国政府AI研发合作" | 避免军事敏感性 |
| "中国禁用美国AI芯片" | "政策鼓励国产AI加速器应用" | 中性化贸易政策 |
| "诱导儿子自残" | "加强未成年人保护" | 淡化负面案例 |
| "中美科技竞争" | "国际科技格局调整" | 避免对抗性表述 |

**🟡 Medium Risk (需要注意表述):**

| 类别 | 注意事项 | 优化方法 |
|------|----------|----------|
| 金融数据 | 大额融资、市值变化 | 添加免责声明 |
| 政策监管 | 国内外政策法规 | 保持客观中立 |
| 市场预测 | 行业趋势预判 | 标注为"预测"或"分析" |
| 公司业绩 | 财报数据、增长率 | 注明数据来源 |

**🟢 Low Risk (正常报道):**

- 产品发布
- 技术进展
- 企业合作
- 融资信息
- 人才招聘

#### Compliance Checklist

Before publishing, verify:

- [ ] 敏感词汇已中性化
- [ ] 军事相关内容已淡化
- [ ] 未成年人相关内容平衡报道
- [ ] 金融数据已添加免责声明
- [ ] 政策内容保持客观中立
- [ ] 避免使用"暴涨""狂跌"等情绪化词汇
- [ ] 数据来源已标注

### 4. WeChat-Specific Elements

**Required Components:**

1. **引导语 (Opening Hook)**
   ```markdown
   > 本周科技圈风云变幻，AI投资创新高，量子计算迎来商用元年，
   > 监管政策持续加码。让我们一起回顾本周最重要的科技动态。
   ```

2. **目录 (Table of Contents)**
   - 支持锚点跳转
   - 分国内/国外或按主题
   - Emoji图标增强可读性

3. **免责声明 (Disclaimer)**
   ```markdown
   **免责声明**

   *本报告基于2025年XX月XX日的公开信息整理，数据来源包括官方公告、
   主流媒体报道和行业分析。所有投资相关信息仅供参考，不构成投资建议。*
   ```

4. **相关阅读 (Related Reading)**
   ```markdown
   **相关阅读推荐**

   - [上周科技新闻汇总](链接)
   - [AI行业深度分析](链接)
   - [芯片产业趋势报告](链接)
   ```

5. **互动引导 (Engagement)**
   - 文末提问引导评论
   - 鼓励分享转发
   - 订阅号关注引导

**Formatting Guidelines:**

- **总字数**: 控制在8000字以内
- **段落**: 每段不超过200字
- **标题**: 使用Emoji增强视觉效果
- **引用**: 使用引用块突出重点
- **数据**: 使用表格或列表呈现
- **链接**: 使用Markdown格式便于点击

### 5. Tone and Style

**Writing Principles:**

- **客观中立**: 事实为主，避免主观评价
- **简洁明了**: 一句话说清核心信息
- **数据支持**: 用数字说话，增强可信度
- **中文表达**: 符合中文阅读习惯
- **避免专业术语**: 必要时解释专业概念

**Language Optimization:**

✅ **Good Examples:**
- "NVIDIA市值达5万亿美元" (具体数据)
- "量子计算进入商用元年" (行业趋势)
- "政策鼓励国产芯片应用" (中性表述)

❌ **Avoid:**
- "NVIDIA股价暴涨" (情绪化)
- "中国禁用美国芯片" (对抗性)
- "诱导儿童自残" (负面渲染)

## Workflow

### Standard Workflow

1. **分析原始新闻**
   - 识别新闻主题和地域分布
   - 评估敏感内容风险
   - 确定目标读者群体

2. **选择结构方案**
   - 国内/国外分类 (推荐用于微信)
   - 主题分类 (适合专业读者)
   - 混合方案 (大型汇总)

3. **创建焦点板块**
   - 选择3-5条最重要新闻
   - 每条新闻一句话总结
   - 添加地域标识emoji

4. **合规性检查**
   - 识别高风险内容
   - 应用优化表述
   - 添加必要免责声明

5. **添加微信元素**
   - 撰写引导语
   - 生成目录结构
   - 添加免责声明
   - 插入相关阅读

6. **最终检查**
   - 字数控制
   - 格式统一
   - 链接有效性
   - 阅读流畅度

### Quick Reference: Structure Templates

Access pre-built templates in `assets/templates/`:

- `domestic_international.md` - 国内/国外分类模板
- `theme_based.md` - 主题分类模板
- `focus_highlights.md` - 焦点板块示例

## Resources

### references/

- `compliance_guidelines.md` - 完整的微信公众号合规指南
- `sensitive_keywords.md` - 敏感词汇替换对照表
- `engagement_tactics.md` - 提高互动率的技巧

### assets/

- `templates/domestic_international.md` - 国内/国外分类模板
- `templates/theme_based.md` - 主题分类模板
- `templates/focus_highlights.md` - 焦点板块模板

## Best Practices

### Do's ✅

- 优先使用国内/国外分类（符合中国读者习惯）
- 焦点板块放在开头（提高完读率）
- 政策内容独立板块（便于审核管理）
- 敏感内容中性化表述
- 添加免责声明（金融数据必须）
- 引导语增强互动性

### Don'ts ❌

- 不使用对抗性语言（中美竞争→格局调整）
- 不过度渲染负面案例
- 不使用情绪化词汇（暴涨→上涨）
- 不忽略数据来源标注
- 不超过8000字限制
- 不遗漏合规检查步骤

## Examples

See `daily_news/docs/research/tech_news_20251107_demo.md` for a complete example of WeChat-optimized tech news article.

**Key Features Demonstrated:**
- 🌟 Focus highlights (5 headline news)
- 🇨🇳/🌍 Domestic/International categorization
- 📜 Separate policy section
- ✅ Compliance-optimized language
- 📱 WeChat-specific elements
