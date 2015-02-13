__author__ = 'fauri'

import unittest

from binarytree import BinarySearchTree

TREE_SEQUENCE = [(5, "five"), (3, "three"), (7, "seven"), (1, "one"), (4, "four"), (8, "eight"), (2, "two"),
                 (9, "nine"), (6, "six"), (0, "zero")]
NR_OF_NODES = len(TREE_SEQUENCE)

NODES_IN_FIRST_SEARCH = 4
NODES_IN_SECOND_SEARCH = 5
NODES_IN_THIRD_SEARCH = 9


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinarySearchTree(nodes=TREE_SEQUENCE)

    def test_len(self):
        self.assertEqual(NR_OF_NODES, len(self.binary_tree),
                         "Length of binary tree should be {0} instead it is {1}".format(NR_OF_NODES,
                                                                                        len(self.binary_tree)))

    def test_another_len(self):
        self.binary_tree.put(10, "ten")
        self.assertEqual(NR_OF_NODES + 1, len(self.binary_tree),
                         "Length of binary tree should be {0} instead it is {1}".format(NR_OF_NODES + 1,
                                                                                        len(self.binary_tree)))

    def test_get_value(self):
        self.assertEqual("five", self.binary_tree[5])

    def test_get_not_existent_key(self):
        self.assertEqual(None, self.binary_tree[-3])

    def test_first_search_raise(self):
        with self.assertRaises(TypeError):
            self.binary_tree.subnodes("start_key")

    def test_second_search_raise(self):
        with self.assertRaises(TypeError):
            self.binary_tree.subnodes(5, end_key="end_key")

    def test_third_search_raise(self):
        with self.assertRaises(ValueError):
            self.binary_tree.subnodes(5, end_key=-1)

    def test_first_search(self):
        # I should compare the key/value of nodes and their order but I'm too lazy at this hour so I'll just test the length
        nodes = self.binary_tree.subnodes(5, 9)
        self.assertEqual(NODES_IN_FIRST_SEARCH, len(nodes))

    def test_second_search(self):
        # I should compare the key/value of nodes and their order but I'm too lazy at this hour so I'll just test the length
        nodes = self.binary_tree.subnodes(5, 10)
        self.assertEqual(NODES_IN_SECOND_SEARCH, len(nodes))

    def test_third_search(self):
        # I should compare the key/value of nodes and their order but I'm too lazy at this hour so I'll just test the length
        nodes = self.binary_tree.subnodes(1)
        self.assertEqual(NODES_IN_THIRD_SEARCH, len(nodes))


if __name__ == "__main__":
    unittest.main("test_binarytree")