update_txt_file=$DOTFILES/utils/update/update.txt

source "$DOTFILES/utils/update/_update.zsh"

if [[ -s "$update_txt_file" ]]; then
  cat "$update_txt_file"
  rm "$update_txt_file"
fi

__update() {
  update_results=$(update_dotfiles)
  if [[ -n "$update_results" ]]; then
    print "$update_results" > "$update_txt_file"
  fi
}

# don't create nohup.out file
(nohup "$(__update)" > /dev/null 2>&1 &) 2> /dev/null
