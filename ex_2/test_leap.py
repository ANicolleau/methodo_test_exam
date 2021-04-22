from unittest import TestCase
from leap_year import is_leap_year_v1, is_leap_year_v2, is_leap_year_v3, is_leap_year_v4


class LeapTestsV1(TestCase):
    def tests_leap_v1__year_is_integer(self):
        self.assertFalse(is_leap_year_v1([]))

    def test_leap_v1__year_is_in_str(self):
        self.assertTrue(is_leap_year_v1('2016'))


class LeapTestV2(TestCase):
    def test_leap_v2__is_leap_year(self):
        self.assertFalse(is_leap_year_v2(2015))
        self.assertTrue(is_leap_year_v2(2000))


class LeapTestV3(TestCase):
    def test_leap_v2__is_not_leap_year_divisible_by_100_not_divisible_by_400(self):
        self.assertFalse(is_leap_year_v3(1900))


class LeapTestV4(TestCase):
    def test_leap_v2__is_not_leap_year_divisible_by_4_not_divisible_by_100(self):
        self.assertFalse(is_leap_year_v4(2012))

    def test_leap_v2__is_not_leap_year(self):
        self.assertFalse(is_leap_year_v4(2019))
