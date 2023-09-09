# Gitpod

- [Gitpod](#gitpod)
  - [Useful Links](#useful-links)
  - [Helpful](#helpful)
  - [Commands](#commands)
  - [Yaml File](#yaml-file)


## Useful Links

- [gitpod samples](https://github.com/gitpod-samples)
- [gitpod github](https://github.com/gitpod-io)
- [gitpod status](https://www.gitpodstatus.com/)
- [gitpodify](https://www.gitpod.io/guides/gitpodify)
- [Gitpod workspace](https://www.gitpod.io/docs/configure/workspaces/workspace-image) uses [workspace-full](https://hub.docker.com/r/gitpod/workspace-full) docker image.
- [Open Visual Studio Code Extension Registry](https://open-vsx.org/)
- [Personalize Environments](https://www.gitpod.io/blog/personalize-your-gitpod-workspace-environment)
- [Dotfiles](https://github.com/gitpod-samples/demo-dotfiles-with-gitpod)
- [Sharing Workspaces](https://www.gitpod.io/docs/configure/workspaces/collaboration)
- [Gitpod Twitter](https://twitter.com/gitpod)
- [Gitpod Community](https://discord.com/channels/816244985187008514/816249489911185418)

## Helpful

* Type @builtin in extensions to see all builtin extensions

## Commands

- [CLI](https://www.gitpod.io/docs/references/gitpod-cli)

```bash
gp init # Initialize a new .gitpod.yml file
gp validate # Validate the .gitpod.yml file
gp help # Get help on the CLI
gp url # Get the URL of the running workspace
gp preview $(gp url 8000)/index.html # Open the workspace in a new browser tab for path and port specified
```

## Yaml File

- [Gitpod Yaml Reference](https://www.gitpod.io/docs/references/gitpod-yml)


```yaml
# List the start up tasks. Learn more: https://www.gitpod.io/docs/configure/workspaces/tasks

# Before and init runs during prebuild => https://www.gitpod.io/docs/configure/projects/prebuilds

tasks:
  - name: Start web server
    init: python -m http.server 8000
  - name: Before Task 
    before: echo 'before script'  ## Use this for tasks that need to run before init and before command. For example, customize the terminal or install global project dependencies.
  - name: Init Task
    init: echo 'init script' # Use this for heavy-lifting tasks such as downloading dependencies or compiling source code.
  - name: Commmand Task
    command: echo 'command script' # Use this to start your database or development server.
  - name: Multiline Commmand Task
    command: |
      echo 'multiline command script 1' 
      echo 'multiline command script 2' 
  - name: Await Task
    command: |
      gp sync-await tasktowaiton
      echo 'awaited for another task'
      TIMESTAMP=$(date +%Y%m%d_%H%M%S)
      echo "Timestamp: $TIMESTAMP"
  - name: Awaited Task
    command: |
      gp sync-done tasktowaiton
      echo 'awaited for this task'
      TIMESTAMP=$(date +%Y%m%d_%H%M%S)
      echo "Timestamp: $TIMESTAMP"
      sleep 1
  - name: Installed Python Version
    command: python --version
  - name: Installed Docker Version
    command: docker version
  - name: Installed Ruby Version
    command: ruby -v
  - name: Installed Java Version
    command: java -version
  - name: Installed Node Version
    command: node -v
  - name: Installed Go Version
    command: go version

ports:
  - port: 8000
    onOpen: open-preview

vscode:
  extensions:
    - dracula-theme.theme-dracula


```