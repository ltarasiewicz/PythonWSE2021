from unittest import TestCase
import age

testCases = [
    {
        'input': '1986',
        'has_errors': False,
        'message': "You're 35 years old and you are an adult",
    },
    {
        'input': '2010',
        'has_errors': False,
        'message': "You're 11 years old and you aren't an adult",
    },
    {
        'input': '2042',
        'has_errors': True,
        'message': age.Validator.FUTURE_DATE_ERROR
    },
    {
        'input': 'abcd',
        'has_errors': True,
        'message': age.Validator.WRONG_FORMAT_ERROR
    },
    {
        'input': '1234576',
        'has_errors': True,
        'message': age.Validator.WRONG_FORMAT_ERROR
    }
]


class TestAgeValidator(TestCase):

    def setUp(self) -> None:
        self.validator = age.Validator()
        self.validator.current_year = 2021  # Seal the current year so that tests don't break in the future

    def test_validation(self):
        for idx, case in enumerate(testCases):
            with self.subTest(i=idx):
                self.validator.message(case["input"])
                validation_failure = self.validator.has_error()
                self.assertTrue(validation_failure) if case["has_errors"] is True else self.assertFalse(
                    validation_failure)

    def test_message(self):
        for idx, case in enumerate(testCases):
            with self.subTest(i=idx):
                msg = self.validator.message(case["input"])
                self.assertEqual(case["message"], msg)
