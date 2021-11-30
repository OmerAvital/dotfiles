import os
from dataclasses import dataclass
from time import sleep

from .Terminal import Cursor, Terminal, StyledStr, Styling
from .InputItems import ask_question
import readchar


@dataclass
class ListOption:
    text: str
    value: str
    __is_selected: bool
    is_multi: bool = False

    def __init__(self, text: str, value: str = None, is_selected: bool = False):
        self.text = text
        self.value = value if value is not None else text
        self.__is_selected = is_selected

    def toggle(self):
        self.__is_selected = not self.__is_selected
        return self

    def is_selected(self):
        return self.__is_selected

    def set_is_selected(self, is_selected: bool):
        self.__is_selected = is_selected
        return self

    def _prefix(self):
        if self.is_multi:
            return f'[{"X" if self.__is_selected else " "}]'
        return '>'

    def print(self, hovering: bool):
        if not self.is_multi:
            self.__is_selected = hovering

        styled_str = StyledStr(self._prefix(), self.text)

        if hovering:
            styled_str.set_fg(Styling.CYAN)
            styled_str.style = Styling.BOLD

        Terminal.send(styled_str, end='\n')


class List:
    question: str
    options: list[ListOption]
    multi_select: bool
    hovering: int = 0

    __directions = StyledStr('[q to exit]', fg=6)
    __cursor = (0, 0)

    def __init__(self, question: str, options: list[ListOption | str], multi_select: bool = False):
        self.question = question
        self.options = [ListOption(option) if type(option) == str else option for option in options]
        for opt in self.options:
            opt.is_multi = multi_select
        self.multi_select = multi_select

    def __print_options(self):
        Terminal.send(self.__directions)
        Terminal.send('\n')
        for i, option in enumerate(self.options):
            option.print(hovering=i == self.hovering)

    def __submit(self) -> list[ListOption]:
        selected_options = [opt for opt in self.options if opt.is_selected()]
        Cursor.to(self.__cursor)
        Terminal.send(' ' * len(self.__directions))
        Cursor.to(self.__cursor)
        for _ in self.options:
            Cursor.move_down()
            Cursor.erase_line()
        Cursor.to(self.__cursor)
        Terminal.send(StyledStr(', '.join([opt.text for opt in selected_options]), fg=6), end='\n')
        return selected_options

    def get_input(self) -> list[ListOption]:
        Terminal.send('\n' * (len(self.options) + 1))  # reserve space for options before saving cursor position
        Cursor.move_up(len(self.options) + 1)
        ask_question(self.question)
        self.__cursor = Cursor.position()
        Cursor.blink_off()

        try:
            while True:
                Cursor.to(self.__cursor)
                self.__print_options()
                key = readchar.readkey()
                match key:
                    case readchar.key.UP:
                        self.hovering = max(0, self.hovering - 1)
                    case readchar.key.DOWN:
                        self.hovering = min(len(self.options) - 1, self.hovering + 1)
                    case readchar.key.ENTER:
                        return self.__submit()
                    case readchar.key.SPACE:
                        if self.multi_select:
                            self.options[self.hovering].toggle()
                    case 'q':
                        self.options = [option.set_is_selected(False) for option in self.options]
                        return self.__submit()
        finally:
            Cursor.blink_on()
