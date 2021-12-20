from . import Text, TextOption, List, ListOption


def yes_no(question: str, default: bool = True) -> bool:
    return Text(
        question=question,
        options=[
            TextOption('Yes', complete_match=False, default=default),
            TextOption('No', complete_match=False, default=not default),
        ],
        hint='(Y/n)' if default else '(y/N)',
    ).get_input() == 'Yes'


def yes_no_select(question: str, default: bool = True) -> bool:
    return List(
        question=question,
        options=[
            ListOption('Yes', True, is_selected=default),
            ListOption('No', False, is_selected=not default),
        ],
        list_type=List.HORIZONTAL,
    ).get_input()[0].value

