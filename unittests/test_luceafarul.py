import pprint
from anagrama import Anagram

__author__ = 'fauri'

with open("Luceafarul.txt") as f:
    poem = f.read()

    anagrams = Anagram(poem)
    pprint.pprint(anagrams.get_asc_sorted_anagrams())
