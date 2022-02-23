def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    if word in wordlist:
        return True
    return False


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    #accumulator
    result = ''
    #for each letter in specified row
    for letter in board[row_index]:
        #accumulate 
        i = 0
        letter_to_add = letter[i]
        result = result + letter_to_add
        #go to next letter
        i = i+1
    return result


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    result = ''
    #go through each list item in overall list
    for i in range(len(board)):
        #add the the letter from the specified column_index to the result
        letter_to_add = board[i][column_index]
        result = result + letter_to_add

    return result


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """
    #for each board[list_index]
    for row_index in range(len(board)):
        #check if the word is in the result of predefined function
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    #for each list item in board
    for row_index in range(len(board)):
        #for each list item in the row
        for column_index in range(len(board[row_index])):
            #the goal of this function was to ultimately loop through all 4 column indexes to
            #use as in input in the make_str_from_column function
            if word in make_str_from_column(board, column_index):
                return True
    return False

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    if board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word):
        return True
    return False
        

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    score = 0
    if len(word)< 3:
        score = score
        return score
    if 3<= len(word) <= 6:
        score = score + 1*(len(word))
        return score
    if 7<= len(word) <= 9:
        score = score + 2*(len(word))
        return score
    if len(word) >= 10:
        score = score + 3*(len(word))
        return score
    else: return score


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    points_from_word = word_score(word)
    new_score = player_info[1]+ points_from_word
    player_info[1] = new_score

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    word_count = 0
    for word in words:
        for row_index in range(len(board)):
            if word in make_str_from_row(board, row_index):
                word_count = word_count + 1
                
        #This is says for a range of just 0 to 1, which is just 0. 
        for i in range(0,1):
            #Then this gets the total # of different column indexes to insert into make_str_from_column function
            #The goal of both of these for loops is to just get all the diff column indexes and
            #put it in the previous function above. Then the function can use the column indexes
            #and see if the word is in any of the columns
            for column_index in range(len(board[i])):
                if word in make_str_from_column(board, column_index):
                    word_count = word_count +1
    return word_count

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words_list = words_file.readlines()
    for i in range(len(words_list)-1):
        words_list[i] = words_list[i].rstrip('\n')
    return words_list
        


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    #put string into list
    board_list = board_file.readlines()
    #accumulate final list
    boardlist = []
    #remove the newline function from each line
    for i in range(len(board_list)-1):
        #update the original list
        board_list[i] = board_list[i].rstrip('\n')
    #take each item in list of str
    for i in range(len(board_list)):
        #pull out each row. 
        a = board_list[i]
        f = list(a)
        boardlist.append(f)
    return boardlist
        
        
