import re
from datetime import date
from typing import Final


class ValidationException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class Validator:
    MESSAGE_PATTERN: Final = "You're %d years old and you %s an adult"
    AFFIRMATIVE: Final = "are"
    NEGATIVE: Final = "aren't"

    WRONG_FORMAT_ERROR: Final = "Provide the year of birth in the four digit format"
    FUTURE_DATE_ERROR: Final = "You cannot insert future year"

    def __init__(self):
        self._regexp = re.compile('^\\d{4}$')
        self._current_year = date.today().year
        self._error: bool = False

    @property
    def current_year(self):
        return self._current_year

    @property
    def error(self):
        return self._error

    @current_year.setter
    def current_year(self, y):
        self._current_year = y

    def message(self, dob: str) -> str:
        try:
            self.validate(dob)
        except ValidationException as err:
            return err.msg

        age = self._current_year - int(dob)
        is_adult = age >= 18

        return self.MESSAGE_PATTERN % (age, self.AFFIRMATIVE if is_adult else self.NEGATIVE)

    def validate(self, dob: str):
        matches = self._regexp.match(dob)

        if matches is None:
            self._error = True
            raise ValidationException(self.WRONG_FORMAT_ERROR)

        if int(dob) > self._current_year:
            self._error = True
            raise ValidationException(self.FUTURE_DATE_ERROR)

    def has_error(self):
        return self._error is True
