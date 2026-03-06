# Marketitive

AI-powered marketing platform built with agentic workflow patterns.

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## AI Agent Configuration

This project is configured for optimal AI agent collaboration using Factory Droid patterns.

### Key Configuration Files

- **AGENTS.md** - Main briefing file for AI agents with project conventions
- **SKILLS.md** - Documentation of available agent skills and capabilities
- **.factory/** - Agent configuration directory with skills, droids, and hooks

### Working with AI Agents

The project includes several pre-configured skills for common workflows:

- **Code Review** (`/code-review`) - Review changes for quality and security
- **Feature Implementation** (`/feature-implementation`) - Build new features following standards

### Automated Workflows (Hooks)

The following automation runs automatically:
- Code formatting after file edits
- Validation before commits
- Command logging for audit trail

See `.factory/README.md` for detailed configuration.

## Project Structure

```
Marketitive/
├── AGENTS.md              # AI agent briefing
├── SKILLS.md              # Skills documentation
├── README.md              # This file
├── .factory/              # Agent configuration
│   ├── skills/            # Reusable capabilities
│   ├── droids/            # Custom agent definitions
│   ├── hooks/             # Automation scripts
│   └── settings.json      # Local configuration
├── src/                   # Application source
├── public/                # Static assets
└── tests/                 # Test files
```

## Development Workflow

### For Developers

1. Read `AGENTS.md` to understand project conventions
2. Use AI agents for code review, testing, and implementation
3. Invoke skills with `/skill-name` or let agents use them automatically
4. Follow the established patterns and conventions

### For AI Agents

1. Read `AGENTS.md` before starting work
2. Use skills from `.factory/skills/` when applicable
3. Follow hooks configured in `.factory/settings.json`
4. Provide evidence for all changes (tests, lint, type checks)

## Contributing

When contributing:
1. Create a feature branch from `main`
2. Follow conventions in `AGENTS.md`
3. Run tests and linting before committing
4. Provide clear PR description with evidence
5. Request code review

## Documentation

- [AGENTS.md](./AGENTS.md) - Agent briefing and conventions
- [SKILLS.md](./SKILLS.md) - Available skills
- [.factory/README.md](./.factory/README.md) - Agent configuration details
- [Factory Documentation](https://docs.factory.ai/) - Full Factory guide

## License

[Add your license here]
