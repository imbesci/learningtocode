def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    intbus = n//50
    if n%50 != 0:
        return intbus + 1
    else:
        return intbus

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    pos_sum = 0
    neg_sum = 0
    for n in price_changes:
        if n>0:
            pos_sum = pos_sum + n
        if n<0:
            neg_sum = neg_sum + n
    return (pos_sum, neg_sum)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    first = []
    middle= []
    second = []
    for a in range(0,k):
        first.append(L[a])
    for b in range(k,(len(L)-k)):
        middle.append(L[b])
    for c in range((len(L)-k), len(L)):
        second.append(L[c])
    L.clear()
    for i in second:
        L.append(i)
    for j in middle:
        L.append(j)
    for k in first:
        L.append(k)


    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
