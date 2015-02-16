__author__ = 'fauri'

import sys


class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.__key = key
        self.__value = val
        self.__left_child = left
        self.__right_child = right
        self.parent = parent

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, value):
        self.__left_child = value

    @property
    def right_child(self):
        return self.__right_child

    @right_child.setter
    def right_child(self, value):
        self.__right_child = value

    def __iter__(self):
        # :) inorder recursive iteration
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self
            if self.right_child:
                for elem in self.right_child:
                    yield elem

    def __str__(self):
        return "({0}:{1})".format(self.__key, self.__value)


class BinarySearchTree(dict):
    def __init__(self, nodes=None):
        """
        :param nodes: a list of tuples where the first value is the key and the second is the payload associated to the key
        """
        self.__root = None
        self.__size = 0
        if nodes is not None:
            for key, value in nodes:
                self.put(key, value)

    def __len__(self):
        return self.__size

    def put(self, key, val):
        """
        Inserts a new key and the corresponding value in the tree. If there
        is no key in the tree this will become the root of the graph.

        :param key: int value as key
        :param val: any type as value
        """
        if self.__root:
            self.__recursive_put(key, val, self.__root)
        else:
            self.__root = Node(key, val)
        self.__size = self.__size + 1


    def get(self, key):
        """
        Finds a Node instance with given key.

        :param key: int value to search for
        :return: a Node instance if key is found in the three, None otherwise
        """
        if self.__root:
            node = self.__recursive_get(key, self.__root)
            if node:
                return node.value
            else:
                return None
        else:
            return None

    def get_depth_first_nodes(self):
        """
        Gets a list of Nodes instances from the Tree by using depth first algorithm.
        """
        stack = []
        return self.__recursive_depth_first_traversal(self.__root, stack)

    def subnodes(self, start_key, end_key=sys.maxint):
        """
        Returns a list of nodes greater or equal than start_key, and lower than end_key if provided.
        :param start_key: a int number
        :param end_key: an int number greater than start_key. If this is not provided than all keys greater or
        equal to start_key will be provided
        :return: a list of Node instances
        """
        if not isinstance(start_key, int):
            raise TypeError("start_key should be int type")
        if not isinstance(end_key, int):
            raise TypeError("end_index should be int type")
        if (start_key > end_key):
            raise ValueError("start_key should have a lower value than end_key")

        nodes = self.get_depth_first_nodes()
        return [node for node in nodes if node.key >= start_key and node.key < end_key]


    def __recursive_depth_first_traversal(self, start_node, stack):
        stack.append(start_node)
        for node in start_node:
            if not node in stack:
                stack = self.__recursive_depth_first_traversal(node, stack)
        return stack

    def __recursive_put(self, key, val, current_node):
        """ Insert a key and value by recursively traversing the tree starting from current node."""

        if key < current_node.key:
            if current_node.left_child:
                self.__recursive_put(key, val, current_node.left_child)
            else:
                current_node.left_child = Node(key, val, parent=current_node)
        else:
            if current_node.right_child:
                self.__recursive_put(key, val, current_node.right_child)
            else:
                current_node.right_child = Node(key, val, parent=current_node)

    def __recursive_get(self, key, current_node):
        """ Searches for the key recursively starting from current node"""
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.__recursive_get(key, current_node.left_child)
        else:
            return self.__recursive_get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, k, v):
        self.put(k, v)


    def __str__(self):
        nodes = self.get_depth_first_nodes()
        to_ret = ""
        for node in nodes:
            to_ret += "{0}, ".format(node)
        return to_ret