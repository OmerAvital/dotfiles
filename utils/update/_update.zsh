update_dotfiles() {
  _cur_dir=$(pwd)
  cd "$DOTFILES" || return 1
  local submodules_update

  UPSTREAM=${1:-'@{u}'}
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "$UPSTREAM")
  BASE=$(git merge-base @ "$UPSTREAM")

  if [ "$LOCAL" = "$REMOTE" ]; then
      # up to date
      print ""
  elif [ "$LOCAL" = "$BASE" ]; then
    # need to pull
    print "${bg_bold[blue]} Dotfiles updated\! ${reset_color}"
    git pull origin HEAD
  elif [ "$REMOTE" = "$BASE" ]; then
      # need to push
      print ""
  fi
  submodules_update=$(cd "$DOTFILES" && git submodule update --init --recursive --remote)


  if [ -n "$submodules_update" ]; then
      print "${bg_bold[blue]} Submodules updated\! ${reset_color}"
      print "$submodules_update\n"
  fi
  cd "$_cur_dir" || return 1
  return 0
}
