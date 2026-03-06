# GitHub Integration Guide for Droid CLI

## Method 1: GitHub MCP Server (Recommended)

The GitHub MCP server provides direct GitHub API access to Droid.

### Installation Steps

1. **Install GitHub MCP Server**
```bash
# Via npx (no installation needed)
npx -y @modelcontextprotocol/server-github

# Or install globally
npm install -g @modelcontextprotocol/server-github
```

2. **Add to MCP Configuration**

Run in Droid:
```bash
droid
> /mcp
```

Or manually edit `~/.factory/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

3. **Create GitHub Personal Access Token**

Go to: https://github.com/settings/tokens/new

Required scopes:
- `repo` (full control of private repositories)
- `workflow` (update GitHub Action workflows)
- `read:org` (read organization data)
- `read:user` (read user profile data)

Save the token and add to environment:
```bash
# Add to ~/.zshrc or ~/.bashrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_your_token_here"
```

Or use in mcp.json directly (less secure):
```json
"env": {
  "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
}
```

### Available GitHub Tools

Once configured, Droid can:
- Create, update, close issues
- Create, update, merge PRs
- Search repositories, code, issues
- Manage branches
- Read/write repository files
- Create/update releases
- Manage GitHub Actions workflows

### Usage Examples

```
"Create a GitHub issue for the bug we just fixed"
"Open a PR for my current changes"
"Search for open issues related to authentication"
"Create a new branch called feature/user-profile"
"What are the recent PRs in this repo?"
```

---

## Method 2: Git Automation Skills (No MCP Needed)

Create skills for common Git/GitHub workflows.

### Create Git Workflow Skill

`.factory/skills/git-commit-push/SKILL.md`:

```markdown
---
name: git-commit-push
description: Stage, commit, and push changes to GitHub with proper commit messages
user-invokable: true
disable-model-invocation: false
---

# Git Commit & Push Workflow

## Instructions

When the user asks to commit and push changes:

1. **Check Status**
   - Run `git status` to see changes
   - Identify modified, added, deleted files

2. **Review Changes**
   - Run `git diff` for staged changes
   - Run `git diff HEAD` for all changes
   - Summarize what changed

3. **Stage Changes**
   - Ask user which files to stage (or stage all)
   - Run `git add <files>` or `git add .`

4. **Create Commit Message**
   - Follow conventional commits format:
     - `feat:` new feature
     - `fix:` bug fix
     - `docs:` documentation
     - `refactor:` code refactoring
     - `test:` adding tests
     - `chore:` maintenance
   - Keep first line under 50 chars
   - Add description if needed

5. **Commit**
   - Run `git commit -m "type: message"`

6. **Push**
   - Check current branch: `git branch --show-current`
   - Push: `git push` or `git push -u origin <branch>`

7. **Confirm**
   - Show commit SHA
   - Provide GitHub PR link if applicable

## Example Output

**Changes staged:**
- src/auth.ts (modified)
- tests/auth.test.ts (added)

**Commit message:** `feat: add JWT authentication support`

**Pushed to:** origin/feature/auth (3 files, 245 insertions)

**Next steps:**
- Create PR: `gh pr create` or visit https://github.com/user/repo/pull/new/feature/auth
```

### Create PR Creation Skill

`.factory/skills/create-pr/SKILL.md`:

```markdown
---
name: create-pr
description: Create GitHub pull request with proper title and description
user-invokable: true
---

# Create Pull Request

## Prerequisites

- GitHub CLI (`gh`) must be installed
- Authenticated: `gh auth login`

## Instructions

1. **Analyze Changes**
   - Run `git log origin/main..HEAD --oneline` to see commits
   - Understand scope of changes

2. **Generate PR Details**
   - Title: Summarize the change (conventional commits format)
   - Description:
     - What changed and why
     - How to test
     - Related issues (fixes #123)
     - Breaking changes (if any)

3. **Create PR**
   - Run: `gh pr create --title "Title" --body "Description"`
   - Or interactive: `gh pr create`

4. **Provide Link**
   - Show PR URL
   - Mention reviewers if applicable

## Example

```bash
gh pr create \
  --title "feat: Add user authentication" \
  --body "## Changes
- Implemented JWT-based auth
- Added login/register endpoints
- Added auth middleware

## Testing
- Run: npm test
- Manual: Try login at /api/auth/login

Fixes #42"
```
```

---

## Method 3: Git Hooks for Automation

### Auto-commit Hook (SessionEnd)

Add to `.factory/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$FACTORY_PROJECT_DIR\"/.factory/hooks/auto-commit.sh"
          }
        ]
      }
    ]
  }
}
```

### Create Auto-Commit Script

`.factory/hooks/auto-commit.sh`:

```bash
#!/usr/bin/env bash
# Auto-commit changes when session ends

set -euo pipefail

cd "$FACTORY_PROJECT_DIR" || exit 0

# Check if there are changes
if ! git diff --quiet || ! git diff --cached --quiet; then
  # Ask user if they want to commit
  echo "📝 Uncommitted changes detected. Commit them?"
  echo "Run: git add . && git commit -m 'your message' && git push"
fi

