#!/bin/bash

# WeChat Tech News Plugin Packaging Script
# Creates distribution ZIP for marketplace installation

set -e

PLUGIN_NAME="wechat-tech-news"
VERSION="1.0.0"
OUTPUT_DIR="dist"
ARCHIVE_NAME="${PLUGIN_NAME}-${VERSION}.zip"

echo "📦 Packaging ${PLUGIN_NAME} v${VERSION}..."

# Create dist directory
mkdir -p "${OUTPUT_DIR}"

# Remove old archives
rm -f "${OUTPUT_DIR}/${ARCHIVE_NAME}"

# Create temporary staging directory
STAGING_DIR=$(mktemp -d)
STAGE_PLUGIN="${STAGING_DIR}/${PLUGIN_NAME}"

echo "📁 Staging files..."

# Copy plugin structure
mkdir -p "${STAGE_PLUGIN}"
cp -r .claude-plugin "${STAGE_PLUGIN}/"
cp README.md LICENSE CONTRIBUTING.md "${STAGE_PLUGIN}/"

# Copy skills
for skill in daily-tech-news-search wechat-tech-news-writer tech-news-workflow; do
    echo "  - Copying ${skill}..."
    cp -r "${skill}" "${STAGE_PLUGIN}/"
done

# Create archive
echo "🗜️  Creating archive..."
cd "${STAGING_DIR}"
zip -r "${ARCHIVE_NAME}" "${PLUGIN_NAME}" -q

# Move to dist
mv "${ARCHIVE_NAME}" "${OLDPWD}/${OUTPUT_DIR}/"
cd "${OLDPWD}"

# Cleanup
rm -rf "${STAGING_DIR}"

# Calculate size
SIZE=$(du -h "${OUTPUT_DIR}/${ARCHIVE_NAME}" | cut -f1)

echo "✅ Package created successfully!"
echo ""
echo "📊 Package Details:"
echo "   Name: ${ARCHIVE_NAME}"
echo "   Size: ${SIZE}"
echo "   Location: ${OUTPUT_DIR}/${ARCHIVE_NAME}"
echo ""
echo "📤 Installation Instructions:"
echo "   1. Share the ZIP file with users"
echo "   2. Users extract to: ~/.claude/plugins/marketplaces/"
echo "   3. Restart Claude Code"
echo "   4. Enable plugin in Settings → Plugins"
echo ""
echo "🚀 Or users can install via marketplace (coming soon)"
