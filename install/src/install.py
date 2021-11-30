import os
import shutil
import argparse
from time import sleep, time
from input import YesNo, List, ListOption, StyledStr, Terminal, Styling


# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--IS_ON_LINUX', type=bool)
parser.add_argument('--UNAME_MACHINE', type=str)
parser.add_argument('-y', help='Answer yes to all questions', action='store_true')
args = parser.parse_args()

HOME = os.environ['HOME']

dn = os.path.dirname
dotfiles_dir = dn(dn(dn(__file__)))

# Check dotfiles directory location
if not dotfiles_dir == f'{HOME}/.dotfiles':
    if args.y or YesNo('The dotfiles folder is not at ~/.dotfiles. Do you want to install it?'):
        shutil.move(dotfiles_dir, f'{HOME}/.dotfiles/')

# Install homebrew apps
apps = [
    ListOption('google-chrome', is_selected=True),
    ListOption('iterm2', is_selected=True),
    ListOption('jetbrains-toolbox', is_selected=True),
    ListOption('setapp'),
    ListOption('silicon-info'),
    ListOption('whatsapp'),
    ListOption('zoom'),
    ListOption('rectangle', is_selected=True),
    ListOption('visual-studio-code', is_selected=True),
    ListOption('funter'),
    ListOption('firefox'),
    ListOption('firefox-developer-edition', is_selected=True),
    ListOption('node', is_selected=True),
    ListOption('deno', is_selected=True),
    ListOption('gh', is_selected=True),
    ListOption('alfred'),
]

if os.system('which brew > /dev/null') == 0:
    apps_to_install = List('Which apps do you want to install through Homebrew?', apps, multi_select=True).get_input()
    if apps_to_install:
        sleep(0.1)
        os.system(f'brew install {" ".join(app.value for app in apps_to_install)}')

# Create dotfiles in home directory
now = int(time())
with open('created_timestamp.txt', 'w') as f:
    f.write(str(now))


def backup_file(file: str):
    f = StyledStr(file, fg=Styling.MAGENTA)
    if os.path.exists(f'{HOME}/{file}') and YesNo(f'Do you want to save a copy of your {f}?'):
        shutil.copy(f'{HOME}/{file}', f'{HOME}/{file}.backup_{now}')


backup_file('.zshenv')
backup_file('.zshrc')
backup_file('.vimrc')

Terminal.send(StyledStr('Creating dotfiles in home directory...', fg='green'), end='\n')
with open(f'{HOME}/.zshenv', 'w') as zshenv, open(f'{HOME}/.zshrc', 'w') as zshrc, open(f'{HOME}/.vimrc', 'w') as vimrc:
    zshenv.write(f'source {dotfiles_dir}/zsh/.zshprofile\n')
    zshrc.write('source $DOTFILES/zsh/.zshrc\n')
    vimrc.write('source $DOTFILES/vim/.vimrc\n')
