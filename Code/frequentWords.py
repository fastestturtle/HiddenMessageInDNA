from Code import patterns


def findWordsFrequency(genome, k):

    """
    find the frequency of the words of k-length (k-mers)
    :param genome: genome sequence
    :param k: length of the word
    :return: frequency dict
    """

    wordFrequency = {}

    for index in range(0, len(genome) - k + 1):
        pattern = genome[index:index + k]

        if pattern in wordFrequency:
            continue

        count = patterns.countPattern(genome, pattern)
        # print(pattern, count)

        if count == 0:
            # this should not happen
            print("WTF: zero count was found for pattern " + pattern + ". it should be at least one")

        wordFrequency[pattern] = count

    return wordFrequency


def findMostFrequentWords(genome, k):
    """
    Finds the most frequent k-mers in a genome sequence
    :param genome:
    :param k:
    :return:
    """

    mostFrequentWords = []

    wordsFrequency = findWordsFrequency(genome, k)
    maxfrequency = max(wordsFrequency.values())

    for pattern in wordsFrequency.keys():
        if wordsFrequency[pattern] == maxfrequency:
            mostFrequentWords.append(pattern)

    return mostFrequentWords
