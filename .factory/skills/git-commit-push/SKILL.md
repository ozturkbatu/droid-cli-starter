---
name: git-commit-push
description: Stage, commit, and push changes to GitHub with proper commit messages. Use when the user wants to commit and push changes.
user-invokable: true
disable-model-invocation: false
---

# Git Commit & Push Workflow

## Purpose

Automate the Git workflow: stage changes, create proper commit messages, and push to GitHub.

## When to Use

- User says "commit and push"
- User wants to save changes to GitHub
- After completing a feature or fix
- Before switching tasks

## Instructions

### 1. Check Current Status

Run `git status` to see:
- Which files are modified
- Which files are staged
- Current branch
- Behind/ahead of origin

### 2. Review Changes

Run `git diff` to see unstaged changes
Run `git diff --staged` to see staged changes

Summarize what changed for the user.

### 3. Stage Changes

Ask user which files to stage, or stage all:
- Specific files: `git add <file1> <file2>`
- All changes: `git add .`
- Interactive: `git add -p` (patch mode)

### 4. Create Commit Message

Follow **Conventional Commits** format:

**Format**: `<type>(<scope>): <description>`

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Formatting, no code change
- `refactor:` - Code restructuring
- `test:` - Adding or updating tests
- `chore:` - Maintenance, deps, config

**Rules:**
- Keep first line under 50 characters
- Use present tense ("add" not "added")
- Don't capitalize first letter
- No period at the end

**Examples:**
```
feat: add user authentication
fix: resolve login redirect issue
docs: update API documentation
refactor: simplify payment logic
test: add user service tests
```

**With scope:**
```
feat(auth): add JWT token validation
fix(api): handle null user responses
```

### 5. Commit

Execute: `git commit -m "<message>"`

If commits fail, check for:
- Pre-commit hooks running
- Empty commit (no changes staged)
- Commit message format issues

### 6. Push to Remote

Check current branch:
```bash
git branch --show-current
```

Push changes:
```bash
# If tracking is set up
git push

# First push on new branch
git push -u origin $(git branch --show-current)
```

Handle common issues:
- **Rejected push**: May need to pull first (`git pull --rebase`)
- **Diverged branches**: Resolve conflicts, then push
- **Force push** (be careful!): `git push --force-with-lease`

### 7. Confirm Success

Show:
- Commit SHA
- Branch pushed to
- Files changed summary
- Remote URL for viewing changes

### 8. Suggest Next Steps

If on feature branch:
- "Create PR? Run `/create-pr` or `gh pr create`"
- "View changes: <GitHub URL>"

If on main:
- "Changes pushed to main"
- "CI/CD may be running"

## Output Format

```
📝 Changes Summary
------------------
Modified: src/auth.ts, src/middleware/auth.ts
Added: tests/auth.test.ts

✅ Staged: 3 files

💬 Commit Message
-----------------
feat: add JWT authentication support

🚀 Pushed to origin/feature/auth
------------------
Commit: abc1234
Files: 3 changed, 245 insertions(+), 12 deletions(-)

🔗 View on GitHub:
https://github.com/username/repo/tree/feature/auth

📋 Next Steps:
• Create PR: gh pr create
• Or visit: https://github.com/username/repo/pull/new/feature/auth
```

## Error Handling

### Merge Conflicts

```
⚠️  Merge conflicts detected

Run: git pull --rebase
Resolve conflicts in marked files
Then: git add . && git rebase --continue
```

### Push Rejected

```
⚠️  Push rejected (non-fast-forward)

Your branch is behind 'origin/feature'.
Run: git pull --rebase
Then try pushing again.
```

### Nothing to Commit

```
ℹ️  No changes to commit

Working tree is clean.
All changes are already committed.
```

## Best Practices

✅ Review changes before committing  
✅ Write clear, descriptive commit messages  
✅ Keep commits focused (one logical change)  
✅ Pull before pushing to avoid conflicts  
✅ Never force push to shared branches  
✅ Use feature branches, not main directly

## Verification

Before marking complete:
- [ ] Changes are staged
- [ ] Commit message follows conventions
- [ ] Commit succeeded (has SHA)
- [ ] Push completed without errors
- [ ] Remote branch updated

## Example Usage

```
User: "Commit and push my auth changes"

Droid:
1. Checks git status
2. Shows: "Modified auth.ts, added auth.test.ts"
3. Stages files
4. Suggests: "feat: add JWT authentication"
5. Commits with that message
6. Pushes to origin/feature/auth
7. Shows GitHub URL and suggests creating PR
```
