# Marketitive AI Agent Configuration

This directory contains the configuration and workflow patterns for AI coding agents working on the Marketitive project.

## Directory Structure

```
.factory/
├── README.md              # This file
├── settings.json          # Local project settings (hooks configuration)
├── memories.md            # Project memory (decisions, context, learnings)
├── skills/                # Reusable agent capabilities
│   ├── code-review/       # Code review skill
│   │   └── SKILL.md
│   └── feature-implementation/  # Feature implementation skill
│       └── SKILL.md
├── droids/                # Custom agent definitions
│   ├── README.md
│   ├── code-reviewer.md   # Read-only code review agent
│   ├── security-auditor.md # Security analysis agent
│   └── task-coordinator.md # Multi-step task coordinator
├── rules/                 # Coding conventions (NEW!)
│   ├── README.md
│   ├── typescript.md      # TypeScript conventions
│   ├── testing.md         # Testing standards
│   └── security.md        # Security requirements
└── hooks/                 # Automation scripts
    ├── README.md          # Hooks documentation
    ├── format-code.sh     # Auto-format code after edits
    ├── validate-commit.py # Validate changes before commits
    ├── log-commands.sh    # Log executed commands
    └── memory-capture.py  # Automatic memory capture
```

## Key Files

### AGENTS.md (project root)
The main briefing file for AI agents. Contains:
- Core commands (install, test, build)
- Project layout
- Coding style and conventions
- Git workflow
- Security guidelines
- PR requirements

### SKILLS.md (project root)
Documentation for available skills and how to create new ones.

### Skills Directory
Contains reusable agent capabilities:
- **code-review**: Review code for quality, security, and conventions
- **feature-implementation**: Implement new features following standards

Each skill has:
- `SKILL.md` with instructions and success criteria
- Optional supporting files (templates, checklists, schemas)

### Hooks Directory
Automation scripts that run at specific lifecycle events:
- **format-code.sh**: Auto-formats TypeScript/JavaScript/Python files
- **validate-commit.py**: Checks for sensitive data and validates changes
- **log-commands.sh**: Logs all executed commands for audit

Hooks are configured in `.factory/settings.json`.

### Droids Directory
Custom agent definitions for specialized tasks. Each droid is a `.md` file with:
- System prompts tailored to specific workflows
- Tool access control (read-only, edit, execute, etc.)
- Model preferences
- Specific capabilities and constraints

**Included Examples**:
- **code-reviewer.md**: Read-only reviewer focused on quality and security
- **security-auditor.md**: Security-focused analysis with web search capability
- **task-coordinator.md**: Multi-step task execution with progress tracking

## Getting Started

### For Developers

1. **Read AGENTS.md** in the project root to understand conventions
2. **Review SKILLS.md** to see available capabilities
3. **Use skills** by typing `/skill-name` or letting the agent invoke them automatically
4. **Check hooks** in `.factory/hooks/` to understand automation

### For AI Agents

1. Read `AGENTS.md` for project context and conventions
2. Use skills from `.factory/skills/` when relevant
3. Follow hooks configured in `.factory/settings.json`
4. Reference this directory structure when creating new files

## Customization

### Adding New Skills

1. Create directory: `.factory/skills/<skill-name>/`
2. Add `SKILL.md` with YAML frontmatter and instructions
3. Document in `SKILLS.md`

### Adding New Hooks

1. Create script in `.factory/hooks/`
2. Make it executable: `chmod +x script.sh`
3. Add configuration to `.factory/settings.json`
4. Document in `.factory/hooks/README.md`

### Creating Custom Droids

1. Create `.md` file in `.factory/droids/`
2. Define frontmatter (name, model, tools)
3. Write system prompt
4. Use with the Task tool

## Best Practices

### For Skills
- Keep skills narrow and focused
- Define clear success criteria
- Include verification steps
- Make requirements explicit

### For Hooks
- Always use absolute paths
- Validate inputs carefully
- Never expose secrets
- Test in safe environment
- Include timeouts

### For AGENTS.md
- Keep concise (≤150 lines recommended)
- Use concrete commands in backticks
- Update when workflows change
- Link to external docs instead of duplicating

## Documentation References

- [Factory AGENTS.md Guide](https://docs.factory.ai/cli/configuration/agents-md)
- [Skills Documentation](https://docs.factory.ai/cli/configuration/skills)
- [Hooks Guide](https://docs.factory.ai/cli/configuration/hooks-guide)
- [Custom Droids](https://docs.factory.ai/cli/configuration/custom-droids)

## Contributing

When adding new workflows or automation:
1. Document in appropriate README
2. Follow existing patterns
3. Test thoroughly
4. Update this README if structure changes
