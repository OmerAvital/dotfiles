#!/usr/bin/env zsh

autoload -U colors && colors

cur_pwd=$(pwd)
cd ~/.dotfiles || exit 1

# Check .dotfiles location
cur_location=$(dirname "$(realpath $cur_pwd/$0)")

if [[ $cur_location != $HOME/.dotfiles ]]; then
  echo -n "${fg_bold[yellow]}The .dotfiles folder is not at ${fg_bold[green]}~/.dotfiles${fg_bold[yellow]}. Should I move it [Yn]?${reset_color} "
  read -q "?" yn
  echo;
  if [[ $yn == "y" ]]; then
    mv "$cur_location" "$HOME/.dotfiles"
    echo "Moved .dotfiles folder from $cur_location to ${0:a:h}"
  fi
fi

# Check for updates
echo "${bg_bold[green]} Updating files... ${reset_color}"
source utils/_update.zsh
update_dotfiles

install_brew() {
  local yn

  if ! which brew &> /dev/null && [[ $1 != true ]]; then
    echo "${fg_bold[white]}Homebrew isn't installed on your computer. Would you like me to install it [yn]? ${reset_color}"
    read -q "?" yn
  fi

  if [[ $yn == y ]] || [[ $0 == true ]]; then
    echo "${bg_bold[green]}Installing Homebrew...${reset_color}"
    /bin/bash "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi
}
install_brew

# Check if coreutils is installed
if ! which gls &> /dev/null; then
  install_brew true
  echo "${bg_bold[green]}Installing coreutils...${reset_color}"
  brew install coreutils
else
  install_brew
fi

# Update dotfiles
__copy_file() {
  file=$1
  if [[ -f ~/$file ]]; then
      echo -n "${fg_bold[blue]}It looks like you already have a ${fg_bold[yellow]}$file${fg_bold[blue]} file. Should I back it up [Yn]?${reset_color} "
      read -q "?" yn
      echo;
      if [[ $yn == "y" ]]; then
        mv "$HOME/$file" "$HOME/$file.old"
        echo "${fg_bold[white]}Backed up ${fg_bold[yellow]}$file${fg_bold[white]} to ${fg_bold[yellow]}$file.old${reset_color}"
      fi
    fi
}

__copy_file ".zshenv"
echo "source $cur_location/zsh/.zshenv" > "$HOME/.zshenv"
echo "${fg_bold[white]}Created ${fg_bold[yellow]}~/.zshenv${reset_color}"

__copy_file ".zshrc"
echo "source \$DOTFILES/zsh/.zshrc" > "$HOME/.zshrc"
echo "${fg_bold[white]}Created ${fg_bold[yellow]}~/.zshrc${reset_color}"

__copy_file ".vimrc"
echo "source \$DOTFILES/vim/.vimrc" > "$HOME/.vimrc"
echo "${fg_bold[white]}Created ${fg_bold[yellow]}~/.vimrc${reset_color}"

cd "$cur_pwd" || exit 1
exec zsh
