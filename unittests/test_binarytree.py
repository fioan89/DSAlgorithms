__author__ = 'fauri'
import unittest

TREE_SEQUENCE = [(5,"five"),(3, "three"), (7, "seven"), (1, "one"), (4, "four"), (8, "eight"), (2, "two"), (9, "nine"), (6, "six"), (0, "zero")]
class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.binary_tree = BinaryTree()

    def test_len(self):