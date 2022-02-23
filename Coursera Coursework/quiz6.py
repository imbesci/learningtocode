def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    matches.append(line.startswith(letter).rstrip('\n'))

    return matches
