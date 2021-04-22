from unittest import TestCase
from ex_3.auto_return import auto_return_v1, auto_return_v2, auto_return_v3

test_string = 'Je suis une petite écrevisse d eau douce vivant dans des eaux sales.'


class TestAutoReturnV1(TestCase):

    def test_auto_return_v1__first_argument_is_str(self):
        self.assertEqual(test_string, auto_return_v1(test_string, 10))

    def test_auto_return_v1__second_argument_is_integer(self):
        self.assertEqual(test_string, auto_return_v1(test_string, 10))


class TestAutoReturnV2(TestCase):
    test_string_with_return = 'Je suis un\ne petite é\ncrevisse d\n eau douce\n vivant da\nns des eau\nx sales.'

    def test_auto_return_v2__line_length_is_not_more_than_parameter_line_length(self):
        concat_string = auto_return_v2(test_string, 10)
        self.assertEqual('\n', concat_string[10])


class TestAutoReturnV3(TestCase):
    test_string_with_return = 'Je suis une petite\nécrevisse d eau\ndouce vivant dans\ndes eaux sales.'

    def test_auto_return_v3__return_between_word(self):
        self.assertEqual(self.test_string_with_return, auto_return_v3(test_string, 20))
