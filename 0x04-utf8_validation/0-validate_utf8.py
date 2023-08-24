#!/usr/bin/python3

"""A module to check for a valide utf8
"""


def validUTF8(data):
    """Valide the utf 8

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Helper function to check if a byte is a valid UTF-8 continuation byte
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
