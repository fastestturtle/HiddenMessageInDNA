from Code import frequencyArray, common

def findClumps(genome, k, L, t):
    """
     given genome, L, k, t: find k-mers that have been repeated at least t times within substring of L in text
    """
    patterns = []

    for index in range(0, len(genome) - L):
        substr = genome[index:index + L]
        frequencies = frequencyArray.computeFrequencies(substr, k)
        for index in range(0, len(frequencies)):
            if frequencies[index] >= t:
                pattern = frequencyArray.numberToPattern(index, k)
                if patterns.count(pattern) == 0:
                    patterns.append(pattern)

    return patterns

def findClumpsOptimized(genome, k, L, t):
    """
    given genome, L, k, t: find k-mers that have been repeated at least t times within substring of L in text
    this is optimized for speed by calculating frequency array only once (considering that
    the frequency array of a sliding window of L over genome only changes in the first and last k-mer)
    """
    patterns = []
    count = pow(4, k) - 1
    clumps = [0] * count
    substr = genome[0:L]
    frequencies = frequencyArray.computeFrequencies(substr, k)

    for index in range(0, count):
        if frequencies[index] >= t:
            clumps[index] = 1

    for index in range(1, len(genome) - L):

        firstPattern = genome[index - 1:index - 1 + k]
        firstPatternIndex = frequencyArray.patternToIndex(firstPattern)
        frequencies[firstPatternIndex] -= 1

        lastPattern = genome[index + L - k:index + L]
        lastPatternIndex = frequencyArray.patternToNumber(lastPattern)
        frequencies[lastPatternIndex] += 1

        if frequencies[lastPatternIndex] >= t:
            clumps[lastPatternIndex] = 1

    for i in range(0, pow(4, k) - 1):
        if clumps[i] == 1:
            pattern = frequencyArray.indexToPattern(i, k)
            if patterns.count(pattern) == 0:
                patterns.append(pattern)

    return patterns