def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    shortest = len(min(strs, key=len))
    ans = ''
    matches = True
    i = 0

    while matches:
        if i==shortest:
            break
        let = []
        for j in range(len(strs)):
            if len(strs[j]) == 0:
                return ''
            else:
                let.append(strs[j][i])
        if all(k == let[0] for k in let):
            ans += let[0]
            i+=1
        else:
            matches = False
    return ans


print(longestCommonPrefix(strs = ["flower","flow","flight"]))


