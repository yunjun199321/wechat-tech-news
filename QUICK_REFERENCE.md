# WeChat Tech News Plugin - 快速参考

> **一页纸速查手册** - 打印或保存以便快速查阅

---

## 🚀 快速开始

### 安装插件

**添加 Marketplace**:
```
/plugin marketplace add your-org/wechat-tech-news
```

**安装插件**:
```
/plugin install wechat-tech-news@your-org
```

**验证**:
```
/help
```

### 一键完整工作流

```
使用 tech-news-workflow skill
```

⏱️ **时间**: 25-40 分钟
📄 **输出**: 2 个文件（原始 + 微信优化版）
📊 **内容**: ~50 条验证新闻

---

## 🎯 三个核心 Skills

### 1️⃣ Daily Tech News Search

**用途**: 搜索和验证科技新闻

```
使用 daily-tech-news-search skill
```

- ⏱️ 时间: 15-25 分钟
- 📊 输出: ~50 条验证新闻
- 🔍 搜索: AI 公司 + 科技巨头
- ✅ 验证: 5 轮质量检查

### 2️⃣ WeChat Tech News Writer

**用途**: 优化为微信公众号格式

```
使用 wechat-tech-news-writer skill [input-file]
```

- ⏱️ 时间: 5-10 分钟
- 📝 输出: 微信格式文章
- 🛡️ 合规: 100+ 关键词优化
- 🎨 结构: 国内/国际或主题分类

### 3️⃣ Tech News Workflow

**用途**: 端到端自动化编排

```
使用 tech-news-workflow skill [options]
```

**选项**:
- `--date DATE` - 指定日期
- `--count N` - 目标条数
- `--structure TYPE` - 结构类型
- `--compliance LEVEL` - 合规级别

---

## 📂 输出文件

### 默认位置
```
daily_news/docs/research/
├── tech_news_20251107_raw.md      # 原始结果
├── tech_news_20251107_wechat.md   # 微信版本
└── metadata/
    └── workflow_20251107.json     # 执行元数据
```

### 文件说明

| 文件 | 内容 | 用途 |
|------|------|------|
| `*_raw.md` | 50 条验证新闻 + 验证详情 | 原始数据、英文内容 |
| `*_wechat.md` | 微信优化文章（6000-8000 字） | 直接复制粘贴发布 |
| `workflow_*.json` | 执行元数据和质量指标 | 性能追踪 |

---

## 🔧 配置位置

**Claude Code 中**:
```
Settings → Plugins → wechat-tech-news → Configure
```

**默认配置**:
```json
{
  "outputDirectory": "daily_news/docs/research",
  "defaultItemCount": 50,
  "defaultStructure": "domestic_international",
  "complianceLevel": "normal"
}
```

---

## 📊 质量指标速查

| 指标 | 目标 | 优秀 |
|------|------|------|
| 条数 | 45-55 | 50 |
| 质量评分 | ≥7.0 | ≥8.5 |
| 来源可信度 | ≥7.0 | ≥8.5 |
| 去重率 | ≥95% | ≥97% |
| 合规标记 | <20% | <10% |

---

## 🔍 5 轮验证流程

```
原始搜索结果（~80-120 条）
    ↓
Round 1: 来源可信度（≥7/10）→ ~73 条
    ↓
Round 2: 日期验证（24h，UTC+8）→ ~63 条
    ↓
Round 3: 去重（≥95% 独特）→ ~52 条
    ↓
Round 4: 完整性（≥7/10）→ ~51 条
    ↓
Round 5: 质量关卡（平衡 + 合规）→ 50 条
    ↓
最终输出
```

---

## 🛡️ 合规优化要点

### 3 级风险分类

- 🔴 **高风险**: 军事/国防、未成年、政治敏感
  - **处理**: 中性化或移除

- 🟡 **中风险**: 金融投机、未验证声明
  - **处理**: 添加免责声明

- 🟢 **低风险**: 常规科技新闻
  - **处理**: 保持原样

### 关键词替换示例

| 原词 | 替换为 |
|------|--------|
| 军事合同 | 政府合作 |
| 贸易战 | 贸易政策调整 |
| 监控 | 安全技术 |
| 垄断 | 市场主导地位 |

---

## 📞 快速故障排除

### 问题 1: Marketplace 未添加

```
# 检查 marketplaces
/plugin marketplace list

# 添加 marketplace
/plugin marketplace add your-org/wechat-tech-news
```

### 问题 2: 插件未安装

