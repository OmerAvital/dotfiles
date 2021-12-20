import os
import sys
from dataclasses import dataclass
from typing import TypedDict


class Terminal:
    ESC = '\033'

    @staticmethod
    def send(*cmd, sep=' ', end=''):
        print(*cmd, sep=sep, end=end, file=sys.stdout, flush=True)

    @staticmethod
    def size() -> (int, int):
        return os.get_terminal_size()

    @staticmethod
    def width() -> int:
        return Terminal.size()[0]

    @staticmethod
    def height() -> int:
        return Terminal.size()[1]


@dataclass
class Style:
    open: str
    close: str = ''

    def __str__(self):
        return self.open

    def __hash__(self):
        return hash(self.open + self.close)


class StyledStr:
    content: str
    fg: Style
    bg: Style
    style: Style

    def set_fg(self, fg: int | str):
        self.fg = Styling.fg(fg)
        return self

    def set_bg(self, bg: int | str):
        self.bg = Styling.bg(bg)
        return self

    def __init__(self, *args, fg: int | str = '', bg: int | str = '', style: Style = Style('')):
        self.content = ' '.join(args)
        self.fg = Styling.fg(fg)
        self.bg = Styling.bg(bg)
        self.style = style

    def __str__(self):
        return f'{self.fg.open}{self.bg.open}{self.style.open}{self.content}{self.fg.close}{self.bg.close}{self.style.close}'

    def __len__(self):
        return len(self.content)

    def __add__(self, other):
        return str(self) + str(other)


class Styling:
    RESET_ALL = Style(f'{Terminal.ESC}[0m')
    BOLD = Style(f'{Terminal.ESC}[1m', f'{Terminal.ESC}[22m')
    DIM = Style(f'{Terminal.ESC}[2m', f'{Terminal.ESC}[22m')
    ITALIC = Style(f'{Terminal.ESC}[3m', f'{Terminal.ESC}[23m')
    UNDERLINE = Style(f'{Terminal.ESC}[4m', f'{Terminal.ESC}[24m')
    REVERSE = Style(f'{Terminal.ESC}[7m', f'{Terminal.ESC}[27m')
    STRIKETHROUGH = Style(f'{Terminal.ESC}[9m', f'{Terminal.ESC}[29m')

    BLACK = 'black'
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'
    MAGENTA = 'magenta'
    CYAN = 'cyan'
    WHITE = 'white'
    GRAY = 'gray'

    __colors = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 15,
        'gray': 8,
    }

    @staticmethod
    def __validate_color(color):
        if not color:
            return ''
        if color in Styling.__colors.keys():
            return Styling.__colors[color]
        raise ValueError(f'Invalid color: {color}')

    @staticmethod
    def fg(color: int | str):
        if type(color) is int:
            return Style(f'{Terminal.ESC}[38;5;{color}m', f'{Terminal.ESC}[39m')
        return Style(f'{Terminal.ESC}[38;5;{Styling.__validate_color(color)}m', f'{Terminal.ESC}[39m')

    @staticmethod
    def bg(color: int | str):
        if type(color) is int:
            return Style(f'{Terminal.ESC}[48;5;{color}m', f'{Terminal.ESC}[49m')
        return Style(f'{Terminal.ESC}[48;5;{Styling.__validate_color(color)}m', f'{Terminal.ESC}[49m')


class Coordinate:
    col: int
    row: int

    def __init__(self, col: int, row: int):
        self.col = col
        self.row = row


class Cursor:
    @staticmethod
    def to(pos: Coordinate):
        Terminal.send(f'{Terminal.ESC}[{pos.row};{pos.col}H')

    @staticmethod
    def move_up(n=1):
        Terminal.send(f'{Terminal.ESC}[{n}A')

    @staticmethod
    def move_down(n=1):
        Terminal.send(f'{Terminal.ESC}[{n}B')

    @staticmethod
    def move_forward(n=1):
        Terminal.send(f'{Terminal.ESC}[{n}C')

    @staticmethod
    def move_backward(n=1):
        Terminal.send(f'{Terminal.ESC}[{n}D')

    @staticmethod
    def erase_line():
        Terminal.send('\033[2K')

    @staticmethod
    def erase_line_from_cursor():
        Terminal.send('\033[K')

    @staticmethod
    def save():
        Terminal.send('\033[s')

    @staticmethod
    def restore():
        Terminal.send('\033[u')

    @staticmethod
    def blink_on():
        Terminal.send('\033[?25h')

    @staticmethod
    def blink_off():
        Terminal.send('\033[?25l')

    @staticmethod
    def position() -> Coordinate:
        import sys
        import re
        if sys.platform == "win32":
            import ctypes
            from ctypes import wintypes
        else:
            import termios
        if sys.platform == "win32":
            old_stdin_mode = ctypes.wintypes.DWORD()
            old_stdout_mode = ctypes.wintypes.DWORD()
            kernel32 = ctypes.windll.kernel32
            kernel32.GetConsoleMode(kernel32.GetStdHandle(-10), ctypes.byref(old_stdin_mode))
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 0)
            kernel32.GetConsoleMode(kernel32.GetStdHandle(-11), ctypes.byref(old_stdout_mode))
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        else:
            old_stdin_mode = termios.tcgetattr(sys.stdin)
            _ = termios.tcgetattr(sys.stdin)
            _[3] = _[3] & ~(termios.ECHO | termios.ICANON)
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)
        try:
            _ = ""
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()
            while not (_ := _ + sys.stdin.read(1)).endswith('R'):
                pass
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", _)
        finally:
            if sys.platform == "win32":
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), old_stdin_mode)
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), old_stdout_mode)
            else:
                termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, old_stdin_mode)
        if res:
            return Coordinate(int(res.group("x")), int(res.group("y")))
        return Coordinate(-1, -1)
