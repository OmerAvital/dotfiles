update_txt_file=$DOTFILES/utils/update.txt

update_dotfiles() {
  _cur_dir=$(pwd)
  cd "$DOTFILES" || return 1
  if [[ -s "$update_txt_file" ]]; then
    rm "$update_txt_file"
  fi
  local dotfiles_update submodules_update
  dotfiles_update=$(git fetch)
  submodules_update=$(cd "$DOTFILES" && git submodule update "$1" --init --recursive --remote)

  if [[ -n "$dotfiles_update" ]]; then
    print "${bg_bold[blue]} Dotfiles updated\! ${reset_color}"
    print "$dotfiles_update\n"
  fi
  if [[ -n "$submodules_update" ]]; then
      print "${bg_bold[blue]} Submodules updated\! ${reset_color}"
      print "$submodules_update\n"
  fi
  cd "$_cur_dir" || return 1
  return 0
}
