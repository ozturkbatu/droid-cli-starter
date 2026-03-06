#!/usr/bin/env bash
#
# Auto-format code files after editing or creation
# This hook runs after Edit and Create tool calls
#
# Usage: Configure in .factory/settings.json under PostToolUse hook

set -euo pipefail

# Read JSON input from stdin
input=$(cat)

# Extract file path from the tool input
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

if [ -z "$file_path" ]; then
  exit 0
fi

# Format TypeScript/JavaScript files
if [[ "$file_path" =~ \.(ts|tsx|js|jsx)$ ]]; then
  if command -v npx &> /dev/null; then
    npx prettier --write "$file_path" 2>&1 || echo "Warning: Prettier formatting failed for $file_path"
  fi
fi

# Format Python files
if [[ "$file_path" =~ \.py$ ]]; then
  if command -v black &> /dev/null; then
    black "$file_path" 2>&1 || echo "Warning: Black formatting failed for $file_path"
  fi
fi

# Format JSON files
if [[ "$file_path" =~ \.json$ ]]; then
  if command -v jq &> /dev/null; then
    temp_file=$(mktemp)
    jq '.' "$file_path" > "$temp_file" && mv "$temp_file" "$file_path" || rm -f "$temp_file"
  fi
fi

exit 0
