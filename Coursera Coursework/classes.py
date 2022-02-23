class wordplaystr(str):
    "A subclass of string that has additional functionalites)"

    def samefirstlast(self):
        '''
        (wordplaystr) -> bool

        Parameter: len(self) != 0

        Returns whether a wordplaystr has the same first and last letter

        >>> a = wordplaystr('alabama')
        >>> a.samefirstlast()
        True
        >>> b = wordplaystr('ryan')
        >>> b.samefirstlast()
        False
        '''
        return self[0] == self[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()


