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

def checkAnagrams(w1, w2):
    """
        Checks if w1 and w2 are anagrams
        Input: str
        Input: str
        Output: bool
    """
    if w1 is None or w2 is None:
        return False
    len1 = len(w1)
    len2 = len(w2)
    if len1 != len2:
        return False
    char_map = {}
    for ch in w1:
        if ch in char_map:
            char_map[ch] += 1
        else:
            char_map[ch] = 1
    # end of for
    for ch in w2:
        if ch not in char_map:
            return False
        char_map[ch] -= 1
        if char_map[ch] < 0:
            return False
    # end of for
    for k in char_map:
        if char_map[k] != 0:
            return False
    # end of for
    return True
# End of method

def zigZagConvert(s, numRows):
    """
        Convert given string into zig zag string with given number of rows
    """
    if s is None:
        return None
    if numRows < 1:
        return None
    if numRows == 1:
        return s
    rows = [[] for _ in range(numRows)]
    jmp = 0
    zigDir = True

    for ch in s:
        if jmp >= numRows:
            # Reverse the direction
            if zigDir:
                jmp = numRows - 2
                zigDir = False
            # else throw exception
        # end of if

        if jmp < 0:
            if not zigDir:
                jmp = 1
                zigDir = True
            # else throw exception
        # end of if
        row_select = rows[jmp]
        row_select.append(ch)
        if zigDir:
            jmp += 1
        else:
            jmp -= 1
    # end of for
    rowsStrs = ["".join(r) for r in rows]
    print(rowsStrs)
    resultStr = "".join(rowsStrs)
    return resultStr
