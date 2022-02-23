numProbs = int(input())

problemList = []

for i in range(numProbs):
    views = input().split(' ')
    problemList.append(views)


def solutions(x):
    answer = 0
    for j in range(len(problemList)):
        count = 0
        for solution in problemList[j]:
            v = int(solution)
            if v == 1:
                count+=1
        if count >= 2:
            answer += 1
    return answer

print(solutions(problemList))