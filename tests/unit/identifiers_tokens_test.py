import unittest
import sys
from lexer import Lexer

sys.path.append('../..')


def eat_tokens(line):
    lex = Lexer(line)
    line = ""
    while lex.getNextToken():
        line += lex.peekToken().test()
        if lex.peekToken().type in ["EOF", "ERROR"]:
            break
    return line


class IdentifiersTokensTest(unittest.TestCase):

    def test_simple_identifier(self):
        self.assertEqual(eat_tokens("foo"), "<IDENTIFIER=foo><EOF>")

    def test_underscore_identifier(self):
        self.assertEqual(eat_tokens("_foo"), "<IDENTIFIER=_foo><EOF>")

    def test_underscore_with_number_identifier(self):
        self.assertEqual(eat_tokens("_foo42"), "<IDENTIFIER=_foo42><EOF>")

    def test_double_underscore_with_number_identifier(self):
        self.assertEqual(eat_tokens("_foo__42"), "<IDENTIFIER=_foo__42><EOF>")

    def test_underscore_and_uppercase_identifier(self):
        self.assertEqual(eat_tokens("_FOO"), "<IDENTIFIER=_FOO><EOF>")

    def test_underscore_at_the_end_and_uppercase_identifier(self):
        self.assertEqual(eat_tokens("FOO_"), "<IDENTIFIER=FOO_><EOF>")

    def test_identifier_can_not_start_with_a_number(self):
        self.assertNotEqual(eat_tokens("5_FOO_"), "<IDENTIFIER=5_FOO_><EOF>")

    def test_31_characters(self):
        self.assertEqual(
                eat_tokens("this_is_a_very_long_identifier_"),
                "<IDENTIFIER=this_is_a_very_long_identifier_><EOF>")

    # def test_only_31_characters_are_significant(self):
    #     self.assertEqual(
    #             eat_tokens("this_is_a_very_long_identifier_this_should_not_count")
    #             ,
    #             "IDENTIFIER")
