# run ls after cd
chpwd() {
  clear
  la
}

# show history with timestamp
h() {
  history -f -$1
}

# Times the ZSH startup 10 times
timezsh() {
  local shell
  shell=${1-$SHELL}
  for _ in {1..10}; do
    /usr/bin/time "$shell" -i -c exit
  done
}

brew_prefix() {
  dirname "$(dirname "$(which brew)")"
}

clrs() {
  _print_fg() { printf "\e[38;5;%sm%3s " $1 $1; }

  _print_bg() { printf "\e[48;5;%sm%3s " $1 $1; }

  # https://www.ditig.com/256-colors-cheat-sheet
  # FOREGROUND COLORS
  # Standard colors
  for COLOR in {0..7}; do
    _print_fg $COLOR;
  done;
  echo;
  # High intensity colors
  for COLOR in {8..15}; do
    _print_fg $COLOR;
  done;
  echo;
  # 216 colors
  for COLOR in {16..231}; do
    _print_fg $COLOR;
  done;
  echo;
  # Grayscale colors
  for COLOR in {232..255}; do
    _print_fg $COLOR;
  done;
  echo;

  echo;

  # BACKGROUND COLORS
  # Standard colors
    for COLOR in {0..7}; do
      _print_bg $COLOR;
    done;
    echo;
    # High intensity colors
    for COLOR in {8..15}; do
      _print_bg $COLOR;
    done;
    echo;
    # 216 colors
    for COLOR in {16..231}; do
      _print_bg $COLOR;
    done;
    echo;
    # Grayscale colors
    for COLOR in {232..255}; do
      _print_bg $COLOR;
    done;
    echo;
}
