# Add colors to ls
if [[ $(gls -d) == . ]]; then
    alias ls='gls --color'
else
    alias ls='ls -G'
fi

alias ll='ls -l'
alias la='ls -A'
alias l='ls -la'

alias mv='nocorrect mv'       # no spelling correction on mv
alias cp='nocorrect cp'       # no spelling correction on cp
alias mkdir='nocorrect mkdir' # no spelling correction on mkdir

alias now='date +%s'
alias nowdt='date +"%Y-%m-%d %T"'

alias copy=pbcopy
alias paste=pbpaste
alias gs='git status -s -b'
