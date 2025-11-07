# Contributing to WeChat Tech News Plugin

感谢您对本项目的兴趣！

## 如何贡献

### 报告问题

如果您发现问题，请在 GitHub Issues 中提交：

1. 使用清晰的标题描述问题
2. 提供复现步骤
3. 包含预期行为和实际行为
4. 附上相关日志或截图

### 提交改进

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- **Skill 文档**：使用 Markdown YAML 前言格式
- **参考文档**：清晰的章节结构，包含示例
- **配置文件**：遵循 JSON Schema 规范
- **中文文档**：优先使用简体中文，技术术语保留英文

### Skill 开发指南

#### 添加新 Skill

1. 在插件目录创建新文件夹：`[skill-name]/`
2. 创建 `SKILL.md` 文件（必需）：

```yaml
---
name: skill-name
description: Brief description
---

# Skill Name

## When to Use This Skill
...

## Core Capabilities
...
```

3. 更新 `plugin.json` 的 `skills` 数组
4. 更新主 `README.md` 文档

#### 改进现有 Skill

1. 修改 `SKILL.md` 内容
2. 更新 `references/` 中的参考文档
3. 测试 Skill 功能
4. 更新版本号和更新日志

### 文档改进

- README.md：主要功能和快速开始
- SKILL.md：详细的 Skill 使用说明
- references/：深度参考和最佳实践
- assets/：模板和示例

### 测试

提交前请测试：

1. Skill 能否正常加载
2. 所有引用的命令和 MCP 服务是否可用
3. 输出格式是否符合预期
4. 中文和英文内容是否正确

### Pull Request 流程

1. 确保所有测试通过
2. 更新相关文档
3. 在 PR 描述中说明：
   - 改动内容
   - 改动原因
   - 测试结果
   - 相关 Issue（如有）

### 版本规范

遵循语义化版本：

- **Major (1.0.0)**: 破坏性变更
- **Minor (0.1.0)**: 新功能，向后兼容
- **Patch (0.0.1)**: Bug 修复

### 提交信息规范

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type**:
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 格式调整
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**:
```
feat(search): 添加量子计算新闻源

- 新增 IonQ, Rigetti 等量子计算公司
- 扩展搜索查询模板
- 更新验证标准

Closes #42
```

## 行为准则

- 尊重所有贡献者
- 建设性反馈
- 专注于改进项目
- 保持专业和友善

## 许可证

提交代码即表示您同意在 MIT 许可证下分发您的贡献。

## 问题？

如有疑问，请：

1. 查看现有 Issues
2. 阅读文档
3. 开启新 Discussion
4. 发送邮件至 support@wechat-tech-news.dev

感谢您的贡献！ 🎉
