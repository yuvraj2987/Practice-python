
def fullJustify(words, maxWidth):
    """
        Returns justified string
    """
    lines = []
    curLine = []
    curLen = 0
    for w in words:
        lw = len(w)
        if curLen + lw > maxWidth:
            lines.append(curLine)
            curLine = [w+" "]
            curLen = lw + 1
        elif curLen + lw == maxWidth:
            curLine.append(w)
            lines.append(curLine)
            curLine = []
            curLen = 0
        else: # curLen + lw < maxWidth
            curLine.append(w + " ")
            curLen = curLen + lw + 1
    # end of for
    if curLine is not None:
        lines.append(curLine)
    # end of if
    for i in range(0, len(lines)-1):
        singleLn = lines[i]
        fmtLn = evenJustify(singleLn, maxWidth)
        lines[i] = fmtLn
    # end of for
    lastLn = lines[-1]
    fmtLastLn = leftJustify(lastLn, maxWidth)
    lines[-1] = fmtLastLn
    return lines
# end of for


def evenJustify(words, maxWidth):
    curWidth = lenCount(words)
    if curWidth == maxWidth:
        return "".join(words)
    # else
    padCount = maxWidth - curWidth
    wordCount = len(words)
    evenPadding = padCount//wordCount
    oddPadding = padCount%wordCount
    for idx in range(0, len(words)):
        words[idx] = words[idx] + " " * evenPadding
    # else
    for idx in range(0, oddPadding):
        words[idx] = words[idx] + " "
    return ''.join(words)

def leftJustify(words, maxWidth):
    curWidth = lenCount(words)
    padCount = maxWidth - curWidth
    if padCount <= 0:
        return ''.join(words)
    words[-1] = words[-1] + " " * padCount
    return ''.join(words)

def lenCount(words):
    l = 0
    for w in words:
        l += len(w)
    # end of for
    return l
