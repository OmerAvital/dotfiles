# .dotfiles

## Deploy Directions

To deploy the dotfiles, run the following command:

```shell
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/OmerAvital/dotfiles/main/utils/install/install.zsh)"
```

## General

- Auto-updates dotfiles and plugins

## ZSH

### Enhancements

- Enhanced ZSH prompt
- Enhanced completions
- Syntax highlighting
- Colored `ls`
- Colored man pages
- Autosuggestions
- `la` (see aliases) after `cd`
- `.zsh_history` moved to `$DOTFILES/zsh/` (to avoid cluttering the home directory).

### Aliases:

| Name    | Command               | Description                                                                                    |
|---------|-----------------------|------------------------------------------------------------------------------------------------|
| `ll`    | `ls -l`               | List files in the long format.                                                                 |
| `la`    | `ls -A`               | Include directory entries whose names begin with a dot (`.`) except for `.` and `..`.          |
| `l`     | `ls -la`              | List all files (including those starting with `.` and `..`, and `.` & `..`) in the long format |
| `now`   | `date +%s`            | Prints the date in milliseconds                                                                |
| `nowt`  | `date +"%Y-%m-%d %T"` | Prints the date in the `YY-MM-DD HH:MM` format.                                                |
| `copy`  | `pbcopy`              |                                                                                                |
| `paste` | `pbpaste`             |                                                                                                |
| `gs`    | `git status -s -b`    | Prints the status of the current branch in the short format.                                   |

### Functions:

| Name         | Description                                                                     |
|--------------|---------------------------------------------------------------------------------|
| `h $1`       | Prints out the command history for the last `$1` commands.                      |
| `clrs`       | Prints out all of the foreground/background colors from 1-255 that can be used. |
| `tab`        | Creates a new terminal tab¹.                                                    |
| `split_tab`  | Creates a vertical split¹.                                                      |
| `hsplit_tab` | Creates a horizontal split¹.                                                    |
| `pfd`        | Prints the directory of the frontmost `Finder` window.                          |
| `cfd`        | `cd`'s to the directory of the frontmost `Finder` window.                       |

¹Works in terminal, iTerm, iTerm2, and Hyper

## Vim

### Enhancements

- Syntax highlighting
- `.viminfo` moved to `$DOTFILES/vim/`(to avoid cluttering the home directory).
- Looks for colors and plugins in `$DOTFILES/vim/` in addition to the default locations.

## Git

### Enhancements
- Prevent committing to main/master branch

### Signing commits (verified commits)
- Follow [these instructions][signing-commits].


[signing-commits]:
    git/signing-commits.md
