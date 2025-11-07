#!/bin/bash

# WeChat Tech News Plugin Verification Script
# Checks plugin structure and dependencies

set -e

PLUGIN_DIR="$HOME/.claude/plugins/marketplaces/wechat-tech-news"
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔍 Verifying WeChat Tech News Plugin..."
echo ""

# Function to check file existence
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        return 0
    else
        echo -e "${RED}✗${NC} $2 (missing: $1)"
        return 1
    fi
}

# Function to check directory existence
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        return 0
    else
        echo -e "${RED}✗${NC} $2 (missing: $1)"
        return 1
    fi
}

# Function to validate JSON
validate_json() {
    if python3 -m json.tool "$1" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} $2 (valid JSON)"
        return 0
    else
        echo -e "${RED}✗${NC} $2 (invalid JSON)"
        return 1
    fi
}

ERRORS=0

# Check plugin directory
echo "📁 Plugin Directory Structure"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_dir "$PLUGIN_DIR" "Plugin root directory" || ((ERRORS++))
check_dir "$PLUGIN_DIR/.claude-plugin" "Metadata directory" || ((ERRORS++))
echo ""

# Check metadata files
echo "📋 Metadata Files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_file "$PLUGIN_DIR/.claude-plugin/plugin.json" "plugin.json" || ((ERRORS++))
check_file "$PLUGIN_DIR/.claude-plugin/marketplace.json" "marketplace.json" || ((ERRORS++))

if [ -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]; then
    validate_json "$PLUGIN_DIR/.claude-plugin/plugin.json" "plugin.json syntax" || ((ERRORS++))
fi

if [ -f "$PLUGIN_DIR/.claude-plugin/marketplace.json" ]; then
    validate_json "$PLUGIN_DIR/.claude-plugin/marketplace.json" "marketplace.json syntax" || ((ERRORS++))
fi
echo ""

# Check documentation
echo "📚 Documentation Files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_file "$PLUGIN_DIR/README.md" "README.md" || ((ERRORS++))
check_file "$PLUGIN_DIR/LICENSE" "LICENSE" || ((ERRORS++))
check_file "$PLUGIN_DIR/CONTRIBUTING.md" "CONTRIBUTING.md" || ((ERRORS++))
check_file "$PLUGIN_DIR/INSTALL_GUIDE.md" "INSTALL_GUIDE.md" || ((ERRORS++))
echo ""

# Check skills
echo "🎯 Skills"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

SKILLS=("daily-tech-news-search" "wechat-tech-news-writer" "tech-news-workflow")

for skill in "${SKILLS[@]}"; do
    check_dir "$PLUGIN_DIR/$skill" "$skill directory" || ((ERRORS++))
    check_file "$PLUGIN_DIR/$skill/SKILL.md" "$skill/SKILL.md" || ((ERRORS++))
done
echo ""

# Check skill references and assets
echo "📎 Skill Resources"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# daily-tech-news-search references
check_dir "$PLUGIN_DIR/daily-tech-news-search/references" "Search references" || ((ERRORS++))
check_file "$PLUGIN_DIR/daily-tech-news-search/references/search_queries.md" "Search queries reference" || ((ERRORS++))
check_file "$PLUGIN_DIR/daily-tech-news-search/references/verification_process.md" "Verification process reference" || ((ERRORS++))

# wechat-tech-news-writer references and assets
check_dir "$PLUGIN_DIR/wechat-tech-news-writer/references" "Writer references" || ((ERRORS++))
check_dir "$PLUGIN_DIR/wechat-tech-news-writer/assets" "Writer assets" || ((ERRORS++))
check_file "$PLUGIN_DIR/wechat-tech-news-writer/references/compliance_guidelines.md" "Compliance guidelines" || ((ERRORS++))
check_file "$PLUGIN_DIR/wechat-tech-news-writer/references/sensitive_keywords.md" "Sensitive keywords database" || ((ERRORS++))
check_file "$PLUGIN_DIR/wechat-tech-news-writer/references/engagement_tactics.md" "Engagement tactics" || ((ERRORS++))
echo ""

# Check plugin.json content
echo "🔧 Plugin Configuration"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]; then
    # Extract plugin name
    PLUGIN_NAME=$(python3 -c "import json; print(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json'))['name'])" 2>/dev/null || echo "unknown")
    echo -e "Plugin Name: ${GREEN}$PLUGIN_NAME${NC}"

    # Extract version
    VERSION=$(python3 -c "import json; print(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json'))['version'])" 2>/dev/null || echo "unknown")
    echo -e "Version: ${GREEN}$VERSION${NC}"

    # Check skills array
    SKILL_COUNT=$(python3 -c "import json; print(len(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json')).get('skills', [])))" 2>/dev/null || echo "0")
    echo -e "Skills defined: ${GREEN}$SKILL_COUNT${NC}"

    if [ "$SKILL_COUNT" -eq 3 ]; then
        echo -e "${GREEN}✓${NC} All 3 skills registered"
    else
        echo -e "${RED}✗${NC} Expected 3 skills, found $SKILL_COUNT"
        ((ERRORS++))
    fi
fi
echo ""

# Check dependencies
echo "🔗 Dependencies"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if Tavily MCP is mentioned
if grep -q "tavily" "$PLUGIN_DIR/.claude-plugin/plugin.json" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Tavily MCP dependency declared"
else
    echo -e "${YELLOW}⚠${NC} Tavily MCP dependency not found in plugin.json"
fi

# Check if /sc:research is mentioned
if grep -q "/sc:research" "$PLUGIN_DIR/.claude-plugin/plugin.json" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} /sc:research command dependency declared"
else
    echo -e "${YELLOW}⚠${NC} /sc:research dependency not found in plugin.json"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ Verification passed!${NC}"
    echo ""
    echo "Plugin is ready for:"
    echo "  1. Local installation (restart Claude Code)"
    echo "  2. Distribution (run ./package.sh)"
    echo "  3. Marketplace submission"
    echo ""
    echo "Next steps:"
    echo "  - Run: ./package.sh to create distribution ZIP"
    echo "  - Restart Claude Code to load the plugin"
    echo "  - Enable in Settings → Plugins"
else
    echo -e "${RED}❌ Verification failed with $ERRORS error(s)${NC}"
    echo ""
    echo "Please fix the errors above before proceeding."
    exit 1
fi
