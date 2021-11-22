autoload -U colors && colors

# UPDATE
source "$DOTFILES/utils/update.zsh"

# PATH
export PATH="$HOME/.config/yarn/global/node_modules/.bin:$PATH"
export PATH="$HOME/.yarn/bin:$PATH"

# HISTORY
export HISTFILE="$DOTFILES/zsh/.zsh_history"
export SAVEHIST=1000000000 # Number of lines to keep in history file
export HISTSIZE=1000000000 # Number of lines to keep in memory
setopt INC_APPEND_HISTORY # Immediately append to .zsh_history
setopt EXTENDED_HISTORY # Add timestamp to history
setopt HIST_FIND_NO_DUPS # No duplicates when navigating history with arrows

# macos
source "$DOTFILES/zsh/helpers/macos.zsh"
# aliases
source "$DOTFILES/zsh/helpers/aliases.zsh"
# functions
source "$DOTFILES/zsh/helpers/funcs.zsh"
# prompt
source "$DOTFILES/zsh/helpers/prompt.zsh"
# completion
source "$DOTFILES/zsh/helpers/completion.zsh"

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
