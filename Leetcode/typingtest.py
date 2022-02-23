import curses
from curses import wrapper
import time
from english_words import english_words_lower_alpha_set
import random

TESTLENGTH = 10
def wordset():
    #filter wordset to 3-9 char words only
    correctLengthWords = [word for word in english_words_lower_alpha_set if len(word) >= 3 and len(word) <= 9]
    setLength = len(correctLengthWords)
    wordset = []
    while len(wordset) < TESTLENGTH:
        rand = random.randrange(0, setLength)
        wordset.append(correctLengthWords[rand])
    return ' '.join(wordset)

def start_screen(stdscr): #intro screen
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test!")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.addstr("\nPress Esc at anytime to quit.")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2, 0, f'WPM : {wpm}', curses.color_pair(3))

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    wordString = wordset()
    target_text = wordString
    current_text = []
    wpm = 0
    start_time = 0
    stdscr.nodelay(True)
    count = 0

    while True:
        timeelapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (timeelapsed/60))/5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue
        if count == 0:
            start_time = time.time()
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
        count+=1

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "You have completed the text. Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        
    
wrapper(main)
