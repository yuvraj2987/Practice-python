#! /usr/bin/env python


def merge(arr, tarr, ls, le, rs, re):
    """
        arr: Original array to be modified
        tarr: temporary array to store result of merge
        ls: left start index
        le: left end index
        rs: right start index
        re: right end index
    """
    if ls > le: return
    if le > rs: return
    if rs > re: return
    if ls == le == rs == re:
        return # single element
    li = ls
    ri = rs
    ti = ls
    while li <= le and ri <= re:
        if arr[li] < arr[ri]:
            tarr[ti] = arr[li]
            li += 1
        else:
            tarr[ti] = arr[ri]
            ri +=1
        # end of if/else
        ti += 1
    # end of while
    if li <= le:
        while li <= le:
            tarr[ti] = arr[li]
            li += 1
            ti += 1
    # end of if li
    if ri <= re:
        while ri <= re:
            tarr[ti] = arr[ri]
            ri += 1
            ti += 1
    # end of if ri
    i = ls
    while i <= re:
        arr[i] = tarr[i]
        i += 1
    # end of while
    return