#!/usr/bin/env zsh

export TEMP_INSTALL_FOLDER="$HOME/.dotfiles_install"
INSTALL_URL_BASE="https://raw.githubusercontent.com/OmerAvital/dotfiles/main"

if [[ -d "$TEMP_INSTALL_FOLDER" ]]; then
    rm -rf "$TEMP_INSTALL_FOLDER"
fi

mkdir "$TEMP_INSTALL_FOLDER"
(
  cd "$TEMP_INSTALL_FOLDER" || exit

  curl --request GET -sL \
       --url "$INSTALL_URL_BASE/utils/install/requirements.txt"\
       --output "requirements.txt"

  curl --request GET -sL \
       --url "$INSTALL_URL_BASE/utils/install/install.py"\
       --output "install.py"

  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt &> /dev/null
  python3 install.py
)
