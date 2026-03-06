# Marketitive Skills Documentation

Skills are reusable capabilities that extend what agents can do. Each skill is a directory under `.factory/skills/` containing a `SKILL.md` file with instructions and optional supporting files.

## Available Skills

### Code Review
- **Location**: `.factory/skills/code-review/`
- **Purpose**: Review code changes for quality, security, and best practices
- **Usage**: Invoke with `/code-review` or let the agent use automatically

### Feature Implementation
- **Location**: `.factory/skills/feature-implementation/`
- **Purpose**: Implement new features following project conventions
- **Usage**: Describe the feature and the agent will follow the workflow

### Git Commit & Push
- **Location**: `.factory/skills/git-commit-push/`
- **Purpose**: Automated Git workflow - stage, commit, and push to GitHub
- **Usage**: Say "commit and push" or invoke with `/git-commit-push`

## Creating New Skills

1. Create a directory under `.factory/skills/<skill-name>/`
2. Add a `SKILL.md` file with:
   - YAML frontmatter (name, description)
   - Instructions for the agent
   - Success criteria
3. Add optional supporting files (schemas, checklists, etc.)

## Skill Best Practices

- Keep skills narrow and outcome-focused
- Define clear success criteria
- Make inputs and requirements explicit
- Include verification steps
- Reference existing documentation instead of duplicating

## Invocation Control

Use frontmatter to control who can invoke skills:

- `user-invocable: true` (default): User can invoke with `/skill-name`
- `disable-model-invocation: true`: Only user can invoke (prevents automatic use)
- `user-invocable: false`: Only agent can invoke (background knowledge)

## Example Skill Structure

```
.factory/skills/
  ├─ code-review/
  │  ├─ SKILL.md              # Main skill definition
  │  └─ checklist.md          # Optional supporting file
  ├─ feature-implementation/
  │  ├─ SKILL.md
  │  └─ templates/
  │     └─ component.ts       # Optional templates
```

For more information, see the [Factory Skills Documentation](https://docs.factory.ai/cli/configuration/skills).
