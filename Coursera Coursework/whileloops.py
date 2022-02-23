def up_to_vowel(s):
    '''(str)-> str
    Returns the substring of in index to but not including the first vowel in s.
    >>> up_to_vowel('there')
    'th'
    '''

    # h contains all the characters in s[0:i]
    i = 0
    h = ''

    # accumulate non-vowels in h 
    while i < len(s) and (not s[i] in 'aeiouAEIOU'):
        h = h + s[i]
        i = i + 1
    print(h)


def get_answer(prompt):
    '''(str) -> str
    Use prompt to ask the user for a 'yes' or 'no' answer and continue asking until the user gives a valid response.
    Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)
    return answer

def double_even_indices(lst):
    i = 0
    while i<len(lst):
        lst[i] = lst[i]*2
        i=i+2
        
def even_sum(int1,int2):
    ''' (int, int)-> int
    returns the sum of every even number in increments of 2 given a starting integer range
    '''
    total = 0
    for num in range(int1, (int2+1)):
        if num % 2 != 0:
            total = total + num
    return total


def while_sum(input1, input2):
    ''' (int, int) -> int '''
    total = 0
    while input1 <= input2 and input1%2 != 0:
        total = total + input1
        input1 = input1+2
    return total























    
