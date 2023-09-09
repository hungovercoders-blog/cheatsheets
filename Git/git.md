---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Git Cheat Sheet

- [Git Cheat Sheet](#git-cheat-sheet)
  - [Local](#local)
  - [Remote](#remote)
  - [Branch and Commit Management](#branch-and-commit-management)
  - [Setup local git config](#setup-local-git-config)

## Local

```bash
git init ## initialise a new git repo
git add . ## add all files in the directory to git repo
git add "filename" ## add specific file to the git repo
git status ## check the status of files in the git repo
git commit -m "message" ## commit your working code to the git repo with a message
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
