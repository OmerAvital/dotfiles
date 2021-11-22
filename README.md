# .dotfiles

### Enhancements
- Enhanced ZSH prompt
- Syntax highlighting
- Colored `ls`
- Autosuggestions
- `la` (see aliases) after `cd`
- Auto-updates dotfiles and plugins

### Other Changes
- `.zsh_history` moved to `$DOTFILES/zsh/`.
- `.viminfo` moved to `$DOTFILES/vim/`.
- Vim also looks for colors and plugins in `$DOTFILES/vim/`

### Aliases:
| Name | Command | Description |
|------|---------|-------------|
| `ll` | `ls -l` | List files in the long format. |
| `la` | `ls -A` | Include directory entries whose names begin with a dot (`.`) except for `.` and `..`. |
| `l` | `ls -la` | List all files (including those starting with `.` and `..`, and `.` & `..`) in the long format |
| `now` | `date +%s` | Prints the date in milliseconds |
| `nowt` | `date +"%Y-%m-%d %T"` | Prints the date in the `YY-MM-DD HH:MM` format. |
| `copy` | `pbcopy` |
| `paste` | `pbpaste` |
| `gs` | `git status -s -b` | Prints the status of the current branch in the short format. |

### Functions:
| Name | Description |
|------|------------|
| `h $1` | Prints out the command history for the last `$1` commands. |
| `clrs` | Prints out all of the foreground/background colors from 1-255 that can be used. |
| `tab` | Creates a new terminal tab (works in terminal, iTerm, iTerm2, and Hyper). |
| `split_tab` | Creates a vertical split (works in terminal, iTerm, iTerm2, and Hyper). |
| `hsplit_tab` | Creates a horizontal split (works in terminal, iTerm, iTerm2, and Hyper). |
| `pfd` | Prints the directory of the frontmost `Finder` window. |
| `cfd` | `cd`'s to the directory of the frontmost `Finder` window. |
