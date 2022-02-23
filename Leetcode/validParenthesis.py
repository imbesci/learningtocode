def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    closedToOpen = {')':'(', ']':'[', '}':'{'}
    stack = []
    
    for char in s:
        if char in closedToOpen:
            if stack and stack[-1] == closedToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    if not stack: return True



print(isValid('()'))