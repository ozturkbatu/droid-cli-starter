# Hooks Configuration

Hooks are automation scripts that execute at various points in the agent lifecycle. They provide deterministic control over agent behavior.

## Available Hooks

Hooks can be configured in `.factory/settings.json` or globally in `~/.factory/settings.json`.

### Hook Events

- **PreToolUse**: Runs before tool calls (can block them)
- **PostToolUse**: Runs after tool calls complete
- **UserPromptSubmit**: Runs when user submits a prompt
- **Notification**: Runs when agent sends notifications
- **Stop**: Runs when agent finishes responding
- **SessionStart**: Runs when a session starts
- **SessionEnd**: Runs when a session ends

## Example Hooks in This Directory

### format-code.sh
Automatically formats code files after creation or editing.

**Usage**: Configure in settings.json:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Create",
        "hooks": [
          {
            "type": "command",
            "command": "$FACTORY_PROJECT_DIR/.factory/hooks/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

### validate-commit.sh
Validates changes before commits.

### log-commands.sh
Logs executed commands for audit trail.

## Creating Custom Hooks

1. Create a script in this directory
2. Make it executable: `chmod +x script.sh`
3. Add configuration to `.factory/settings.json`
4. Test with `/hooks` command in the CLI

## Security Considerations

⚠️ **Important**: Hooks execute with your credentials and can access/modify any files. Always:
- Review hook code before adding
- Use absolute paths (prefer `$FACTORY_PROJECT_DIR`)
- Validate inputs
- Avoid exposing secrets
- Test in safe environment first

## Hook Script Requirements

- Must be executable
- Receive JSON input via stdin
- Exit codes:
  - 0: Success
  - 2: Blocking error (shows stderr to agent)
  - Other: Non-blocking error

## References

- [Hooks Guide](https://docs.factory.ai/cli/configuration/hooks-guide)
- [Hooks Reference](https://docs.factory.ai/reference/hooks-reference)
- [Hooks Cookbook](https://docs.factory.ai/guides/hooks/auto-formatting)
