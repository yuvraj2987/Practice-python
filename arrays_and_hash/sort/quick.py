"""Quick sort related methods.

Write different utility functions for implementing quick sort.
Will include multiple implementations.

"""

def swap(arr, i, j):
    """Swap 2 array indexes."""
    if arr is None:
        return
    n = len(arr)
    if i >= n or j >= n:
        return
    arr[i],arr[j] = arr[j],arr[i]


def partitioner_efficient(arr, pivote_index):
    """Partition array around pivote.

    Pivote = arr[pivote_index]

    Patition elements around pivote

       ______________________________________________
      |  < p     || == p  ||             ||         ||
      |__________||_______||_____________||_________||
                 s         e              l         pi

    Maintain invariant
    a[0:s-1]: < pivote
    a[s:e-1]: == pivote
    a[e:l]: Unexplored elements
    a[l:end]: > pivote
    when l == e exit from the loop and
    ``` swap(arr, pivote_index, n-1) ```
    since n-1 element is == pivote
    """
    if arr is None:
        return
    if len(arr) <= 1:
        return
    n = len(arr)
    if pivote_index >= n:
        return
    pivote = arr[pivote_index]
    swap(arr, pivote_index, n-1)
    smaller = equal = 0
    larger = n -1
    while equal < larger:
        if arr[equal] < pivote:
            swap(arr, smaller, equal)
            smaller +=1
            equal += 1
        elif arr[equal] == pivote:
            equal += 1
        else: # arr[equal] > pivote
            swap(arr, equal, larger-1)
            larger -= 1
    # end of while
    swap(arr, equal, n-1)
# end of partition

def partition_fail(arr, pi):
    """Do nothing.

    Method to verify if tests are failing.
    """
    pass

