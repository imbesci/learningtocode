def palindrome(word):
    ''' (string) -> bool '''

    length = len(word)
    half = int(len(word)/2)
    if word[0] != word[-1]:
        return False
    if len(word)%2 == 0:
        firsthalf = word[0:half]
        secondhalf = word[half:]
        length2 =  int(len(secondhalf)-1)
        reverse = ''
        while length2 >=0:
            reverse = reverse + secondhalf[length2]
            length2 =  length2-1
        if reverse == firsthalf:
            return True
        else: return False
    oddhalfend = int(len(word)//2)
    oddhalfstart =  int(len(word)//2)+1
    if len(word)%2 != 0:
        firsthalf = word[0:oddhalfend]
        secondhalf = word[oddhalfstart:]
        length2 =  int(len(secondhalf)-1)
        reverse = ''
        while length2 >=0:
            reverse = reverse + secondhalf[length2]
            length2 =  length2-1
        if reverse == firsthalf:
            return True
        else: return False

def palindrome2(word):
    reverse = ''
    wordlength = int(len(word) -1
    length2 = wordlength
    while length2 >= 0:
        reverse = reverse + word[length2]
        length2 = length2 - 1

    if word == reverse:
        return True
    return False

def reverse(word):
    output = ''
    for letter in word:
        output = letter + output
    return output

def palindrome3(word):
    n = int(len(word))
    return word[:(n//2)] == reverse(word[n-(n//2):])
                     
