########################
# Recursive implementation of Karatsuba multiplication algorithm

def getPowerOfTen(num):
    """
        Given a number returns power of 10^n for that number
    """
    n = -1
    while num > 0:
        num = num // 10
        n += 1
    # end of while
    return n

