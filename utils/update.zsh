_cur_dir=$(pwd)
cd "$DOTFILES" || exit 1

source "$DOTFILES/utils/_update.zsh"

if [[ -s "$update_txt_file" ]]; then
  cat "$update_txt_file"
fi

__update() {
  update_results=$(_update)
  if [[ -n "$update_results" ]]; then
    print "$update_results" > "$update_txt_file"
  fi
}

(nohup "$(update_dotfiles)" & exit) 2> /dev/null

cd "$_cur_dir" || exit 1
