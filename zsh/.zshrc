autoload -U colors && colors

# UPDATE
source "$DOTFILES/utils/update/update.zsh"

# HISTORY
export HISTFILE="$DOTFILES/zsh/.zsh_history"
export SAVEHIST=1000000000 # Number of lines to keep in history file
export HISTSIZE=1000000000 # Number of lines to keep in memory
setopt INC_APPEND_HISTORY # Immediately append to .zsh_history
setopt EXTENDED_HISTORY # Add timestamp to history
setopt HIST_FIND_NO_DUPS # No duplicates when navigating history with arrows

# THEFUCK
# https://github.com/nvbn/thefuck/issues/859#issue-388147791
if command -v thefuck > /dev/null 2>&1; then
  fuck() {
    eval "$(thefuck --alias)" && fuck
  }
fi

# macos
source "$DOTFILES/zsh/macos.zsh"
# aliases
source "$DOTFILES/zsh/aliases.zsh"
# functions
source "$DOTFILES/zsh/funcs.zsh"
# prompt
source "$DOTFILES/zsh/prompt.zsh"
# completion
source "$DOTFILES/zsh/completion.zsh"
# Colored man pages
source "$DOTFILES/zsh/colored-man-pages.zsh"

# PLUGINS ---------------------------------------------------------------------
# autosuggestions
if [[ -f $DOTFILES/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh ]]; then
  source "$DOTFILES/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh"
else
  echo "zsh-autosuggestions plugin not found"
fi
# syntax highlighting
if [[ -f $DOTFILES/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]]; then
  source "$DOTFILES/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
else
  echo "zsh-syntax-highlighting plugin not found"
fi
