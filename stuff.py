import unittest


class Tests(unittest.TestCase):

    def test_zero_does_not_exist(self):
        with self.assertRaises(NoZero):
            convert(0)

    def test_one_returns_I(self):
        self.assertEqual('I', convert(1))

    def test_two_returns_II(self):
        self.assertEqual('II', convert(2))

    def test_three_returns_III(self):
        self.assertEqual('III', convert(3))

    def test_four_returns_IV(self):
        self.assertEqual('IV', convert(4))

    def test_five_returns_V(self):
        self.assertEqual('V', convert(5))

    def test_six_returns_VI(self):
        self.assertEqual('VI', convert(6))

    def test_seven_returns_VII(self):
        self.assertEqual('VII', convert(7))

    def test_eight_returns_VIII(self):
        self.assertEqual('VIII', convert(8))

    def test_nine_returns_IX(self):
        self.assertEqual('IX', convert(9))

    def test_ten_returns_X(self):
        self.assertEqual('X', convert(10))

    def test_eleven_returns_XI(self):
        self.assertEqual('XI', convert(11))

    def test_twelve_returns_XII(self):
        self.assertEqual('XII', convert(12))

    def test_thirteen_returns_XIII(self):
        self.assertEqual('XIII', convert(13))

    def test_fourteen_returns_XIV(self):
        self.assertEqual('XIV', convert(14))

    def test_fifteen_returns_XV(self):
        self.assertEqual('XV', convert(15))

    def test_sixteen_returns_XVI(self):
        self.assertEqual('XVI', convert(16))

    def test_seventeen_returns_XVII(self):
        self.assertEqual('XVII', convert(17))

    def test_eighteen_returns_XVIII(self):
        self.assertEqual('XVIII', convert(18))

    def test_ninteen_returns_XIX(self):
        self.assertEqual('XIX', convert(19))

    def test_twenty_returns_XX(self):
        self.assertEqual('XX', convert(20))


class NoZero(Exception):
    pass


special_numbers = {
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    15: 'XV',
    19: 'XIX',
    20: 'XX',
}


def get_remainder(num):
    less = list(filter(lambda x: x < num, special_numbers.keys()))
    if less:
        return min(less, key=lambda y: abs(y-num))
    return 0


def convert(num):
    if num == 0:
        raise NoZero
    if num in special_numbers:
        return special_numbers[num]
    remainder = get_remainder(num)
    if remainder:
        return convert(remainder) + convert(num - remainder)
    return 'I' * num
