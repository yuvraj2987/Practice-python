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


def get_compressed_string(s):
    """
        Compress give string by counting repeated chars
        input: str
        output: str
    """
    if not isinstance(s, str):
        return None
    if len(s) <= 1:
        return s
    end_idx = len(s)
    compress_chars = []
    cur_char = s[0]
    char_count = 1
    idx = 1
    while idx < end_idx:
        if s[idx] == cur_char:
            char_count += 1
        else:
            compress_chars.append(cur_char)
            compress_chars.append(str(char_count))
            cur_char = s[idx]
            char_count = 1
        # end of if
        idx += 1
    # end of while
    compress_chars.append(cur_char)
    compress_chars.append(str(char_count))
    compress_str = ''.join(compress_chars)
    if len(compress_str) >= len(s):
        return s
    return compress_str
# end of method
