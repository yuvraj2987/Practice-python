#! /usr/bin/env python


def is_unique(string):
    """
        Given a string checks if it has
        all unique characters.
        output - True/False
    """
    if string is None:
        return False
    if not isinstance(string, str):
        return False
    if len(string) <= 0:
        return False
    if len(string) == 1:
        return True
    char_map = {}
    for char in string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    # end of for
    for char, count in char_map.items():
        if count > 1:
            return False
        # end of if
    # end of for
    return True
# end of method
