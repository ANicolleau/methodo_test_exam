from unittest import TestCase
from ex_1.ex1 import join, average


class TestEx1(TestCase):
    def test_join__list_empty(self):
        concat_string = join([], ' ,')
        self.assertEqual('', concat_string)

    def test_join__is_not_type_list(self):
        concat_string = join({}, ' ,')
        self.assertIsNone(concat_string)

    def test_join__separator_is_not_str(self):
        concat_string = join([], 1)
        self.assertIsNone(concat_string)

    def test_join__join_work(self):
        concat_string = join(['Je', 'suis', 'Antoine'], ' ')
        self.assertEqual('Je suis Antoine', concat_string)

    def test_average__list_empty(self):
        self.assertEqual(0, average([]))

    def test_average__is_not_list(self):
        self.assertIsNone(average({}))

    def test_average__string_in_list(self):
        self.assertIsNone(average([1, 2, '3']))

    def test_average__working(self):
        self.assertEqual(5, average([5, 5, 5, 5, 5]))
