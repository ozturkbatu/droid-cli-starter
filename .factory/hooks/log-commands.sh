#!/usr/bin/env bash
#
# Log shell commands executed by the agent
# This hook runs before Execute tool calls
#
# Usage: Configure in .factory/settings.json under PreToolUse hook

set -euo pipefail

# Create logs directory if it doesn't exist
log_dir="$HOME/.factory/logs"
mkdir -p "$log_dir"

# Read JSON input
input=$(cat)

# Extract the command
command=$(echo "$input" | jq -r '.tool_input.command // empty')

if [ -z "$command" ]; then
  exit 0
fi

# Log the command with timestamp
timestamp=$(date '+%Y-%m-%d %H:%M:%S')
log_file="$log_dir/command-history.log"

echo "[$timestamp] $command" >> "$log_file"

# Optional: Show a message to the user
# echo "Command logged to $log_file"

exit 0
