update_txt_file=$DOTFILES/utils/update/update.txt

update_dotfiles() {
  _cur_dir=$(pwd)
  cd "$DOTFILES" || return 1
  if [[ -s "$update_txt_file" ]]; then
    rm "$update_txt_file"
  fi
  local dotfiles_update submodules_update

  # Fetch dry run first because pull always produces output
  dotfiles_update=$(git fetch --dry-run)
  submodules_update=$(cd "$DOTFILES" && git submodule update --init --recursive --remote)

  if [[ -n "$dotfiles_update" ]]; then
    dotfiles_update=$(git pull origin HEAD)
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