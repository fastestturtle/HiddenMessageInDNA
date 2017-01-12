
def patternToIndex(pattern):
    """
    the index of the pattern in lexicographically ordered k-mers
    """
    if len(pattern) == 1:
        if pattern == 'A': return 0
        elif pattern =='C': return 1
        elif pattern =='G': return 2
        elif pattern =='T': return 3

    lastChar = pattern[-1:]
    prefix = pattern[:-1]

    return 4 * patternToIndex(prefix) + patternToIndex(lastChar)


def indexToSymbol(index):
    """
    returns the nucleotide symbol for an index in the alphabetic order
    """
    if index == 0: return 'A'
    elif index == 1: return 'C'
    elif index == 2: return 'G'
    elif index == 3: return 'T'
    else:
        print('number should be  0 to 3, it is ' + str(index))
        return 'X'


def indexToPattern(index, k):
    """
    returns the nucleotide sequence for an index in lexicographically ordered k-mers array
    """
    if k == 1:
        return indexToSymbol(index)

    prefixNumber = index / 4
    lastCharNumber = index % 4

    lastChar = indexToSymbol(lastCharNumber)
    prefixPattern = indexToPattern(prefixNumber, k-1)

    return prefixPattern + lastChar


def computeFrequencies(genome, k):
    """
    compute frequency array of k-mers in the given genome sequence
    """

    # create an array to represent all combinations of k-mers of A,T,G,C
    frequencies = [0]*pow(4, k)
    patternIndexDict = {}

    for index in range(0, len(genome)-k+1):
        pattern = genome[index:index+k]

        index = -1
        if pattern in patternIndexDict:
            index = patternIndexDict[pattern]
        else:
            index = patternToIndex(pattern)
            patternIndexDict[pattern] = index

        frequencies[index] += 1

    return frequencies


def getFrequentWord(genome, word):

    k = len(word)
    frequencies = computeFrequencies(genome, k)
    wordNumber = patternToIndex(word)

    return frequencies[wordNumber]

