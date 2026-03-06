# Marketitive Agent Configuration

This file serves as a briefing packet for AI coding agents working on the Marketitive project.

## Core Commands

• Install dependencies: `npm install`
• Type-check and lint: `npm run lint`
• Auto-fix style: `npm run lint:fix`
• Run tests: `npm test`
• Start dev server: `npm run dev`
• Build for production: `npm run build`

## Project Layout

```
├─ src/           → Application source code
├─ public/        → Static assets
├─ tests/         → Test files
├─ .factory/      → Agent configuration and workflows
│  ├─ skills/     → Reusable agent capabilities
│  ├─ droids/     → Custom agent definitions
│  └─ hooks/      → Automation scripts
```

## Coding Standards

Follow the conventions documented in `.factory/rules/`:
- **TypeScript**: `.factory/rules/typescript.md` - Type definitions, patterns, imports
- **Testing**: `.factory/rules/testing.md` - Test structure, mocking, coverage
- **Security**: `.factory/rules/security.md` - Input validation, auth, secrets

When working on a file, check the relevant rules first.

### Coding Style (Quick Reference)
• Use TypeScript with strict mode enabled
• Follow ESLint and Prettier configurations
• Use meaningful variable and function names
• Keep functions small and focused (single responsibility)
• Write tests for new features and bug fixes

### Git Workflow
1. Branch from `main` with descriptive names: `feature/<name>` or `fix/<name>`
2. Run `npm run lint` before committing
3. Keep commits atomic with clear messages
4. Never force-push to `main`
5. Request code review before merging

### Architecture
• Follow the existing folder structure
• Keep business logic separate from UI components
• Use TypeScript interfaces for data structures
• Document complex logic with comments

## Evidence Required for Pull Requests

A PR is ready for review when it includes:

- All tests passing (`npm test`)
- Lint and type checks passing (`npm run lint`)
- One-paragraph description of changes
- For bug fixes: test demonstrating the fix
- For features: new tests covering the feature
- No secrets or sensitive data in code

## Memory & Context

Project history, architecture decisions, and domain knowledge are documented in:
- **Project Memory**: `.factory/memories.md` - Architecture decisions, learnings, technical debt
- **Personal Memory**: `~/.factory/memories.md` - Your preferences and coding style (optional)

**Quick Capture**: Start your message with `#` to save to project memory, or `##` for personal memory.

## External Services & Dependencies

• Document any new external APIs or services here
• List required environment variables
• Note any third-party integrations

## Security

• Never commit sensitive data (API keys, passwords, tokens)
• Validate all user inputs
• Follow security best practices for authentication
• Review dependencies for known vulnerabilities

## Gotchas & Known Issues

• Document any known issues or workarounds here
• List any technical debt that should be addressed
• Note any platform-specific considerations
