" Set .viminfo file location to the .dotfiles directory
set viminfofile=$DOTFILES/vim/.viminfo

" COLORSCHEME ----------------------------------------------------------------
set rtp^=$DOTFILES/vim
colorscheme atom-dark-256


" CURSOR --------------------------------------------------------------------
let &t_SI = "\<esc>[6 q"  " I-beam in insert mode
let &t_SR = "\<esc>[4 q"  " underline in replace mode
let &t_EI = "\<esc>[2 q"  " default cursor (usually blinking block) otherwise


" PREFERENCES ----------------------------------------------------------------
" Disable compatibility with vi which can cause unexpected issues.
set nocompatible

" Enable type file detection. Vim will be able to try to detect the type of file in use.
filetype on

" Enable plugins and load plugin for the detected file type.
filetype plugin on

" Load an indent file for the detected file type.
filetype indent on

" Turn syntax highlighting on.
syntax on

" Add numbers to each line on the left-hand side.
set number

" Highlight cursor line underneath the cursor horizontally.
set cursorline

" Set tab width to 4 columns.
set tabstop=4

" Use space characters instead of tabs.
set expandtab

" While searching though a file incrementally highlight matching characters as you type.
set incsearch

" Ignore capital letters during search.
set ignorecase

" Override the ignorecase option if searching for capital letters.
set smartcase

" Use highlighting when doing a search.
set hlsearch

" Set the commands to save in history default number is 20.
set history=1000
