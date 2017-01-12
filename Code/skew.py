
def findSkew(genome):
    """
    returns the skew of a genome sequence, which is the difference between the total number of occurrences of G and the total number of occurrences of C
    :param genome:
    :return:
    """
    length = len(genome) + 1
    skews = [0]*length

    for index in range(0, length-1):
        if genome[index] == 'C':
            skews[index+1] = skews[index] - 1
        elif genome[index] == 'G':
            skews[index+1] = skews[index] + 1
        else:
            skews[index+1] = skews[index]

    return skews


def findSkewMin(genome):
    """
    the index of where genome skew hits minimum. this is important to find the replication ori
    :param genome:
    :return:
    """
    skews = findSkew(genome)
    mins = []
    min = 0

    for s in skews:
        if s < min: min = s

    for index in range(0, len(skews)):
        if skews[index] <= min:
            mins.append(index)

    #print(min)
    return mins