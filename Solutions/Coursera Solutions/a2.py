def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


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

def 𝚒𝚜_𝚟𝚊𝚕𝚒𝚍_𝚜𝚎𝚚𝚞𝚎𝚗𝚌𝚎(dna):
    """ (str) -> bool
    Return True if sequence only contains ATGC
    """
    for letter in dna:
        if letter not in 'ATGC':
            return False
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    Return dna1 spliced with dna2 at index

    """
    return dna1[:index] + dna2 + dna1[index:]

def 𝚐𝚎𝚝_𝚌𝚘𝚖𝚙𝚕𝚎𝚖𝚎𝚗𝚝(nt):
    """ (str) -> str
    Return the complement nucleotide
    """
    if nt == 'T':
        return 'A'
    elif nt == 'A':
        return 'T'
    elif nt == 'G':
        return 'C'
    else:
        return 'G'

def 𝚐𝚎𝚝_𝚌𝚘𝚖𝚙𝚕𝚎𝚖𝚎𝚗𝚝𝚊𝚛𝚢_𝚜𝚎𝚚𝚞𝚎𝚗𝚌𝚎(dna):
    """ (str) -> (str)
    Get the entire complimentary sequence
    """
    dna_complement = ''
    for letter in dna:
        dna_complement += 𝚐𝚎𝚝_𝚌𝚘𝚖𝚙𝚕𝚎𝚖𝚎𝚗𝚝(letter)  
    return dna_complement
