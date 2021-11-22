autoload -U colors && colors

# UPDATE
source "$DOTFILES/utils/update.sh"

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
source "$DOTFILES/zsh/helpers/macos.sh"
# aliases
source "$DOTFILES/zsh/helpers/aliases.sh"
# functions
source "$DOTFILES/zsh/helpers/funcs.sh"
# prompt
source "$DOTFILES/zsh/helpers/prompt.sh"
# completion
source "$DOTFILES/zsh/helpers/completion.sh"

# PLUGINS ---------------------------------------------------------------------
# autosuggestions
if [[ -f $DOTFILES/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh ]]; then
  source "$DOTFILES/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh"
fi
# syntax highlighting
if [[ -f $DOTFILES/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]]; then
  source "$DOTFILES/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
fi
