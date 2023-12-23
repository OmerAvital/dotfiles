update_txt_file=$DOTFILES/utils/update/update.txt

update_dotfiles() {
  # Check for internet connection
  if ! (ping -c 1 google.com > /dev/null); then
    rm "$update_txt_file"
    return 0
  fi

  cur_dir=$(pwd)
  cd "$DOTFILES" || return 1

  # Fetch dry run first because pull always produces output
  if ! (git fetch --dry-run &> "$update_txt_file"); then
    printf "${bg_bold[red]} Dotfiles Error! ${reset_color}\n%s$(cat "$update_txt_file")\n" > "$update_txt_file"
    cat "$update_txt_file"
  else
    if [ -s "$update_txt_file" ]; then
      echo "${bg_bold[blue]} Dotfiles updated! ${reset_color}" > "$update_txt_file"
      git pull --all &>> "$update_txt_file"
    fi
  fi

  cd "$DOTFILES" &> /dev/null || return 1
  submodules_update=$(git submodule update --init --recursive --remote)
  if [ -n "$submodules_update" ]; then
    echo "${bg_bold[blue]} Submodules updated! ${reset_color}" >> "$update_txt_file"
    echo "$submodules_update" >> "$update_txt_file"
  fi

  cd "$cur_dir" &> /dev/null || return 1
  return 0
}

if [ $? -eq 0 ] && [ -s "$update_txt_file" ]; then
  cat "$update_txt_file"
  rm "$update_txt_file"
fi

(nohup "$(update_dotfiles)" < /dev/null > /dev/null 2>&1 &) &> /dev/null
