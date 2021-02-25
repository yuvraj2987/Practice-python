#! /usr/bin/env python

# -------------------------
# Test the modules as they will be used by clients
#
from arrays_and_hash import sort


def main():
    array = [ 4, 1, 3, 2]
    print("Original array: ", array)
    sort.mergeSort(array)
    print("Modify array:", array)




if __name__ == '__main__':
    main()
