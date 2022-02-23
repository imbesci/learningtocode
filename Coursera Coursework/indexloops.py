def repeated_string(s):
    '''(str)->int
    '''
    repeats = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            repeats = repeats +1
    return repeats


def shift_left(L):
    '''(list) -> NoneType
    shift everything over by one. the first item goes to the last place
    precondition: len(L)>1
    '''
    first = L[0]

    for i in range(1, len(L)):
        L[i-1] = L[i]
        
    L.remove(L[len(L)-1])
    L.append(first)

def sum_items(list1, list2):
    ''' (list of num, list of num) -> list of num
    precondition: len(list1) == len(list2)
    '''
    listsum = []
    listlen=(len(list1))
    
    for i in range(listlen):
        listsum.append((list1[i]+ list2[i]) )
    return listsum
        
def overlap(s1, s2):
    '''(str, str) -> int '''
    count = 0
    for i in (range(len(s1))):
        if s1[i] == s2[i]:
            count = count +1
    return count


def calcavg(list1):
    '''(list of list of [str, number]) -> float
    Returns the avg of grades
    '''
    count = 0
    total = 0
    for i in range(len(list1)):
        total = total + list1[i][1]
        count = count + 1
    return total/count

def multilenavg(list1):
    ''' (list of lists of varying length) -> list of floats
    When given multiple lists within a list, return the average of all sublists
    >>> grades = [[70,75,80],[70,80,90,100],[80,100]]
    >>> multilenavg(grades)
    float
    '''
    #accumulate the final result
    final = []
    #for every sublis in overall list
    for subject in list1:
        #accumulate the local sublist total, thats why its in the scope of the broader list
        total = 0
        #for every item in the sublist
        for grade in subject:
            #total the grades up
            total = total + grade
        #after the sublist grades are done totaling, add the average to the end of the final list
        #this is in the scope of the larger list because we dont want it done until we sum the avg up
        final.append(total/len(subject))
       #return the final list
    return final
        
















    







    
