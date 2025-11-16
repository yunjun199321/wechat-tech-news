# wechat-tech-news Marketplace 使用指南

## 📦 Marketplace 信息

**名称**: wechat-tech-news
**版本**: 1.0.0
**技能数量**: 3 个
**符合标准**: ✅ Claude Skills 官方标准 100% 合规

## 🚀 快速开始

### 安装方法

将整个 `wechat-tech-news` 目录复制到 Claude Code 的 plugins 目录：

```bash
# 目标位置
~/.claude/plugins/marketplaces/wechat-tech-news/
```

Claude Code 会自动识别并加载所有技能，**无需运行任何安装脚本**。

### 验证安装

安装后重启 Claude Code，在对话中输入：

```
使用 daily-tech-news-search 搜索今日科技新闻
```

如果技能加载成功，Claude 会自动调用该技能执行任务。

## 📚 包含的技能

### 1. daily-tech-news-search

**功能**: 自动化每日科技新闻搜索
**输出**: 约 50 条经过 5 轮验证的高质量科技新闻

**使用场景**:
- 收集每日科技新闻用于发布或分析
- 需要全面覆盖 AI 和科技公司动态
- 需要结构化、经过验证的新闻收集（而非原始搜索）
- 使用中国时区日期确保新闻时效性

**示例**:
```
使用 daily-tech-news-search 搜索今日科技新闻
搜索 2025年11月7日 的 AI 相关新闻
```

### 2. wechat-tech-news-writer

**功能**: 将科技新闻转换为微信公众号优化的文章
**特色**: 合规优化、标题精选、国内外分类、焦点突出

**使用场景**:
- 创建或优化用于微信发布的科技新闻内容
- 处理敏感内容（政府政策、中美科技竞争、金融数据等）
- 批量处理新闻条目并生成发布就绪的文章

**示例**:
```
使用 wechat-tech-news-writer 将搜索结果转换为微信文章
优化这些新闻条目为微信公众号格式
```

### 3. tech-news-workflow

**功能**: 端到端自动化工作流，结合前两个技能
**特色**: 一键从原始搜索到发布就绪的内容

**使用场景**:
- 需要完整的自动化流程（搜索 → 转换 → 优化）
- 每日定期生成科技新闻文章
- 节省手动协调多个技能的时间

**示例**:
```
使用 tech-news-workflow 生成今日科技新闻文章
执行完整的新闻搜集和编辑流程
```

## 🔧 依赖项

### 必需的 MCP 服务器

- **tavily** (必需): 用于网络搜索
- **serena** (可选): 用于会话持久化

### 必需的命令

- **/sc:research**: 深度研究命令

### 验证依赖

确保你的 Claude Code 配置中已启用这些 MCP 服务器和命令。

## 📁 目录结构

```
wechat-tech-news/
├── .claude-plugin/
│   ├── plugin.json           # 插件配置
│   └── marketplace.json      # Marketplace 配置
├── daily-tech-news-search/
│   └── SKILL.md              # 技能定义 (大写)
├── wechat-tech-news-writer/
│   └── SKILL.md              # 技能定义 (大写)
├── tech-news-workflow/
│   └── SKILL.md              # 技能定义 (大写)
├── README.md                 # 项目说明
├── INSTALL_GUIDE.md          # 安装指南
├── LICENSE                   # 许可证
└── USAGE.md                  # 本文件
```

## ✅ 标准合规性

本 Marketplace 100% 符合 Claude Skills 官方标准：

- ✅ 所有技能使用 `SKILL.md` (大写) 文件名
- ✅ 所有技能包含正确的 YAML frontmatter
- ✅ `name` 字段使用 hyphen-case 命名
- ✅ `name` 字段与目录名称匹配
- ✅ 包含完整的 `description` 字段
- ✅ plugin.json 和 marketplace.json 配置正确
- ✅ 依赖项声明完整
- ✅ 无需安装脚本（Claude Code 自动加载）

## 🔍 故障排除

### 技能未加载

1. 确认目录位置正确：`~/.claude/plugins/marketplaces/wechat-tech-news/`
2. 重启 Claude Code
3. 检查依赖项（tavily MCP、/sc:research 命令）

### 技能无法执行

1. 验证 tavily MCP 服务器已启用
2. 确认 /sc:research 命令可用
3. 检查网络连接

### 获取帮助

如遇问题，请检查：
- plugin.json 格式是否正确（JSON 语法）
- SKILL.md 文件是否存在（注意大写）
- 依赖的 MCP 服务器是否运行

## 📝 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

## 🤝 贡献

欢迎提出建议和改进！

---

**最后更新**: 2025-01-16
**验证状态**: ✅ 所有检查通过
**Claude Skills 合规性**: ✅ 100%
