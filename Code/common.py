"""
Some common functions that are used in the code
"""

def readGenomeSequenceFromFile(path):
    """
    reads an entire text file assuming it got one line, i.e. a genome sequence
    :param path: local path to the file
    :return: a string representing the genome sequence
    """
    with open(path) as f:
        return f.readline()

def arraytoSpaceSeparatedValues(array):
    """
    print array members as a line of space separated values
    :param array: input array
    :return: space separated values as a string
    """
    output = ''
    for a in array:
        output += a.__str__() + ' '

    return output.rstrip()
