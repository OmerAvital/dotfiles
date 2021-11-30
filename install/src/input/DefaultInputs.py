from . import Text, TextOption, List


def YesNo(question: str, default: bool = True):
    return Text(
        question=question,
        options=[
            TextOption('Yes', complete_match=False, default=default),
            TextOption('No', complete_match=False, default=not default),
        ],
        hint='(Y/n)' if default else '(y/N)',
    ).get_input() == 'Yes'
