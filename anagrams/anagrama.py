import collections

__author__ = 'fauri'


class Anagram():
    """
    Class for building a list of lower case words and the number of anagrams found in the phrase.
    Same words do not count as anagrams.
    """

    def __init__(self, phrase_block):
        self.__phrase_block = phrase_block
        self.__all_words = self.__get_words()
        self.__unique_words = set(self.__all_words)

    def __get_words(self):
        """
        Get a list of all words in from the internal string block as lowercase values.
        """
        words = self.__phrase_block.split()
        return map(lambda x: x.lower().strip(), words)

    def __have_same_chars(self, first_word, second_word):
        """
         Returns True if second word contains the same chars as the first word, without any additional ones.
        """
        if len(first_word) != len(second_word):
            return False

        for character in first_word:
            if character not in second_word:
                return False
        return True

    def get_anagrams(self):
        """
        Returns a list of words and their count of anagrams.
        """
        anagrams = []
        # keep a map of word length and all words that have the same length
        length_map = collections.defaultdict(list)
        for word in self.__all_words:
            length_map[len(word)].append(word)

        # take all unique words and find out the anagrams
        # the algorithm is really simple: first get a list of words that have the same length
        # and then check each word if they have the same chars
        for word in self.__unique_words:
            potentially_anagrams = length_map[len(word)]
            count = 0
            for potentially_anagram in potentially_anagrams:
                if not word == potentially_anagram and self.__have_same_chars(word, potentially_anagram):
                    count += 1
            anagrams.append((word, count))
        return anagrams

    def get_asc_sorted_anagrams(self):
        """
        Returns a list of words and their count of anagrams sorted ascending by the count of anagrams
        """
        return filter(lambda (x,y): y>0, sorted(self.get_anagrams(), key=lambda tup: tup[1]))


if __name__ == "__main__":
    words = "ioan naoi oani iano ioam moai ioan"
    anagram = Anagram(words)
    print anagram.get_asc_sorted_anagrams()
