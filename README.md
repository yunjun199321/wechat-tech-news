# WeChat Tech News Plugin

> **Complete automated workflow for daily tech news → WeChat Official Account publication**

[![Version](https://img.shields.io/badge/version-4.0.0-blue.svg)](https://github.com/your-org/wechat-tech-news/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/claude--code-%3E%3D1.0.0-purple.svg)](https://claude.ai/code)

## Installation

This is a **Claude Code Plugin** that can be installed with simple commands!

### Install via Marketplace (Recommended)

**Step 1: Add the Marketplace**
```
/plugin marketplace add your-org/wechat-tech-news
```

**Step 2: Install the Plugin**
```
/plugin install wechat-tech-news@your-org
```

Or use the interactive menu:
```
/plugin
```
Then browse and select "wechat-tech-news" to install.

**Step 3: Verify Installation**
```
/help
```
You should see the new skills available.

### Manual Installation (Local Development)

```bash
# Clone to Claude plugins directory
cd ~/.claude/plugins/marketplaces/
git clone https://github.com/your-org/wechat-tech-news.git

# Add as local marketplace
/plugin marketplace add ./wechat-tech-news

# Install from local marketplace
/plugin install wechat-tech-news@wechat-tech-news
```

## Features

### ✅ One-Command Complete Workflow

```
使用 wechat-tech-news skill
```

**Automatically** (5-Phase Pipeline):
1. 🔍 **Collection**: Searches ~50 tech news items (AI + Tech giants)
2. ✓ **Validation**: Verifies through 5 quality rounds with hardcoded rules
3. ✍️ **Writing**: Transforms into WeChat article structure
4. 🎨 **Formatting**: Multi-round optimization (compliance + grammar + punctuation)
5. 📄 **Export**: Generates markdown + optional Word document

**Time**: 30-45 minutes | **Output**: Publication-ready markdown + Word doc

---

### 🔍 Skill 1: daily-tech-news-search (Phase 1: Collection)

**Pure data collection engine**

- Uses `/sc:research --depth exhaustive --strategy unified`
- Targets 45-55 raw news items from major companies
- Product-focused search (60% products, 30% activities, 10% investment)
- Includes community sources: Product Hunt, Hacker News, GitHub Trending
- Basic AI keyword filtering only (deep validation delegated to Phase 2)

**Coverage**: OpenAI, Anthropic, Google, Microsoft, Meta, NVIDIA, Tesla, Alibaba, Tencent, Baidu, ByteDance, Huawei, and more

**Usage**:
```
使用 daily-tech-news-search skill
```

---

### ✅ Skill 2: daily-tech-news-validator (Phase 2: Validation)

**Hardcoded validation engine with mandatory quality gates**

- **5 Validation Rounds**:
  1. Source credibility (domain whitelist/blacklist, 7-10/10)
  2. Time accuracy (strict 48h window, China timezone UTC+8)
  3. AI relevance (keyword matching + exclusion patterns)
  4. Deduplication (similarity detection, ≥95% unique)
  5. Quality assurance (completeness, geographic balance)
- **Round 6 (NEW v4.1)**: Content type classification for 60/30/10 ratio
- Generates `validation_report.md` with pass/fail gates
- Outputs validated JSON (40-45 items)

**Usage**:
```
使用 daily-tech-news-validator skill [raw-file]
```

---

### ✍️ Skill 3: wechat-tech-news-writer (Phase 3: Content Writing)

**Pure content writing engine (NO formatting or compliance)**

- **Structure Creation**:
  - 🇨🇳/🌍 Domestic/International categorization
  - 🎯 Theme-based alternative structure
  - 🌟 "48小时焦点" Focus Highlights (5 headline items)

- **WeChat Elements**:
  - 引导语 (opening hook)
  - 目录 (table of contents)
  - 互动引导 (engagement prompts)
  - 相关阅读 (related reading)

- **Note**: Compliance optimization delegated to Phase 4 (Formatter)
- Outputs unoptimized draft: `tech_news_[DATE]_wechat_draft.md`

**Usage**:
```
使用 wechat-tech-news-writer skill [validated-json]
```

---

### 🎨 Skill 4: daily-tech-news-formatter (Phase 4: Multi-Round Optimization)

**Systematic content optimization with 5 rounds**

- **Round 1**: WeChat compliance (100+ sensitive keyword substitutions, 3-tier risk 🔴🟡🟢)
- **Round 2**: Grammar refinement (readability, flow, transitions)
- **Round 3**: Punctuation normalization (Chinese standards: 。，、：；！？)
- **Round 4**: Title enhancement (clickability, SEO optimization)
- **Round 5**: Final polish (consistency check, formatting cleanup)

- Generates `format_report.md` with before/after comparisons
- Outputs publication-ready: `tech_news_[DATE]_wechat_final.md`

**Usage**:
```
使用 daily-tech-news-formatter skill [draft-file]
```

---

### 🔄 Skill 5: wechat-tech-news (Phase 5: Orchestration)

**End-to-end automation orchestration**

**Pipeline**:
```
Initialize → Collection (P1) → Validation (P2) →
Writing (P3) → Formatting (P4) → Export (P5) → Output
```

**Features**:
- Five-phase execution with quality gates between ALL phases
- Phase-specific error recovery and automatic retry
- Comprehensive execution metadata in `workflow_[DATE].json`
- Customizable parameters for each phase

**Usage**:
```
使用 wechat-tech-news skill [options]

Options:
  --date DATE          Override auto date
  --count N            Target item count (default: 50)
  --structure TYPE     Force structure type
  --skip-phase1        Use existing research
  --compliance LEVEL   strict|normal|lenient
```

## Quick Start

### First Time Setup

1. **Install Plugin** (see above)
2. **Create Output Directory**:
   ```bash
   mkdir -p ~/my-code/ResearchLab/daily_news/docs/research
   mkdir -p ~/my-code/ResearchLab/daily_news/metadata
   ```
3. **Test Installation**:
   ```
   使用 wechat-tech-news skill --help
   ```

### Daily Routine

**Morning (9 AM China time)**:
```
使用 wechat-tech-news skill
```

**30 minutes later**:
1. Open `tech_news_[DATE]_wechat.md`
2. Review compliance flags
3. Copy content
4. Paste into WeChat Official Account editor
5. Publish!

## Configuration

Plugin settings can be customized in Claude Code:

**Settings → Plugins → wechat-tech-news → Configure**

```json
{
  "outputDirectory": "daily_news/docs/research",
  "defaultItemCount": 50,
  "defaultStructure": "domestic_international",
  "complianceLevel": "normal"
}
```

## Output Files

Each run generates:

1. **tech_news_[DATE]_raw.md**
   - 50 verified news items
   - Full verification details
   - Source credibility scores
   - Compliance flags

2. **tech_news_[DATE]_wechat.md**
   - Publication-ready WeChat article
   - 6000-8000 words
   - All compliance optimizations applied
   - Ready to copy-paste

3. **workflow_[DATE].json**
   - Execution metadata
   - Quality metrics
   - Performance tracking

## Requirements

### Required

- **Claude Code**: Latest stable version
- **MCP Server**: Tavily (or alternative web search)
- **Command**: `/sc:research` availability

### Optional

- **Serena MCP**: For project memory (recommended)

## Manage Plugin

**List installed plugins**:
```
/plugin list
```

**Uninstall plugin**:
```
/plugin uninstall wechat-tech-news
```

**Update plugin**:
```
/plugin update wechat-tech-news
```

## Performance

**Typical Execution**:
- Time: 25-40 minutes (average: 30 min)
- Items found: 45-55
- Quality score: 7.8-8.5/10
- Compliance flags: 10-15%
- Word count: 6500-7500

**Resource Usage**:
- Network: ~80-100 URLs fetched
- Storage: ~500 KB per day
- Memory: Peak ~300 MB

## Quality Metrics

```
Metric                  Target    Typical
─────────────────────────────────────────
Items Found             50        45-55
Quality Score           ≥7.0      7.8-8.5
Source Credibility      ≥7.0      7.5-8.0
Completeness            ≥7.0      7.8-8.5
Deduplication Rate      ≥95%      96-98%
Compliance Flags        <20%      10-15%
Publication Readiness   ≥80%      85-90%
```

## Troubleshooting

### Plugin Not Appearing

**Solution**:
1. Check if marketplace is added:
   ```
   /plugin marketplace list
   ```
2. If not, add the marketplace:
   ```
   /plugin marketplace add your-org/wechat-tech-news
   ```
3. Verify marketplace JSON is valid:
   ```bash
   cat ~/.claude/plugins/marketplaces/wechat-tech-news/.claude-plugin/marketplace.json
   ```

### Skills Not Loading

**Solution**:
1. Verify plugin is installed:
   ```
   /plugin list
   ```
2. Reinstall if needed:
   ```
   /plugin uninstall wechat-tech-news
   /plugin install wechat-tech-news@your-org
   ```
3. Check each skill has `SKILL.md`:
   ```bash
   ls ~/.claude/plugins/marketplaces/wechat-tech-news/skills/*/SKILL.md
   ```

### MCP Server Error

**Solution**:
1. Check Tavily MCP is installed
2. Verify in Settings → MCP Servers
3. Alternative: Use different web search MCP

## Documentation

- **[README.md](README.md)** - This file
- **[daily-tech-news-search/SKILL.md](daily-tech-news-search/SKILL.md)** - Research methodology
- **[daily-tech-news-validator/SKILL.md](daily-tech-news-validator/SKILL.md)** - Validation engine
- **[wechat-tech-news-writer/SKILL.md](wechat-tech-news-writer/SKILL.md)** - Content writing
- **[daily-tech-news-formatter/SKILL.md](daily-tech-news-formatter/SKILL.md)** - Multi-round optimization
- **[wechat-tech-news/SKILL.md](wechat-tech-news/SKILL.md)** - Workflow orchestration

### Reference Guides

- **[search_queries.md](daily-tech-news-search/references/search_queries.md)** - Search customization
- **[verification_process.md](daily-tech-news-search/references/verification_process.md)** - Quality control (deprecated in v4.0)
- **[validation_rules.md](daily-tech-news-validator/references/validation_rules.md)** - Hardcoded validation rules
- **[compliance_guidelines.md](wechat-tech-news-writer/references/compliance_guidelines.md)** - Compliance rules
- **[sensitive_keywords.md](wechat-tech-news-writer/references/sensitive_keywords.md)** - Keyword database
- **[engagement_tactics.md](wechat-tech-news-writer/references/engagement_tactics.md)** - Audience engagement
- **[punctuation_guide.md](daily-tech-news-formatter/references/punctuation_guide.md)** - Chinese punctuation standards

## Use Cases

### 📰 Daily Tech News
Run workflow daily, publish to WeChat Official Account

### 📊 Weekly Roundup
Collect 5-7 days, combine best items, format once

### 🎯 Topic Focus
Customize search queries for AI-only, chips-only, etc.

### 🌐 Bilingual Content
Use raw results for English, WeChat version for Chinese

## Support

- **Issues**: [GitHub Issues](https://github.com/your-org/wechat-tech-news/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/wechat-tech-news/discussions)
- **Email**: support@wechat-tech-news.dev

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - see [LICENSE](LICENSE) file

## Changelog

- ✨ Initial release
- ✨ Three core skills: search, writer, workflow
- ✨ 5-round verification system
- ✨ 100+ compliance keyword database
- ✨ Complete end-to-end automation
- ✨ One-click plugin installation

---

**Plugin Homepage**: https://github.com/your-org/wechat-tech-news
**Claude Code Marketplace**: Search "wechat-tech-news"
**Version**: 4.0.0 | **License**: MIT | **Status**: Production Ready ✅
