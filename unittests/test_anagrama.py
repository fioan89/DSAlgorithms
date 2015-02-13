__author__ = 'fauri'
import unittest
from anagrama import Anagram

WORDS_1 = "ioan naoi oani iano ioam moai"
WORDS_2 = "ioan naoi oani iano ioam moai ioan"

ANAGRAMS_1 = [('moai', 1), ('ioam', 1), ('naoi', 3), ('iano', 3), ('oani', 3), ('ioan', 3)]
ANAGRAMS_2 = [('moai', 1), ('ioam', 1), ('ioan', 3), ('naoi', 4), ('iano', 4), ('oani', 4)]


class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.angrams_1 = Anagram(WORDS_1)
        self.angrams_2 = Anagram(WORDS_2)

    def test_first_anagram(self):
        anagrams = self.angrams_1.get_asc_sorted_anagrams()
        self.assertEqual(ANAGRAMS_1, anagrams)

    def test_second_anagram(self):
        anagrams = self.angrams_2.get_asc_sorted_anagrams()
        self.assertEqual(ANAGRAMS_2, anagrams)