exit 0
```

Make executable:
```bash
chmod +x .factory/hooks/auto-commit.sh
```

---

## Method 4: Custom Git Droid

Create a specialized Git management droid.

`.factory/droids/git-manager.md`:

```markdown
---
name: git-manager
description: Manages Git operations including staging, committing, pushing, and PR creation
model: inherit
tools: ["Read", "Execute", "Grep", "LS"]
---

# Git Manager Droid

You are a Git workflow specialist. You help users commit, push, and create PRs efficiently.

## Core Responsibilities

1. **Status & Review**
   - Always run `git status` first
   - Review changes with `git diff`
   - Summarize what changed

2. **Staging**
   - Stage relevant files with `git add`
   - Confirm staged files with `git status`

3. **Commit Messages**
   - Use conventional commits format
   - First line: type(scope): description (max 50 chars)
   - Types: feat, fix, docs, refactor, test, chore
   - Add body for complex changes

4. **Pushing**
   - Check branch: `git branch --show-current`
   - Push: `git push` or `git push -u origin <branch>`
   - Handle errors (conflicts, force push needs)

5. **PR Creation** (if gh CLI available)
   - Generate meaningful PR title and description
   - Include what changed, why, and how to test
   - Reference related issues

## Workflow

**Standard commit & push:**
1. `git status`
2. `git diff` (review changes)
3. `git add .` or selective staging
4. `git commit -m "type: message"`
5. `git push`

**Create PR:**
1. Ensure changes are pushed
2. `gh pr create --title "..." --body "..."`
3. Or: `gh pr create` (interactive)

**Handle conflicts:**
1. `git status` (see conflicts)
2. Guide user to resolve
3. `git add .` after resolution
4. `git commit` to complete merge

## Best Practices

- Always review changes before committing
- Write clear, concise commit messages
- Push to feature branches, not main
- Include issue references in commits
- Keep commits atomic (one logical change)

## Example Interactions

**User:** "Commit and push my changes"

**You:**
1. Run `git status` and `git diff`
2. Summarize changes
3. Suggest commit message
4. Execute: git add, commit, push
5. Confirm success

**User:** "Create a PR"

**You:**
1. Check `git log` for commits
2. Generate PR title and description
3. Run `gh pr create`
4. Provide PR link
```

Usage:
```
"Use git-manager to commit and push my changes"
"Have the git-manager create a PR for this feature"
```

---

## Method 5: Slash Commands

### Quick Commit Command

`.factory/commands/commit.md`:

```markdown
---
description: Stage, commit and push changes
argument-hint: [commit message]
---

# Quick Git Commit & Push

1. Run `git status` to see changes
2. Run `git diff` to review
3. Stage all changes: `git add .`
4. Commit with message: `git commit -m "$ARGUMENTS"`
5. Push: `git push`
6. Show result and commit SHA
```

Usage:
```
/commit feat: add user authentication
```

### Quick PR Command

`.factory/commands/pr.md`:

```markdown
---
description: Create GitHub pull request
argument-hint: [PR title]
---

# Create Pull Request

Requires GitHub CLI (`gh`).

1. Get recent commits: `git log origin/main..HEAD --oneline`
2. Create PR with title from arguments: `gh pr create --title "$ARGUMENTS"`
3. Use interactive mode for description
4. Return PR URL
```

Usage:
```
/pr Add user authentication feature
```

---

## Prerequisites

### Install GitHub CLI

**macOS:**
```bash
brew install gh
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt install gh

# Or via snap
sudo snap install gh
```

**Windows:**
```bash
winget install GitHub.cli
```

### Authenticate GitHub CLI

```bash
gh auth login
```

Follow prompts to authenticate with GitHub.

### Verify Installation

```bash
gh --version
gh auth status
```

---

## Recommended Setup

**For best results, use a combination:**

1. ✅ **GitHub MCP Server** - For issue/PR management, searching
2. ✅ **Git Skills** - For commit/push workflows
3. ✅ **Git Droid** - For complex Git operations
4. ✅ **Slash Commands** - For quick commits

This gives you maximum flexibility!

---

## Troubleshooting

### MCP Server Not Working

```bash
# Test GitHub token
curl -H "Authorization: token $GITHUB_PERSONAL_ACCESS_TOKEN" \
  https://api.github.com/user

# Check MCP server
npx -y @modelcontextprotocol/server-github

# Restart Droid
droid
> /mcp  # Check if GitHub server appears
```

### GitHub CLI Issues

```bash
# Re-authenticate
gh auth logout
gh auth login

# Check status
gh auth status
```

### Git Push Fails

```bash
# Set upstream
git push -u origin $(git branch --show-current)

# Or configure
git config --global push.default current
```

---

## Quick Reference

| Task | Method | Command |
|------|--------|---------|
| Commit & push | Skill | `/git-commit-push` |
| Create PR | Skill | `/create-pr` |
| Quick commit | Slash cmd | `/commit message` |
| Manage issues | MCP | "Create issue for..." |
| Search code | MCP | "Search for auth code in repo" |
| Complex Git ops | Droid | "Use git-manager to..." |

---

## Next Steps

1. Choose your preferred method(s)
2. Install prerequisites (GitHub CLI, MCP server)
3. Configure authentication
4. Test with a simple commit/PR
5. Customize workflows to your needs
