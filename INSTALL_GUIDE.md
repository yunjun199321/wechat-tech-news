# WeChat Tech News Plugin 安装指南

## 方法一：Marketplace 安装（推荐）

> **最简单的方式** - 使用官方 `/plugin` 命令

### 步骤

**1. 添加 Marketplace**

在 Claude Code 对话中输入：
```
/plugin marketplace add your-org/wechat-tech-news
```

**2. 安装插件**

方式 A - 使用命令直接安装：
```
/plugin install wechat-tech-news@your-org
```

方式 B - 使用交互菜单：
```
/plugin
```
然后浏览并选择 "wechat-tech-news" 进行安装。

**3. 验证安装**

```
/help
```

应该能看到新的 skills 列表，包括：
- `daily-tech-news-search`
- `wechat-tech-news-writer`
- `tech-news-workflow`

**4. 测试运行**

```
使用 tech-news-workflow skill
```

如果成功，将开始执行新闻搜索工作流（需要约 25-40 分钟）。

---

## 方法二：手动安装

> **适合高级用户或无法访问 Marketplace 的情况**

### 前置要求

- Claude Code 已安装
- 终端访问权限
- Git（如果从仓库克隆）

### 选项 A：从 GitHub 克隆

```bash
# 1. 进入 Claude 插件目录
cd ~/.claude/plugins/marketplaces/

# 2. 克隆仓库
git clone https://github.com/your-org/wechat-tech-news.git
```

**3. 添加为本地 Marketplace**

在 Claude Code 中：
```
/plugin marketplace add ~/.claude/plugins/marketplaces/wechat-tech-news
```

**4. 安装插件**
```
/plugin install wechat-tech-news@wechat-tech-news
```

**5. 验证**
```
/plugin list
```

### 选项 B：从 ZIP 包安装

```bash
# 1. 下载 ZIP 文件
# 从 GitHub Releases 下载 wechat-tech-news-1.0.0.zip

# 2. 解压到插件目录
unzip wechat-tech-news-1.0.0.zip -d ~/.claude/plugins/marketplaces/
```

**3. 添加为本地 Marketplace**

在 Claude Code 中：
```
/plugin marketplace add ~/.claude/plugins/marketplaces/wechat-tech-news
```

**4. 安装插件**
```
/plugin install wechat-tech-news@wechat-tech-news
```

### 选项 C：从源代码复制

```bash
# 1. 创建插件目录
mkdir -p ~/.claude/plugins/marketplaces/wechat-tech-news

# 2. 复制所有文件
cp -r /path/to/source/* ~/.claude/plugins/marketplaces/wechat-tech-news/
```

**3. 添加为本地 Marketplace**

在 Claude Code 中：
```
/plugin marketplace add ./wechat-tech-news
```

**4. 安装插件**
```
/plugin install wechat-tech-news@wechat-tech-news
```

---

## 验证安装

### 检查插件状态

**在 Claude Code 对话中输入**：

```
/plugin list
```

应该能看到 "wechat-tech-news" 在已安装插件列表中。

**查看可用的 Skills**：

```
/help
```

应该能看到三个新的 skills：
- `daily-tech-news-search`
- `wechat-tech-news-writer`
- `tech-news-workflow`

### 测试 Skills

#### 测试 1：Tech News Workflow（完整工作流）

```
使用 tech-news-workflow skill
```

**预期结果**：
- 执行时间：25-40 分钟
- 输出：两个文件
  - `tech_news_[DATE]_raw.md` - 原始搜索结果
  - `tech_news_[DATE]_wechat.md` - 微信优化版本

#### 测试 2：Daily Tech News Search（仅搜索）

```
使用 daily-tech-news-search skill
```

**预期结果**：
- 执行时间：15-25 分钟
- 输出：`tech_news_[DATE]_raw.md`
- 包含：~50 条验证过的新闻

#### 测试 3：WeChat Writer（仅优化）

```
使用 wechat-tech-news-writer skill tech_news_20251107_raw.md
```

**预期结果**：
- 执行时间：5-10 分钟
- 输出：`tech_news_20251107_wechat.md`
- 包含：微信公众号格式化内容

---

## 配置（可选）

### 默认配置

插件使用以下默认配置：

```json
{
  "outputDirectory": "daily_news/docs/research",
  "defaultItemCount": 50,
  "defaultStructure": "domestic_international",
  "complianceLevel": "normal"
}
```

### 自定义配置

**在 Claude Code 中**：

1. Settings → Plugins → wechat-tech-news
2. 点击 "Configure" ⚙️
3. 修改设置：

```json
{
  "outputDirectory": "my_custom_path/news",
  "defaultItemCount": 60,
  "defaultStructure": "theme_based",
  "complianceLevel": "strict"
}
```

4. 保存配置
5. 重启 Claude Code 使配置生效

### 配置说明

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `outputDirectory` | string | `daily_news/docs/research` | 输出文件存放目录 |
| `defaultItemCount` | number | `50` | 目标新闻条数 |
| `defaultStructure` | enum | `domestic_international` | 文章结构类型<br>`domestic_international` 或 `theme_based` |
| `complianceLevel` | enum | `normal` | 合规检查严格度<br>`strict`, `normal`, 或 `lenient` |

---

## 依赖检查

插件需要以下依赖：

### 必需依赖

1. **Tavily MCP Server**（Web 搜索）

   **检查是否已安装**：
   - Settings → MCP Servers
   - 查找 "tavily"

   **如未安装**：
   ```bash
   # 安装 Tavily MCP
   # 参考：https://docs.tavily.com/mcp-setup
   ```

