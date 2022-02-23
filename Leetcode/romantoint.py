def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romanArr = {"I":1,  "V":5,  "X":10, "L":50, "C":100, "D":500, "M":1000}
    tot = 0
    curr, prev = 0, 0
    for letter in s[::-1]:
        curr = romanArr[letter]
        if curr<prev:
            tot -= curr
        else:
            tot += curr
        prev = curr
    return tot



                 
print(romanToInt('MCMXCIV'))