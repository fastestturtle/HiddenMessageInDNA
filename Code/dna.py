
def findComplimentDNAStrand(genome):
    """
    finds the compliment strand of a given strand
    :param genome:
    :return:
    """

    compliment = ''

    for char in genome:
        if char == 'A':
            compliment += 'T'
        elif char == 'T':
            compliment += 'A'
        elif char == 'C':
            compliment += 'G'
        elif char == 'G':
            compliment += 'C'

    return compliment[::-1]
