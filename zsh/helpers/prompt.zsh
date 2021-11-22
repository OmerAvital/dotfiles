# https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html

# Allow to use variables in prompt
setopt prompt_subst

prompt_reset="%b%f%s%k"

# DIRECTORY
PROMPT_DIR="%B%F{cyan}%1~${prompt_reset} "

# GIT
autoload -Uz vcs_info
precmd() {
  vcs_info
}
# https://arjanvandergaag.nl/blog/customize-zsh-prompt-with-vcs-info.html
zstyle ':vcs_info:git:*' formats "%
%B%F{blue}%s:(%
%{${reset_color}%}%F{#fff}%r %
%B%F{red}%b%
%F{blue})"

PROMPT_GIT='${vcs_info_msg_0_}${prompt_reset} '

# SUDO
RPROMPT_SUDO="%(#.%B%K{yellow}sudo${prompt_reset}.)"

# ARROW
PROMPT_ARROW="%B%F{%(?.green.red)}▶${prompt_reset} "

PROMPT="${PROMPT_DIR}${PROMPT_GIT}${PROMPT_ARROW}"
RPROMPT="${RPROMPT_SUDO}"
