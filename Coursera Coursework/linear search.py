def linear_search(L, s):
    '''(list) -> int
    Return the index of s if it in the list. Else, return -1.

    >>> linear_search([1,2,3,4,5,6],3)
    2
    >>> linear_search([1,2,3,4,5,6],7)
    -1
    '''
    for i in range(len(L)):
        if L[i] == s:
            return i
    return -1
            
def linear_searchv2(L, s):
    '''(list, object) -> int
    Return the index of s if it in the list. Else, return -1.

    >>> linear_search([1,2,3,4,5,6],3)
    2
    >>> linear_search([1,2,3,4,5,6],7)
    -1
    '''
    i = 0
    while i != len(L) and s != L[i]:
        i += 1
    if i == len(L):
        return -1
    else:
        return i

def binary_search(L, s):
    '''(list, object) -> int
    precondition: L is sorted from smalelst to largest, and all the items in L can be compared to s.

    Return the index of the first occurence of s in L, or return -1 if s is not in L.

    '''

    b = 0
    e = len(L)-1

    while b <= e:
        m = (b+e)//2
        
        if L[m] < s:
            b = m+1
        else: e = m-1

    if b==len(L) or L[b] != v:
        return -1
    else:
        return b