```
# 检查已安装插件
/plugin list

# 安装插件
/plugin install wechat-tech-news@your-org
```

### 问题 3: Skills 不可用

```
# 重新安装
/plugin uninstall wechat-tech-news
/plugin install wechat-tech-news@your-org

# 验证
/help
```

### 问题 3: Tavily MCP 错误

```
Settings → MCP Servers → Tavily
→ 配置 API Key
```

### 问题 4: 输出目录不存在

```bash
mkdir -p ~/my-code/ResearchLab/daily_news/docs/research
mkdir -p ~/my-code/ResearchLab/daily_news/metadata
```

---

## 📚 文档快速导航

| 文档 | 内容 |
|------|------|
| [README.md](README.md) | 主要功能和概览 |
| [INSTALL_GUIDE.md](INSTALL_GUIDE.md) | 详细安装说明 |
| [RELEASE_NOTES.md](RELEASE_NOTES.md) | 版本更新日志 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献指南 |
| [daily-tech-news-search/SKILL.md](daily-tech-news-search/SKILL.md) | 搜索 Skill 详解 |
| [wechat-tech-news-writer/SKILL.md](wechat-tech-news-writer/SKILL.md) | 写作 Skill 详解 |
| [tech-news-workflow/SKILL.md](tech-news-workflow/SKILL.md) | 工作流详解 |

---

## 🎯 常用命令速查

### 插件管理

```
# 查看已安装插件
/plugin list

# 查看可用 marketplaces
/plugin marketplace list

# 更新插件
/plugin update wechat-tech-news

# 卸载插件
/plugin uninstall wechat-tech-news
```

### 手动安装

```bash
# 克隆仓库
cd ~/.claude/plugins/marketplaces/
git clone https://github.com/your-org/wechat-tech-news.git

# 添加本地 marketplace
```
在 Claude Code 中：
```
/plugin marketplace add ~/.claude/plugins/marketplaces/wechat-tech-news
/plugin install wechat-tech-news@wechat-tech-news
```

### 开发工具

```bash
# 验证插件结构
cd ~/.claude/plugins/marketplaces/wechat-tech-news
./verify.sh

# 创建分发包
./package.sh
```

---

## 🌟 使用技巧

### 技巧 1: 每日定时执行

建议在中国时间早上 9:00 执行，确保获取前一天全球新闻。

### 技巧 2: 批量处理

周末收集 5-7 天新闻，一次性生成周报：

```
使用 tech-news-workflow skill --count 350
```

### 技巧 3: 主题聚焦

编辑 `search_queries.md` 自定义搜索，专注特定领域（如仅 AI）。

### 技巧 4: 双语输出

- `*_raw.md`: 保留英文，用于国际受众
- `*_wechat.md`: 中文优化，用于微信公众号

### 技巧 5: 质量优先

如条数不足 50，降低 `--count` 保证质量：

```
使用 tech-news-workflow skill --count 40
```

---

## 📈 性能优化

### 提高速度

1. 使用更快的网络连接
2. 降低 `--count` 参数
3. 使用 `--skip-phase1` 重用现有研究

### 提高质量

1. 增加 `--count` 参数（如 60）获取更多选择
2. 设置 `--compliance strict` 严格合规
3. 手动审查 🔴 高风险标记

---

## 🆘 获取帮助

### 在线资源

- **Issues**: https://github.com/your-org/wechat-tech-news/issues
- **Discussions**: https://github.com/your-org/wechat-tech-news/discussions
- **Email**: support@wechat-tech-news.dev

### 社区

- 分享使用经验
- 提出改进建议
- 贡献代码和文档

---

## 📋 检查清单

### ✅ 安装前

- [ ] Claude Code 已安装
- [ ] 了解插件功能和用途
- [ ] 准备 Tavily API Key

### ✅ 安装时

- [ ] 选择安装方法（Marketplace/手动/ZIP）
- [ ] 完成安装步骤
- [ ] 重启 Claude Code
- [ ] 启用插件（Toggle ON）

### ✅ 首次使用

- [ ] 创建输出目录
- [ ] 配置 Tavily MCP
- [ ] 测试工作流
- [ ] 检查输出文件

### ✅ 日常使用

- [ ] 每日执行工作流
- [ ] 审查合规标记
- [ ] 复制微信版本
- [ ] 发布到公众号

---

**版本**: 1.0.0
**更新**: 2025-01-07
**许可**: MIT

---

**立即开始**:
```
使用 tech-news-workflow skill
```

📱 **30 分钟后即可发布！**
