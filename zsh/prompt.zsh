# https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html

# https://arjanvandergaag.nl/blog/customize-zsh-prompt-with-vcs-info.html
# https://zsh.sourceforge.io/Doc/Release/User-Contributions.html#Version-Control-Information
# https://sampo.website/blog/en/2021/zsh/

# Allow to use variables in prompt
setopt prompt_subst

# Uses these colors because 'fg[$1]' function causes issues with the cursor & spacing
prompt_reset="%b%f%s%k"

# Directory
PROMPT_DIR="%F{cyan}%B%1~${prompt_reset} "

# Git
autoload -Uz vcs_info
precmd() {
  vcs_info
}

# this makes %u work, but also the prompt is clearly slower in git dirs when this is on
zstyle ':vcs_info:*' check-for-changes true
# what string to use for %u when there are unstaged changes
zstyle ':vcs_info:*' unstagedstr '*'
# vcs_info supports multiple version control systems, but I need just git
zstyle ':vcs_info:*' enable git

zstyle ':vcs_info:git:*' formats "%
%B%F{blue}%r:(%
%F{red}%b%
%F{magenta}%u%
%F{blue}) "

zstyle ':vcs_info:git:*' actionformats "%
%B%F{blue}%s:(%
%F{red}%b%
%F{magenta}%u%
%F{orange} %a%
%F{blue}) "

PROMPT_GIT='${vcs_info_msg_0_}${prompt_reset}'

# Arrow
PROMPT_ARROW="%B%F{%(?.green.red)}▶${prompt_reset} "

export PROMPT="${PROMPT_DIR}${PROMPT_GIT}${PROMPT_ARROW}"

# Exit code
RPROMPT_EXIT_CODE="%(?..%F{red}(%?%))${prompt_reset}"

export RPROMPT="${RPROMPT_EXIT_CODE}"
