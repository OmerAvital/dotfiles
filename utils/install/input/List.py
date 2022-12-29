from dataclasses import dataclass
from .Terminal import Cursor, Terminal, StyledStr, Styling, Coordinate
from .InputItems import ask_question
import readchar

NOT_SELECTED_COLOR = 250


@dataclass
class ListOption:
    text: str
    value: any
    __is_selected: bool
    type: str

    def __init__(self, text: str, value: any = None, is_selected: bool = False):
        self.text = text
        self.value = value if value is not None else text
        self.__is_selected = is_selected
        self.type = List.DEFAULT

    def toggle(self):
        self.__is_selected = not self.__is_selected
        return self

    def is_selected(self):
        return self.__is_selected

    def set_is_selected(self, is_selected: bool):
        self.__is_selected = is_selected
        return self

    def _prefix(self):
        match self.type:
            case List.MULTI_SELECT:
                return f'[{"X" if self.__is_selected else " "}] '
            case List.HORIZONTAL:
                return ''
            case List.DEFAULT:
                return '> '

    def print(self, hovering: bool):
        if self.type != List.MULTI_SELECT:
            self.__is_selected = hovering

        styled_str = StyledStr(self._prefix() + self.text)

        if self.type == List.HORIZONTAL:
            styled_str.set_fg(NOT_SELECTED_COLOR)

        if hovering:
            styled_str.set_fg(Styling.CYAN)
            styled_str.style = Styling.BOLD

        Terminal.send(styled_str)


class List:
    MULTI_SELECT = 'multi'
    HORIZONTAL = 'horizontal'
    DEFAULT = 'default'

    question: str
    options: list[ListOption]
    type: str
    seperator = ' / '
    directions = ''

    __hovering = 0
    __cursor: Coordinate

    def __init__(self, question: str, options: list[ListOption | str], list_type=DEFAULT):
        self.question = question
        self.options = [ListOption(option) if type(option) == str else option for option in options]
        self.type = list_type
        first_selected = False
        for i, opt in enumerate(self.options):
            opt.type = list_type
            if self.type == self.HORIZONTAL and not first_selected and opt.is_selected():
                self.__hovering = i
                first_selected = True

    def __print_options(self):
        Terminal.send(self.directions, end='\n' if self.type != List.HORIZONTAL else '')
        for i, option in enumerate(self.options):
            option.print(hovering=i == self.__hovering)
            if i != len(self.options) - 1:
                Terminal.send(StyledStr(self.seperator, fg=NOT_SELECTED_COLOR) if self.type == List.HORIZONTAL else '\n')

    def __submit(self) -> list[ListOption]:
        selected_options = [opt for opt in self.options if opt.is_selected()]
        Cursor.to(self.__cursor)
        Terminal.send(' ' * (Terminal.width() - Cursor.position().col + 1))
        Cursor.to(self.__cursor)
        for _ in self.options:
            Cursor.move_down()
            Cursor.erase_line()
        Cursor.to(self.__cursor)
        Terminal.send(StyledStr(', '.join([opt.text for opt in selected_options]), fg=6), end='\n')
        return selected_options

    def __select_next(self):
        self.__hovering = min(len(self.options) - 1, self.__hovering + 1)

    def __select_prev(self):
        self.__hovering = max(0, self.__hovering - 1)

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
                        if self.type != self.HORIZONTAL:
                            self.__select_prev()
                    case readchar.key.DOWN:
                        if self.type != self.HORIZONTAL:
                            self.__select_next()
                    case readchar.key.LEFT:
                        if self.type == self.HORIZONTAL:
                            self.__select_prev()
                    case readchar.key.RIGHT:
                        if self.type == self.HORIZONTAL:
                            self.__select_next()
                    case readchar.key.ENTER:
                        return self.__submit()
                    case readchar.key.SPACE:
                        if self.type == List.MULTI_SELECT:
                            self.options[self.__hovering].toggle()
                    case readchar.key.CTRL_C:
                        self.options = [option.set_is_selected(False) for option in self.options]
                        self.__submit()
                        exit(1)
                    case readchar.key.CTRL_D:
                        raise KeyboardInterrupt
        finally:
            Cursor.blink_on()
