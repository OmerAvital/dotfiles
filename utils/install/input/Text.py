from dataclasses import dataclass, field
from time import sleep

from .Terminal import StyledStr, Cursor, Terminal, Styling, Coordinate
from .InputItems import ask_question


@dataclass
class TextOption:
    text: str
    acceptable_inputs: list[str] = field(default_factory=list)
    complete_match: bool = True
    case_sensitive: bool = False
    default: bool = False

    def validate(self, input_str: str) -> bool:
        full_acceptable_inputs = [*self.acceptable_inputs, self.text]
        the_input = input_str.strip()
        if not self.case_sensitive:
            full_acceptable_inputs = [acceptable_input.lower() for acceptable_input in full_acceptable_inputs]
            the_input = the_input.lower()

        if self.complete_match:
            return the_input in full_acceptable_inputs
        for acceptable_input in full_acceptable_inputs:
            if acceptable_input.startswith(the_input):
                return True
        return False


class Text:
    question: str
    options: list[TextOption]
    hint: str
    __cursor: Coordinate

    def __init__(self, question: str, options: list[TextOption | str] = None, hint: str = None):
        self.question = question
        self.options = [TextOption(option) if type(option) is str else option
                        for option in options] if options is not None else []
        default_opt = [opt for opt in self.options if opt.default]
        if len(default_opt) > 1:
            raise ValueError('Multiple default options')
        if not default_opt and self.options:
            self.options[0].default = True
        self.hint = hint if hint is not None else '(' + '/'.join([opt.text.upper() if opt.default else opt.text.lower() for opt in self.options]) + ')'

    def get_input(self) -> str:
        while True:
            Terminal.send('\n')
            Cursor.move_up()
            ask_question(self.question)
            self.__cursor = Cursor.position()
            Terminal.send(StyledStr(self.hint, style=Styling.DIM), end=' ')
            the_input = input()

            if not self.options:
                Cursor.to(self.__cursor)
                Cursor.erase_line_from_cursor()
                Terminal.send(StyledStr(the_input, fg=6), end='\n')
                return the_input

            if the_input == '':
                the_input = [opt for opt in self.options if opt.default][0].text

            for option in self.options:
                if option.validate(the_input):
                    Cursor.to(self.__cursor)
                    Cursor.erase_line_from_cursor()
                    Terminal.send(StyledStr(option.text, fg=6), end='\n')
                    return option.text

            Terminal.send(StyledStr('Invalid input', fg=Styling.RED, style=Styling.BOLD), end='\n')
