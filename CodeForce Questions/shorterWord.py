numWords = int(input())
wordList = []

for i in range(numWords):
    word = input()
    wordList.append(word)

def shorterWord(x):
    '(str) -> str'

    length = len(x)
    if length < 11:
        return x
    else:
        return str(x[0] + str(length-2) + x[-1])

answer = shorterWord(wordList[0])
for j in range(1, len(wordList)):
    answer += '\n' + shorterWord(wordList[j])

print(answer)
    


