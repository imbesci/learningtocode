def cleanup(arr):
    cleaned = []
    for problem in arr:
        a = problem.split(' ')
        if (a[1] != '+') and (a[1] != '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'
        if (not a[0].isdigit()) or (not a[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        if (len(a[0])>4) or (len(a[2])>4):
            return 'Error: Numbers cannot be more than four digits.'
        cleaned.append(a)
    return cleaned

def split(a):
    return [letter for letter in a]

def findCalcs(probs):
    nums = []
    for ind, item in enumerate(cleanup(probs)):
        if item[1] == '+':
            nums.append(str(int(item[0]) + int(item[2])))
        else:
            nums.append(str(int(item[0]) - int(item[2])))
    print(nums)
    return nums

def arithmetic_arranger(problems, displayAns = False):
    segmented = cleanup(problems)
    #Initial Error Check (Correct operand, digits only, )
    if not isinstance(segmented, list):
        return segmented
    #Check for # of problems (max 5)
    numProblems = len(problems)
    if numProblems > 5:
        return 'Error: Too many problems.'
    
    #CONST  
    extraSpaces = '    '
    rowString1 = ''
    rowString2 = ''
    dashString = '' 
    answerString = ''

    for ind, item in enumerate(segmented):
        longest = max(len(item[0]), len(item[2]))
        if len(item[0]) > len(item[2]):
            spaces = '  '
            rowString1 += spaces + item[0]
        if len(item[0]) <= len(item[2]):
            num = longest + 2 - len(item[0])
            rowString1 += (' ' * num) +  item[0]
        if ind != len(segmented)-1 : rowString1 += extraSpaces
    
    for ind, item in enumerate(segmented):
        rowString2 += item[1] + ' '
        if len(item[0]) > len(item[2]):
            diff = len(item[0]) - len(item[2])
            rowString2 += (' ' * diff) + item[2]
        else: rowString2 += item[2]
        if ind != len(segmented)-1 : rowString2 += extraSpaces

    rs1arr = split(rowString1)
    rs2arr = split(rowString2)
    for ind, item in enumerate(rs2arr):
        if item ==  '+' or item == '-':
            dashString += '-'
        elif (item != ' ' or rs1arr[ind] != ' ') and not (item == '\n'):
            dashString += '-'
        else:
            dashString += ' '
    dasharr = [char for char in dashString]
    for ind, item in enumerate(dasharr):
        if ind>0 and ind < len(dasharr)-1:
            if dasharr[ind-1] == '-' and dasharr[ind+1] == '-':
                dasharr[ind] = '-'
        continue
    dashString = ''.join(dasharr)
    
    answerString = rowString1 + '\n' + rowString2 + '\n'+ dashString
    if displayAns:
        totalString = ''
        sums = findCalcs(problems)
        dashes = dashString.split('    ')
        print(dashes)
        for i in range(len(dashes)):
            s = ''
            lenD = dashes[i].count('-')
            lenA = len(sums[i])
            diff = lenD - lenA
            s = ' '*diff + sums[i]
            totalString += s
            if i != len(dashes)-1 : totalString += extraSpaces
        answerString = answerString + '\n' + totalString
        return answerString

    return answerString
  
print(arithmetic_arranger(["32 + 698", "1 - 3801", "9999 + 9999", "523 - 49"], True))