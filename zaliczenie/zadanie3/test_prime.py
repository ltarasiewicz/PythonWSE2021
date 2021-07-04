from unittest import mock, TestCase
import prime


class TestPrime(TestCase):

    def test_prime_analyzer(self):
        data = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11'
        mock_open = mock.mock_open(read_data=data)
        with mock.patch('builtins.open', mock_open):
            results = prime.analyze('anyfile.txt', prime.is_prime)
            self.assertEqual(results[1], 'NOT PRIME')
            self.assertEqual(results[2], 'PRIME')
            self.assertEqual(results[3], 'PRIME')
            self.assertEqual(results[4], 'NOT PRIME')
            self.assertEqual(results[5], 'PRIME')
            self.assertEqual(results[6], 'NOT PRIME')
            self.assertEqual(results[7], 'PRIME')
            self.assertEqual(results[8], 'NOT PRIME')
            self.assertEqual(results[9], 'NOT PRIME')
            self.assertEqual(results[10], 'NOT PRIME')
            self.assertEqual(results[11], 'PRIME')
