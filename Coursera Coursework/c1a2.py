def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    length = len(dna)
    return length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    longbool =  len(dna1) > len(dna2)
    return longbool

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char in nucleotide:
           count = count + 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna_sequence):
    ''' (str)-> bool
    Return true if the dna sequence provided only has the letters 'A', 'T', 'C', 'G'.

    >>> is_valid_sequence("AATGCGG")
    True
    >>> is_valid_sequence("AATP")
    False
    '''
    total = 0
    for char in dna_sequence:
        if char in 'ATCG':
            total = total + 1
    return total == len(dna_sequence)



def insert_sequence(existing_sequence, new_sequence, loc):
    '''(str, str, int) -> str
    Insert a new dna sequence within an existing dna sequence at a partcular location within the first sequence.
    >>> insert_sequence('AATGC','CGCG', 3)
    'AATCGCGGC'
    >>> insert_sequence('AATGC','CGCG', 5)
    'AATGCCGCG'
    '''
    newstrand = existing_sequence[0:loc] + new_sequence + existing_sequence[loc:]
    return newstrand

def get_complement(n):
    ''' (str)-> str
    Provide a nucleotide and return its complement
    >>> get_complement(A)
    'T'
    >>> get_complement(G)
    'C'
    '''
    if n == 'A':
        return 'T'
    elif n== 'T':
        return 'A'
    elif n== 'G':
        return 'C'
    else:
        return 'G'
    
def get_complementary_sequence(strand):
    ''' (str)-> str
    Returns the compimentary DNA sequence to the strand provided
    >>> get_complementary_sequence('AATTGGCC')
    'TTAACCGG'
    >>> get_complementary_sequence('CGTA')
    'GCAT'
    '''

    newstrand = ''
    for char in strand:
        if char == 'A':
            newstrand = newstrand + 'T'
        elif char == 'T':
            newstrand = newstrand + 'A'
        elif char == 'G':
            newstrand = newstrand + 'C'
        else:
            newstrand = newstrand + 'G'

    return newstrand 
























