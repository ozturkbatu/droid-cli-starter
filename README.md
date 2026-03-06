# Droid CLI Starter

A standardized, batteries-included starter kit for [Factory Droid CLI](https://docs.factory.ai/). This repository provides a pre-configured environment for AI-powered development, designed to be cloned and adapted for any new project.

## Project Goal
The goal of this repository is to provide a consistent **Agentic Workflow** foundation. It codifies best practices for AI agents, including specialized sub-agents (Droids), reusable capabilities (Skills), and automated safeguards (Hooks).

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/ozturkbatu/droid-cli-starter.git

# 2. Install dependencies (Prettier, Black, JQ for hooks)
npm install

# 3. Start a Droid session
droid
```

## AI Agent Infrastructure
This project uses the .factory/ directory to define how AI agents interact with your code.

# Specialized Droids
Located in .factory/droids/, these are sub-agents with specific system prompts and tool access:

- Code Reviewer: A read-only specialist for quality and security audits.
- Security Auditor: Focuses on vulnerability scanning and secret detection.
- Git Manager: Handles staging, conventional commits, and GitHub PR creation.
- Task Coordinator: Breaks down complex features into multi-step checklists with progress tracking.

# Reusable Skills
Standardized workflows located in .factory/skills/:

- /code-review: Review code for quality and adherence to project conventions.
- /feature-implementation: Step-by-step guidance for building new functionality.
- /git-commit-push: Automates staging, conventional commit messages, and pushing.

# Automated Hooks
Lifecycle events configured in .factory/settings.json to ensure code quality:

- Pre-Tool Validation: Checks for sensitive data (API keys, .env files) before edits are allowed.
- Post-Tool Formatting: Automatically runs Prettier (TS/JS), Black (Python), or JQ (JSON) after an agent modifies a file.
- Command Logging: Maintains an audit trail of all shell commands executed by the agent.
- Memory Capture: Automatically saves user prompts starting with # to the project's permanent memory.

## Project Structure

```
.
├── AGENTS.md              # The "Source of Truth" briefing for AI agents
├── SKILLS.md              # Documentation for available agent capabilities
├── .factory/
│   ├── droids/            # Custom agent definitions (system prompts + toolsets)
│   ├── skills/            # Procedural workflows for specific tasks
│   ├── rules/             # Codified standards for TS, Testing, and Security
│   ├── hooks/             # Automation scripts (formatting, validation, logging)
│   ├── memories.md        # Permanent record of architecture decisions
│   └── settings.json      # Hook triggers and local configuration
└── src/
```

# Best Practices for This Template
## For Developers
- Codify your Rules: Add project-specific patterns to .factory/rules/ to stop Droid from making the same mistakes repeatedly.
- Use the Task Coordinator: For complex features, ask Droid to "use the task-coordinator" to see a live TODO list of its progress.
- Check the Logs: View the command history log to see exactly what commands the agent ran.

## For AI Agents
- Read AGENTS.md: This is your primary instruction set for this repository.
- Follow the Rules: Adhere to the specific conventions in .factory/rules/ for TypeScript, Testing, and Security.
- Document Decisions: Use the # prefix to save important architecture choices to .factory/memories.md.

# Documentation References
- [Factory Documentation]([url](https://docs.factory.ai/))
- [GitHub Integration Guide]([url](https://www.google.com/search?q=./.factory/github-integration-guide.md))
- [Hooks Reference]([url](https://www.google.com/search?q=./.factory/hooks/README.md))
