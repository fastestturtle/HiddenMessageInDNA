
def countPattern(genome, pattern):
    """
    Find the number of specific pattern in a genome sequence
    """
    count = 0
    for index in range(0, len(genome)-len(pattern)+1):
        if genome[index:index+len(pattern)] == pattern:
            count += 1

    return count


def findPattern(genome, pattern):
    """
    find the indexes of the pattern in a given genome sequence
    """
    indexes = []

    for index in range(0, len(genome) - len(pattern) + 1):
        if genome[index:index + len(pattern)] == pattern:
            indexes.append(index)

    return indexes
