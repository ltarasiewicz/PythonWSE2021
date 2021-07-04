import numbers
from unittest import TestCase


class TestRates(TestCase):

    def test_rate_numbers(self):
        score_card = numbers.rate(1, 15)

        self.assertEqual(15, len(score_card))

        self.assertEqual(score_card[1], '')
        self.assertEqual(score_card[2], '')
        self.assertEqual(score_card[3], 'GOOD')
        self.assertEqual(score_card[4], '')
        self.assertEqual(score_card[5], 'BETTER')
        self.assertEqual(score_card[6], 'GOOD')
        self.assertEqual(score_card[7], '')
        self.assertEqual(score_card[8], '')
        self.assertEqual(score_card[9], 'GOOD')
        self.assertEqual(score_card[10], 'BETTER')
        self.assertEqual(score_card[11], '')
        self.assertEqual(score_card[12], 'GOOD')
        self.assertEqual(score_card[13], '')
        self.assertEqual(score_card[14], '')
        self.assertEqual(score_card[15], 'BEST')
