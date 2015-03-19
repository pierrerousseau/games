""" Tests for basic bst package.
"""
import unittest

from binary_tree import Node, nodes_to_str, in_traversal, post_traversal, \
    pre_traversal
from bst import create_nodes


class TestNode(unittest.TestCase):
    """ Class for testing.
    """

    def setUp(self):
        pass

    def test_create_nodes(self):
        """ create_nodes: create a bst from a list
        """
        node_list = [4, 2, 6, 3, 1, 5, 7]
        bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

        self.assertEquals(nodes_to_str(bst),
                          nodes_to_str(create_nodes(node_list)))


    def test_pre_traversal(self):
        """ pre_traversal: traverse the binary tree by pre order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [4, 2, 1, 3, 6, 5, 7]

        self.assertEquals(pre_traversal(tree), result)


    def test_in_traversal(self):
        """ in_traversal: traverse the binary tree by in order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [1, 2, 3, 4, 5, 6, 7]

        self.assertEquals(in_traversal(tree), result)


    def test_post_traversal(self):
        """ post_traversal: traverse the binary tree by post order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [1, 3, 2, 5, 7, 6, 4]

        self.assertEquals(post_traversal(tree), result)


if __name__ == '__main__':
    unittest.main()
