---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Git Cheat Sheet

- [Git Cheat Sheet](#git-cheat-sheet)
  - [VS Code Quick Workflow](#vs-code-quick-workflow)
  - [Local](#local)
  - [Remote](#remote)
  - [Branch and Commit Management](#branch-and-commit-management)
  - [Setup local git config](#setup-local-git-config)
  - [Conventional Commits](#conventional-commits)
    - [Format](#format)
    - [Types](#types)
    - [VS Code Quick Workflow](#vs-code-quick-workflow)

## Local

```bash
git init ## initialise a new git repo
git add . ## add all files in the directory to git repo
git add "filename" ## add specific file to the git repo
git status ## check the status of files in the git repo
git commit -m "message" ## commit your working code to the git repo with a message
git commit --amend --no-edit ## amend last commit without creating another one with for example small change
git reset --hard HEAD^ ## go back to commit before last
```

## Remote

```bash
git remote add origin "http://github.com/foo" ## add a remote repo to synch your local repo with
git pull "http://github.com/foo" main ## synch your local repo with a remote repo
git push origin main ## push your locally committed changes to the remote repo
git pull ##pull any changes made in the remote repo to your local repo
```

## Branch and Commit Management

```bash
git log --oneline ## see commits
git branch branch-name ## create new branch
git checkout branch-name ## checkout the branch
git merge other-branch ## merge other-branch into current branch
git branch --list ## what branches are there in the repo
git log -v ## see the change history in a branch
git log -p ## see actual change for a commit
git reset --hard {versionid} ## revert to previous version
git branch -D branch-name ## hard deletes branch even if not merged
```

## Setup local git config

You can find your git configuration file in C:\Users{username}.gitconfig.

```bash
[user]
    name = HUNGOVER CODER
    email = info@hungovercoders.com
```

```bash
git config --global user.name "HUNGOVER CODER"
git config --global user.email "info@hungovercoders.com"
```

```bash
git config --global http.proxy
http://proxyUsername:proxyPassword@proxy.server.com:port
```

## Conventional Commits

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
  - [ConventionalCommits Cheat Sheet 1](https://github.com/qoomon/git-conventional-commits)
  - [ConventionalCommits Cheat Sheet 2](https://megamorf.gitlab.io/cheat-sheets/conventional-commits/)
  - [Conventional Commits Githooks](https://github.com/tapsellorg/conventional-commits-git-hook?tab=readme-ov-file)
  - [VS Code Conventional Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
  - [Jetbrains Conventional Commits](https://plugins.jetbrains.com/plugin/13389-conventional-commit)

### Format

```yaml
<type=feat|fix|perf|build|ci|chore|docs|refactor|revert|style|test>[(optional scope)]: <description, imperative, present tense, lowercase, no dot at end>

[
  Optional body section.

  Motivation for the change and contrast with previous behaviour.

  Can span multiple lines.
]

[BREAKING CHANGE: :warning: <description, imperative, present tense, lowercase, no dot at end>]

[Closes / Fixes #123, #456, #789]

[
  - Additional links and meta-information
  - Additional links and meta-information
  - Additional links and meta-information
]
```

### Types

|Type|Meaning|Description|
|--|--|--|
|feat|Features|A new feature|
|fix|Bug fixes|A bug fix|
|docs|Documentation|Documentation only changes|
|style|Styles|Changes that do not affect the meaning of the code|
|refactor|Code Refactoring|Code change neither fixes a bug nor adds a feature|
|perf|Performance Improvements|Code change that improves performance|
|test|Tests|Adding missing tests or correct existing tests|
|build| Builds| Changes that affect build or deployment pipelines|
|chore|Chores|Other changes that don't modify src or test files|
|revert|Reverts|Reverts a previous commit|

### VS Code Quick Workflow

Following ensures use of conventional commits and automatic syncing on commit!

- Use [Conventional Commits VS Code extension](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits).
- As per extension docs
  1. Enable Settings > conventionalCommits.autoCommit configuration of the extension. The extension enables Settings > conventionalCommits.autoCommit by default.
  2. Enable Settings > git.enableSmartCommit and set Settings > git.smartCommitChanges to all to commit all changes when there are no staged changes.
  3. Set Settings > git.postCommitCommand to sync to run git.sync after commit.
- Ensure autosave is on in VS code.
- Add keyword binding for conventional commits to be CTRl+S.
  - This is nice as whenever I save now using my instinctive shortcut muscle memory I will also be prompted to commit with a good commit message and I will automatically sync my code too!