2. **/sc:research 命令**（深度研究）

   **检查是否可用**：
   在 Claude Code 输入：
   ```
   /sc:research --help
   ```

   应返回帮助信息。

### 可选依赖

1. **Serena MCP**（项目记忆）
   - 用于存储工作流执行历史
   - 不是必需，但推荐使用

---

## 故障排除

### 问题 1：Marketplace 未添加

**症状**：无法安装插件，提示找不到 marketplace

**解决方案**：

```
# 1. 检查已添加的 marketplaces
/plugin marketplace list

# 2. 如果列表中没有，添加 marketplace
/plugin marketplace add your-org/wechat-tech-news

# 或使用本地路径（如果是手动克隆）
/plugin marketplace add ~/.claude/plugins/marketplaces/wechat-tech-news
```

### 问题 2：插件安装失败

**症状**：`/plugin install` 命令失败

**解决方案**：

```bash
# 1. 检查文件是否存在
ls ~/.claude/plugins/marketplaces/wechat-tech-news/.claude-plugin/marketplace.json

# 2. 验证 JSON 格式
cat ~/.claude/plugins/marketplaces/wechat-tech-news/.claude-plugin/marketplace.json | python3 -m json.tool

# 3. 重新添加 marketplace 并安装
```

在 Claude Code 中：
```
/plugin marketplace add your-org/wechat-tech-news
/plugin install wechat-tech-news@your-org
```

### 问题 3：Skills 不可用

**症状**：插件已安装但 `/help` 看不到 skills

**解决方案**：

```bash
# 1. 检查 SKILL.md 文件是否存在
ls ~/.claude/plugins/marketplaces/wechat-tech-news/*/SKILL.md

# 应显示 3 个文件：
# - daily-tech-news-search/SKILL.md
# - wechat-tech-news-writer/SKILL.md
# - tech-news-workflow/SKILL.md
```

在 Claude Code 中：
```
# 2. 重新安装插件
/plugin uninstall wechat-tech-news
/plugin install wechat-tech-news@your-org

# 3. 验证
/help
```

### 问题 3：MCP Server 错误

**症状**：执行时提示 Tavily MCP 不可用

**解决方案**：

1. **安装 Tavily MCP**：
   ```bash
   # 参考 Tavily 官方文档
   # https://docs.tavily.com/
   ```

2. **配置 API Key**：
   - 注册 Tavily 账号获取 API key
   - Settings → MCP Servers → Tavily
   - 输入 API key

3. **验证连接**：
   在 Claude Code 输入：
   ```
   Test Tavily MCP connection
   ```

### 问题 4：输出目录不存在

**症状**：执行失败，提示找不到输出目录

**解决方案**：

```bash
# 创建默认输出目录
mkdir -p ~/my-code/ResearchLab/daily_news/docs/research
mkdir -p ~/my-code/ResearchLab/daily_news/metadata

# 或修改配置使用其他目录
```

### 问题 5：权限错误

**症状**：无法写入文件

**解决方案**：

```bash
# 检查目录权限
ls -ld ~/my-code/ResearchLab/daily_news/

# 修复权限
chmod 755 ~/my-code/ResearchLab/daily_news/
chmod 755 ~/my-code/ResearchLab/daily_news/docs/
chmod 755 ~/my-code/ResearchLab/daily_news/docs/research/
```

---

## 卸载插件

### 使用命令卸载

在 Claude Code 中：
```
/plugin uninstall wechat-tech-news
```

### 完全删除（包括文件）

```bash
# 1. 先卸载插件
# 在 Claude Code 中：/plugin uninstall wechat-tech-news

# 2. 删除插件目录
rm -rf ~/.claude/plugins/marketplaces/wechat-tech-news

# 3. 移除 marketplace（可选）
# 在 Claude Code 中：/plugin marketplace remove your-org
```

---

## 更新插件

### 使用命令更新

在 Claude Code 中：
```
/plugin update wechat-tech-news
```

### 手动更新（Git）

```bash
# 1. 进入插件目录
cd ~/.claude/plugins/marketplaces/wechat-tech-news

# 2. 拉取最新代码
git pull origin main

# 3. 重新安装
# 在 Claude Code 中：
# /plugin uninstall wechat-tech-news
# /plugin install wechat-tech-news@wechat-tech-news
```

---

## 获取帮助

### 文档资源

- **README.md** - 主要功能和快速开始
- **USAGE_GUIDE.md** - 详细使用指南
- **SKILL.md 文件** - 各 Skill 的深度说明
  - `daily-tech-news-search/SKILL.md`
  - `wechat-tech-news-writer/SKILL.md`
  - `tech-news-workflow/SKILL.md`

### 在线支持

- **GitHub Issues**: [https://github.com/your-org/wechat-tech-news/issues](https://github.com/your-org/wechat-tech-news/issues)
- **GitHub Discussions**: [https://github.com/your-org/wechat-tech-news/discussions](https://github.com/your-org/wechat-tech-news/discussions)
- **Email**: support@wechat-tech-news.dev

### 社区

- 加入讨论：分享使用经验和最佳实践
- 报告问题：帮助改进插件
- 贡献代码：参考 [CONTRIBUTING.md](CONTRIBUTING.md)

---

**安装完成后，开始使用**：

```
使用 tech-news-workflow skill
```

30 分钟后，您将获得一篇可发布的微信公众号科技新闻文章！ 🎉
