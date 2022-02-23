import random
MIN = 1
UPPER = random.randint(20, 50)
secretNumber = random.randint(MIN,UPPER)
print(f'Guess the number I\'m thinking of! It can\'t be higher than {UPPER}!')

def getInput():
    while True:
        val = input('Whats your guess? Whole numbers only. ')
        try:
            val = int(val)
        except ValueError:
            print('Please enter an integer')
            continue
        if 1<=val<=UPPER:
            return val
        else:
            print(f'Please pick a number between 1 and {UPPER}.')
guesss = 'guess'
guesses = 'guesses'
gotit = False
for i in range(1, 7):
    guess = getInput()
    if guess < secretNumber:
        print(f'Too low! You have {6-i} {guesses if 0<i<5 else guesss} left')
        continue
    if guess > secretNumber:
        print(f'Too high! You have {6-i} {guesses if 0<i<5 else guesss} left')
        continue
    if guess == secretNumber:
        print(f'Congrats, you won in {i} {guesses if i>1 else guesss}')
        gotit = True
        break
if not gotit:
    print(f'The number was {secretNumber} - Better luck next time!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
