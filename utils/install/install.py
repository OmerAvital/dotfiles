import os
import shutil
from time import sleep, time
from input import yes_no, List, ListOption, StyledStr, Terminal, Styling

HOME = os.environ['HOME']

dn = os.path.dirname
dotfiles_dir = dn(dn(dn(__file__)))

# Check dotfiles directory location
if not dotfiles_dir == f'{HOME}/.dotfiles':
    if yes_no('The dotfiles folder is not at ~/.dotfiles. Do you want to install it?'):
        shutil.move(dotfiles_dir, f'{HOME}/.dotfiles/')

# Install homebrew apps
apps = [
    ListOption('google-chrome', is_selected=True),
    ListOption('iterm2', is_selected=True),
    ListOption('jetbrains-toolbox', is_selected=True),
    ListOption('setapp', is_selected=True),
    ListOption('silicon-info'),
    ListOption('whatsapp', is_selected=True),
    ListOption('zoom', is_selected=True),
    ListOption('rectangle', is_selected=True),
    ListOption('visual-studio-code', is_selected=True),
    ListOption('funter', is_selected=True),
    ListOption('firefox'),
    ListOption('firefox-developer-edition', is_selected=True),
    ListOption('node', is_selected=True),
    ListOption('deno', is_selected=True),
    ListOption('gh', is_selected=True),
    ListOption('alfred', is_selected=True),
]

apps_to_install = List('Which apps do you want to install through Homebrew?', apps, list_type=List.MULTI_SELECT).get_input()
if apps_to_install:
    sleep(0.1)
    os.system(f'brew install {" ".join(app.value for app in apps_to_install)}')

# Create dotfiles in home directory
now = int(time())
with open('created_timestamp.txt', 'w') as f:
    f.write(str(now))


def backup_file(file: str):
    f = StyledStr(file, fg=Styling.MAGENTA)
    if os.path.exists(f'{HOME}/{file}') and yes_no(f'Do you want to save a copy of your {f}?'):
        shutil.copy(f'{HOME}/{file}', f'{HOME}/{file}.backup_{now}')


backup_file('.zshenv')
backup_file('.zshrc')
backup_file('.vimrc')

Terminal.send(StyledStr('Creating dotfiles in home directory...', fg='green'), end='\n')
with open(f'{HOME}/.zshenv', 'w') as zshenv, open(f'{HOME}/.zshrc', 'w') as zshrc, open(f'{HOME}/.vimrc', 'w') as vimrc:
    zshenv.write(f'source {dotfiles_dir}/zsh/.zshprofile\n')
    zshrc.write('source $DOTFILES/zsh/.zshrc\n')
    vimrc.write('source $DOTFILES/vim/.vimrc\n')

Terminal.send(StyledStr('Configuring git', fg=Styling.BLACK, bg=Styling.WHITE, style=Styling.BOLD), end='\n')
os.system('$DOTFILES/git/initial-config.zsh')
