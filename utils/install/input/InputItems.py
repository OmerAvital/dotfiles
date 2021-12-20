from . import StyledStr, Styling, Terminal


def ask_question(question: str) -> int:
    """
    Prints out the question and returns the length of the question string.
    :param question:
    :return:
    """
    qm = StyledStr('?', fg=Styling.GREEN, style=Styling.BOLD)
    question = StyledStr(question, style=Styling.BOLD)
    question_str = f'{qm} {question} '
    Terminal.send(question_str)
    return len(qm) + len(question) + 2
