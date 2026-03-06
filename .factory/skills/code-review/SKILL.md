---
name: code-review
description: Review code changes for quality, security, correctness, and adherence to project conventions. Use when reviewing PRs, staged changes, or commits.
user-invokable: true
disable-model-invocation: false
---

# Code Review Skill

## Purpose

Perform thorough code reviews following team standards and best practices. Identify issues early and provide constructive feedback.

## When to Use

- Reviewing pull requests before merge
- Checking staged changes before commit
- Analyzing specific commits
- Security and quality audits

## Instructions

### 1. Understand the Context

- Read the change description or PR context
- Identify the purpose of the changes (bug fix, feature, refactor)
- Check related issue or ticket if mentioned

### 2. Review the Changes

Examine the code for:

- **Correctness**: Does the code do what it's supposed to do?
- **Security**: Are there any security vulnerabilities?
  - Input validation
  - Authentication/authorization
  - Data sanitization
  - Secrets or sensitive data exposure
- **Performance**: Are there any obvious performance issues?
- **Testing**: Are there adequate tests?
- **Code Quality**:
  - Follows project conventions (see AGENTS.md)
  - Proper error handling
  - Clear naming and documentation
  - No unnecessary complexity
- **Maintainability**: Is the code easy to understand and modify?

### 3. Check Technical Debt

- Identify any quick wins for improvement
- Flag areas that need future attention
- Suggest refactoring opportunities

### 4. Provide Feedback

Format your review as:

**Summary**: One-line overall assessment

**Findings**:
- 🔴 **Critical**: Issues that must be fixed (security, correctness)
- 🟡 **Important**: Issues that should be fixed (quality, maintainability)
- 🟢 **Suggestions**: Nice-to-have improvements
- ✅ **Strengths**: What was done well

**Action Items**:
- List specific changes needed
- Prioritize by importance
- Include code snippets or examples where helpful

### 5. Verification

Before completing the review:
- All critical security issues identified
- Test coverage assessed
- No secrets or sensitive data in changes
- Alignment with project conventions verified

## Success Criteria

A complete review includes:
1. Summary of changes and their purpose
2. Categorized findings (critical, important, suggestions)
3. Specific, actionable feedback
4. Recognition of good practices
5. Clear next steps for the developer

## Example Usage

```
/code-review

# Or let the agent invoke automatically when discussing code changes
"Review the changes in my PR"
"Check if this code is secure"
"What do you think of these changes?"
```

## References

- See AGENTS.md for project coding conventions
- Check existing tests for testing patterns
- Review previous PRs for examples
