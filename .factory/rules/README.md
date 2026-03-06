# Coding Rules and Conventions

This directory contains codified standards that Droid follows consistently. Unlike memories (which capture decisions), rules define **how code should be written**.

## Available Rules

- **typescript.md** - TypeScript conventions and patterns
- **testing.md** - Testing standards and best practices
- **security.md** - Security requirements and validation

## How Rules Work

1. Droid reads these files before working on code
2. Referenced in AGENTS.md for context
3. Can be enforced with hooks (automatic linting, formatting)

## Rules vs Other Configuration

| Type | Purpose | Example |
|------|---------|---------|
| **Rules** | How code should be written | "Use early returns" |
| **Memory** | What was decided and why | "We chose Zustand because..." |
| **AGENTS.md** | How to build/test/run | "Run `npm test`" |
| **Skills** | How to do specific tasks | "Steps to implement API endpoint" |

## Writing Effective Rules

Each rule should be:
- ✅ **Specific**: Clear without interpretation
- ✅ **Actionable**: Tells what to do, not just avoid
- ✅ **Scoped**: States when it applies
- ✅ **Justified**: Explains why (for complex rules)

## Rule Template

```markdown
## [Rule Name]
**Applies to**: [file types, contexts]
**Rule**: [specific instruction]
**Example**: [code showing correct usage]
**Rationale**: [why this matters - optional]
```

## Organization Patterns

### For Teams
```
.factory/rules/
├── _base/           # Foundation (everyone follows)
│   ├── typescript.md
│   └── security.md
├── frontend/        # Frontend-specific
│   ├── react.md
│   └── styling.md
└── backend/         # Backend-specific
    ├── api.md
    └── database.md
```

### For Solo Projects
```
.factory/rules/
├── typescript.md
├── testing.md
└── security.md
```

## Maintenance

### Adding New Rules
When you find yourself correcting Droid repeatedly:
1. Identify the pattern
2. Write a clear rule with examples
3. Add to appropriate rules file
4. Test by asking Droid to do similar work

### Quarterly Review
- [ ] Remove rules enforced by linting
- [ ] Update changed rules
- [ ] Add rules for new patterns
- [ ] Verify examples are accurate

## Automatic Enforcement

Use hooks to enforce rules automatically:
- PostToolUse hook: Run linters after edits
- PostToolUse hook: Auto-format with Prettier
- PreToolUse hook: Validate before edits

See `.factory/hooks/` for examples.

## References

- [Factory Rules Guide](https://docs.factory.ai/guides/power-user/rules-conventions)
- [Setup Checklist](https://docs.factory.ai/guides/power-user/setup-checklist)
