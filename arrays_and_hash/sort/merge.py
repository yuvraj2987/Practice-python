#! /usr/bin/env python


def merge_array(arr, tarr, ls, le, rs, re):
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
# end of method

def mergeSort(arr):
    if arr is None: return
    l = len(arr)
    tarr = [None] * l
    mergeRecur(arr, tarr, 0, l-1)

def mergeRecur(arr, tarr, start, end):
    if start >= end:
        return
    mid = start + (end - start) // 2
    mergeRecur(arr, tarr, start, mid)
    mergeRecur(arr, tarr, mid+1, end)
    merge_array(arr, tarr, start, mid, mid+1, end)
    return
# end of mergeSortRecur
