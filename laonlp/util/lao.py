TONE_MARKS = "່້"+"໊໋"
_tone_mark = str.maketrans({i:None for i in TONE_MARKS})


def remove_tone_mark(text: str) -> str:
    """
    Remove tone mark from Lao text

    :param str text: lao text
    :return: returns a lao text without tone mark.
    :rtype: str
    """
    return text.translate(_tone_mark)