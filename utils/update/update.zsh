_cur_dir=$(pwd)
cd "$DOTFILES" || exit 1

source "$DOTFILES/utils/update/_update.zsh"

if [[ -s "$update_txt_file" ]]; then
  cat "$update_txt_file"
fi

__update() {
  update_results=$(update_dotfiles)
  if [[ -n "$update_results" ]]; then
    print "$update_results" > "$update_txt_file"
  fi
}

(nohup "$(__update)" & exit) 2> /dev/null

cd "$_cur_dir" || exit 1
