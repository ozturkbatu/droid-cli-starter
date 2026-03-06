# Custom Droids (Subagents)

Custom droids are specialized AI agents defined as `.md` files. Each droid has its own system prompt, model preference, and tool access policy.

## Available Droids

### code-reviewer.md
**Purpose**: Focused code review for quality and security  
**Tools**: Read-only (Read, Grep, Glob, LS)  
**Model**: Inherits from session  
**Use Case**: Review PRs, diffs, or specific files without making changes

**Invoke**: Ask the main agent to "use the code-reviewer droid" or use the Task tool

### security-auditor.md
**Purpose**: Security-focused vulnerability analysis  
**Tools**: Read + WebSearch (for CVE lookup)  
**Model**: Inherits from session  
**Use Case**: Security audits, vulnerability scanning, secrets detection

**Invoke**: "Run security audit with the security-auditor droid"

### task-coordinator.md
**Purpose**: Multi-step task execution with progress tracking  
**Tools**: Read, Edit, Create, Execute, Search  
**Reasoning**: Medium effort  
**Use Case**: Complex features requiring multiple steps and coordination

**Invoke**: "Use task-coordinator to implement [feature]"

## Creating Your Own Droids

### 1. Create the File
Create `<name>.md` in this directory (`.factory/droids/`)

### 2. Add Frontmatter
```yaml
---
name: my-droid
description: What this droid does and when to use it
model: inherit  # or specific model like claude-sonnet-4-5-20250929
tools: read-only  # or ["Read", "Edit"] or "edit"
reasoningEffort: medium  # optional: low, medium, high
---
```

### 3. Write the System Prompt
The markdown body is the droid's system prompt:
```markdown
# My Droid

You are a specialist in [domain]. Your role is to [purpose].

## Instructions
1. Step one
2. Step two
...

## Guidelines
- Guideline 1
- Guideline 2
...
```

## Tool Categories

Instead of listing tools individually, you can use categories:

- `read-only`: Read, LS, Grep, Glob
- `edit`: Create, Edit, ApplyPatch
- `execute`: Execute
- `web`: WebSearch, FetchUrl
- `mcp`: Model Context Protocol tools (if configured)

Or specify exact tools:
```yaml
tools: ["Read", "Edit", "WebSearch"]
```

## Model Options

```yaml
model: inherit  # Use parent session's model (recommended)
model: claude-sonnet-4-5-20250929  # Specific model
model: custom:gpt-4o-mini  # BYOK custom model
```

See [pricing page](https://docs.factory.ai/pricing#pricing-table) for model IDs.

## Reasoning Effort

For models that support it (like Claude Sonnet):
```yaml
reasoningEffort: low    # Faster, less thorough
reasoningEffort: medium # Balanced
reasoningEffort: high   # Slower, more thorough
```

## Usage Patterns

### Via Main Agent
```
"Use the code-reviewer droid to review this PR"
"Run security-auditor on the authentication code"
"Have task-coordinator implement the user profile feature"
```

### Via Task Tool (Programmatic)
The main agent can invoke droids using the Task tool:
```
Task(
  subagent_type="code-reviewer",
  description="Review authentication changes",
  prompt="Check the auth.ts file for security issues"
)
```

## Design Tips

### Keep Droids Focused
✓ Single responsibility (review, audit, coordinate)  
✗ General-purpose "do everything" droid

### Define Clear Success Criteria
✓ "A complete review identifies all critical issues"  
✗ "Review the code"

### Limit Tools Appropriately
- **Read-only** for analysis/review droids
- **Edit** for implementation droids  
- **Execute** only when commands are needed
- **Web** for research/documentation lookup

### Write Clear Instructions
✓ Step-by-step process  
✓ Specific output format  
✓ Examples of good output  
✗ Vague instructions

### Include Context
- Reference AGENTS.md for conventions
- Link to relevant docs
- Explain domain-specific terms

## Example Structures

### Analysis Droid (Read-Only)
```yaml
---
name: analyzer
description: Analyzes code patterns and suggests improvements
model: inherit
tools: read-only
---

# Code Analyzer

You analyze code for patterns, anti-patterns, and optimization opportunities.

## Process
1. Read the specified files
2. Identify patterns (good and bad)
3. Suggest improvements with examples
4. Prioritize by impact

## Output Format
**Patterns Found**: ...
**Issues**: ...
**Recommendations**: ...
```

### Implementation Droid (Edit)
```yaml
---
name: feature-builder
description: Implements features following project patterns
model: inherit
tools: ["Read", "Edit", "Create", "Grep"]
---

# Feature Builder

You implement features following project conventions (see AGENTS.md).

## Process
1. Understand requirements
2. Read existing similar code
3. Create/edit files following patterns
4. Verify completeness

## Requirements
- Follow existing code style
- Add TypeScript types
- Include error handling
```

### Research Droid (Read + Web)
```yaml
---
name: tech-researcher
description: Researches technical solutions and best practices
model: inherit
tools: ["Read", "WebSearch", "Grep"]
reasoningEffort: high
---

# Tech Researcher

You research technical solutions and industry best practices.

## Process
1. Understand the question
2. Search for current best practices
3. Review project context
4. Synthesize recommendations

## Output
Provide researched solutions with sources.
```

## Validation

After creating a droid:
1. Check frontmatter is valid YAML
2. Verify tool names are correct
3. Test with `/droids` command in CLI
4. Invoke with a simple task

## Best Practices

✓ **Name clearly**: `security-auditor` not `droid1`  
✓ **Describe precisely**: When to use this droid  
✓ **Limit scope**: Focused > general-purpose  
✓ **Document output**: Expected response format  
✓ **Reference context**: Link to AGENTS.md, docs  
✓ **Test thoroughly**: Start simple, expand gradually

## Troubleshooting

**Droid not appearing**: Check YAML frontmatter syntax  
**Wrong tools used**: Verify tool names (case-sensitive)  
**Unexpected behavior**: Review system prompt clarity  
**Model errors**: Check model ID is valid

## References

- [Custom Droids Documentation](https://docs.factory.ai/cli/configuration/custom-droids)
- [AGENTS.md](../../AGENTS.md) - Project conventions
- [Skills vs Droids](https://docs.factory.ai/cli/configuration/skills#how-skills-differ-from-other-configuration)
