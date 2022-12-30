update_txt_file=$DOTFILES/utils/update/update.txt

update_dotfiles() {
  cur_dir=$(pwd)
  cd "$DOTFILES" || return 1

  # Fetch dry run first because pull always produces output
  git fetch --dry-run &> "$update_txt_file"
  if [ -s "$update_txt_file" ]; then
    rm "$update_txt_file"
    echo "${bg_bold[blue]} Dotfiles updated! ${reset_color}" > "$update_txt_file"
    git pull --all &>> "$update_txt_file"
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

if [ -s "$update_txt_file" ]; then
  cat "$update_txt_file"
  rm "$update_txt_file"
fi

(nohup "$(update_dotfiles)" < /dev/null > /dev/null 2>&1 &) &> /dev/null
