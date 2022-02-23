from english_words import english_words_lower_alpha_set
import random

def wordset():
    #filter wordset to 3-9 char words only
    correctLengthWords = [word for word in english_words_lower_alpha_set if len(word) >= 3 and len(word) <= 9]
    setLength = len(correctLengthWords)
    wordset = []
    testLength = 30
    while len(wordset) < 50:
        rand = random.randrange(0, setLength)
        wordset.append(correctLengthWords[rand])
    print(' '.join(wordset))

wordset()