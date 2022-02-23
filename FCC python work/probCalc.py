import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors) -> None:
        self.contents = [color for color in colors for i in range(colors[color])]
    
    def draw(self, qty) -> list:
        if qty >= len(self.contents):
            return self.contents
        else:
            ballsDrawn = []
            for i in range(qty):
                numDrawn = random.randint(0, (len(self.contents)-1-i))
                ballsDrawn.append(self.contents.pop(numDrawn))
            return ballsDrawn
    
    def draw_safe(self, qty) -> list:
        deepC = (copy.deepcopy(self.contents))
        random.shuffle(deepC)
        if qty >= len(deepC):
            return deepC
        else:
            ballsDrawn = []
            for i in range(qty):
                numDrawn = random.randrange((len(deepC)-1-i))
                ballsDrawn.append(deepC.pop(numDrawn))
            return ballsDrawn



def experiment(hat:Hat, expected_balls:dict, num_balls_drawn:int, num_experiments:int) -> float:
    winningCount = 0
    currentTrial = 0
    while currentTrial < num_experiments:
        resultOfDraw = hat.draw_safe(num_balls_drawn)
        resultsDict = {}
        for ind, elem in enumerate(resultOfDraw):
            if ind > 0 and resultOfDraw[ind-1] == elem:
                continue
            else:
                resultsDict[elem] = resultOfDraw.count(elem)
        compare = True
        for key in expected_balls:
            if resultsDict.get(key) == None or (resultsDict[key] < expected_balls[key]):
                compare = False
                break
            else:
                continue
        if compare:
            winningCount += 1
        currentTrial+=1
    print(winningCount, num_experiments)
    return winningCount/num_experiments


random.seed(95)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print("Probability:", probability)
