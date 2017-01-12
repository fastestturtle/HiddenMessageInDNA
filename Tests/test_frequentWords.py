from unittest import TestCase
from Code import frequentWords
from Code import common

class TestFrequentWords(TestCase):

    def test_findMostFrequentWords(self):
        genome = common.readGenomeSequenceFromFile('../Inputs/frequentWordsInput.txt')
        fw = frequentWords.findMostFrequentWords(genome, 11)

        assert(len(fw) == 1 and fw.count('GTCTACGGGTT') == 1)
