import math
def count_vowels(string_input):
    '''
    (str)->int
    Outputs the integer number of vowels in a given string_input. Does not include y as a vowel.
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('hello')
    2
    '''
    vowel_count = 0
    for char in string_input:
        if char in "aeiouAEIOU":
            vowel_count= vowel_count + 1
            
    return(vowel_count)

def show_vowels(s):
    '''
    (str) -> str
    Outputs the vowels found in a string argument
    >>> show_vowels('shopping')
    oi
    '''
    vowel_list = ''
    for char in s:
        if char in "aeiouAEIOU":
            vowel_list = vowel_list + char
    return vowel_list

    
    
