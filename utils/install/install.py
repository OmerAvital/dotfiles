import platform
import os
import shutil
import git
import subprocess
from time import sleep, time
import inquirer
from termcolor import cprint, colored

REPO_URL_BASE = "https://github.com/OmerAvital/dotfiles/blob/main"
HOME = os.path.expanduser('~')
DOTFILES = f'{HOME}/.dotfiles'
now = int(time())


def backup_file(file: str):
    f = colored(file, color="magenta")
    if os.path.exists(f'{HOME}/{file}') and inquirer.confirm(f'Do you want to save a copy of your {f}?', default=True):
        shutil.copy(f'{HOME}/{file}', f'{HOME}/{file}.backup_{now}')


def main():
    if platform.system() != 'Darwin':
        print("Omer's dotfiles are only supported on MacOS.")
        exit(1)

    if platform.machine() != 'arm64':
        print("Omer's dotfiles are only supported on Apple Silicon Macs.")
        exit(1)

    dotfiles_installed = os.path.exists(DOTFILES)

    if dotfiles_installed:
        cprint('Dotfiles found!', color="white", on_color="on_blue", attrs=["bold"])
    else:
        cprint('Cloning dotfiles directory...', color="white", on_color="on_blue", attrs=["bold"])
        dotfiles_repo = git.Repo.clone_from('ssh://git@github.com:OmerAvital/dotfiles.git', to_path=DOTFILES)
        dotfiles_repo.submodule_update(recursive=True)

    apps = [
        ['alfred', True],
        ['arc', True],
        ['deno', True],
        ['figma', True],
        ['firefox', True],
        ['firefox-developer-edition', False],
        ['funter', False],
        ['gh', True],
        ['google-chrome', True],
        ['google-drive', True],
        ['iterm2', True],
        ['jetbrains-toolbox', True],
        ['microsoft-excel', True],
        ['microsoft-powerpoint', True],
        ['microsoft-word', True],
        ['node', True],
        ['pnpm', True],
        ['rectangle', True],
        ['setapp', True],
        ['thefuck', True],
        ['visual-studio-code', True],
        ['whatsapp', True],
        ['yarn', True],
        ['zoom', True],
        ['grammarly', True]
    ]

    apps.sort(key=lambda x: x[0])

    apps_to_install = inquirer.checkbox('Which apps do you want to install through Homebrew?',
                                        choices=[name for (name, _) in apps],
                                        default=[name for (name, default) in apps if default])

    if not os.path.exists('/opt/homebrew'):
        cprint('Installing Homebrew...', color="green", attrs=["bold"])
        subprocess.run(['/bin/bash',
                        '-c',
                        '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'])
        cprint('Done installing Homebrew!', color="green", attrs=["bold"])

    if not shutil.which('gls'):
        cprint('Installing coreutils...', color="green", attrs=["bold"])
        subprocess.run(['/opt/homebrew/bin/brew', 'install', 'coreutils'])
        cprint('Done installing coreutils!', color="green", attrs=["bold"])

    if apps_to_install:
        cprint('Installing apps through Homebrew...', color="green", attrs=["bold"])
        subprocess.run(['/opt/homebrew/bin/brew', 'install', *(app for app in apps_to_install)])
        cprint('Done installing apps!', color="green", attrs=["bold"])

    # Create dotfiles in home directory
    with open('created_timestamp', 'w') as f:
        f.write(str(now))

    if not dotfiles_installed or inquirer.confirm('Do you want to rewrite the created env files?', default=False):
        backup_file('.zshenv')
        backup_file('.zshrc')
        backup_file('.vimrc')

        cprint('Creating dotfiles in home directory...', color="green")
        with open(f'{HOME}/.zshenv', 'w') as zshenv, open(f'{HOME}/.zshrc', 'w') as zshrc, open(f'{HOME}/.vimrc', 'w') as vimrc:
            zshenv.write(f'source {DOTFILES}/zsh/.zshenv\n')
            zshrc.write('source $DOTFILES/zsh/.zshrc\n')
            vimrc.write('source $DOTFILES/vim/.vimrc\n')

    subprocess.run(['git', 'config', '--global', 'core.hooksPath', f'{DOTFILES}/git/hooks'])
    print(f'Git configuration complete. To sign commits using ssh,'
          'follow the instructions in {REPO_URL_BASE}/git/signing-commits.md')

    cprint("\nConfiguration complete! Opening further config instructions...",
           color="black", on_color="on_green")
    sleep(1)
    subprocess.run(['open', f'{DOTFILES}/utils/install/additional-instructions/index.html', '-a', 'Safari.app'])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        shutil.rmtree(os.environ.get('TEMP_INSTALL_FOLDER'), ignore_errors=True)
