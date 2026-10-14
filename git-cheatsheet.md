# Git Cheat Sheet

## Setup
- `git config --global user.name "Name"`: set the name on my commits.
- `git config --global user.email "email"`: set the email on my commits.

## Daily workflow
- `git clone <url>`: download a repo to my computer.
- `git status`: see what changed and what is staged.
- `git diff`: see the exact lines I changed.
- `git add <file>`: stage a file for the next commit.
- `git commit -m "message"`: save a snapshot with a short description.
- `git push`: upload my commits to GitHub.
- `git pull`: download new commits from GitHub.
- `git log --oneline`: view the commit history.

## Branches
- `git branch`: list branches (the `*` marks the current one).
- `git switch -c <name>`: create a branch and switch to it.
- `git switch <name>`: move to an existing branch.
- `git push -u origin <name>`: publish a new branch and link it.
- `git branch -d <name>`: delete a merged branch locally.

## Pull request flow
1. Create a branch for the change.
2. Commit my work on the branch and push it.
3. Open a pull request on GitHub and review "Files changed".
4. Merge, delete the branch, then `git switch main` and `git pull`.

## Rules I follow
- Never commit passwords, keys, or personal data.
- Write commit messages that describe what changed.
- Commit small and often.

