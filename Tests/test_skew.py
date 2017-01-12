from unittest import TestCase
from Code import skew
from Code import common


class TestSkews(TestCase):

    def test_minSkew(self):
        genome = common.readGenomeSequenceFromFile('../Inputs/skewsMinInput.txt')
        mins = skew.findSkewMin(genome)

        assert(len(mins) == 1 and mins.count(89690) == 1)
