---
name: feature-implementation
description: Implement new features following project architecture, testing, and documentation standards. Use when building new functionality from scratch.
user-invokable: true
disable-model-invocation: false
---

# Feature Implementation Skill

## Purpose

Guide the implementation of new features from specification to tested, documented code following project conventions.

## When to Use

- Building new features from user stories or requirements
- Adding new components or modules
- Extending existing functionality

## Instructions

### 1. Understand Requirements

- Read and clarify the feature specification
- Identify acceptance criteria
- List technical requirements and dependencies
- Note any constraints or edge cases

### 2. Plan the Implementation

Break down the feature into:
- Data models and types
- API endpoints or service methods (if applicable)
- UI components (if applicable)
- Business logic
- Tests
- Documentation

### 3. Follow Project Structure

Implement according to the project layout (see AGENTS.md):
- Place files in appropriate directories
- Use existing patterns and conventions
- Reuse existing components and utilities
- Follow naming conventions

### 4. Implement Core Logic

For each component:
- Write clear, maintainable code
- Add TypeScript types/interfaces
- Include error handling
- Add inline comments for complex logic
- Follow security best practices

### 5. Add Tests

Write tests that:
- Cover happy paths and edge cases
- Test error handling
- Verify business logic
- Are maintainable and clear
- Follow existing test patterns

### 6. Update Documentation

Document:
- Public APIs and interfaces
- Complex algorithms or business logic
- Configuration options
- Usage examples (if it's a component/utility)

### 7. Verification Checklist

Before marking complete:
- [ ] Code follows project conventions
- [ ] All tests pass (`npm test`)
- [ ] No linting errors (`npm run lint`)
- [ ] Types are correct (TypeScript checks pass)
- [ ] Error handling is comprehensive
- [ ] No security vulnerabilities introduced
- [ ] Documentation is updated
- [ ] Feature meets acceptance criteria

## Implementation Workflow

1. **Plan**: Review requirements → Break down tasks → Identify dependencies
2. **Code**: Implement logic → Add types → Handle errors
3. **Test**: Write tests → Run tests → Fix issues
4. **Review**: Self-review → Check conventions → Verify completeness
5. **Document**: Add comments → Update docs → Create examples

## Output Format

Provide a summary:

**Feature**: [Name]

**Implementation Summary**:
- Files created/modified
- Key components added
- Technical approach

**Testing**:
- Test coverage
- Test scenarios covered

**Next Steps**:
- Any remaining tasks
- Suggested improvements
- Known limitations

## Success Criteria

A complete implementation includes:
1. Working code that meets requirements
2. Comprehensive test coverage
3. Proper error handling
4. Type safety (TypeScript)
5. Clear documentation
6. Follows project conventions
7. All verification checks pass

## Example Usage

```
/feature-implementation

# Or describe the feature naturally:
"Implement a user profile page with avatar upload"
"Add authentication using JWT tokens"
"Create a data export feature"
```

## References

- See AGENTS.md for project structure and conventions
- Check existing features for implementation patterns
- Review testing documentation for test patterns
