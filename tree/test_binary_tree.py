""" Tests for basic binary_tree package.
"""
import unittest

from binary_tree import Node, create_nodes, height, in_traversal, \
    min_height, nodes_to_str, post_traversal, pre_traversal


class TestNode(unittest.TestCase):
    """ Class for testing.
    """

    def setUp(self):
        pass

    def test_height_1(self):
        """ height(nodes): the height of an empty binary tree
        """
        tree = None

        self.assertEquals(height(tree), 0)


    def test_height_2(self):
        """ height(nodes): the height of a non empty binary tree
        """
        tree = Node(4, Node(3, Node(2), None), Node(7))

        self.assertEquals(height(tree), 3)

    def test_min_height_1(self):
        """ height(nodes): the min height of a non empty binary tree
        """
        tree = Node(4, Node(3, Node(2), None), Node(7))

        self.assertEquals(min_height(tree), 2)

    def test_min_height_2(self):
        """ height(nodes): the min height of a non empty binary tree
        """
        tree = Node(4, Node(3), Node(7, Node(3)))

        self.assertEquals(min_height(tree), 2)

    def test_nodes_to_str_1(self):
        """ nodes_to_str: convert a binary tree into a string
        """
        tree   = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
        result = "           4 \n" + \
            "     2           6 \n" + \
            "  1     3     5     7 \n"

        self.assertEquals(nodes_to_str(tree), result)


    def test_create_nodes(self):
        """ create_nodes: create a binary tree from a list
        """
        node_list = [4, 2, 6, 3, 1, 5, 7]
        tree = Node(4, Node(2, Node(3), Node(1)), Node(6, Node(5), Node(7)))

        self.assertEquals(nodes_to_str(tree),
                          nodes_to_str(create_nodes(node_list)))


    def test_pre_traversal(self):
        """ pre_traversal: traverse the binary tree by pre order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [4, 2, 3, 1, 6, 5, 7]

        self.assertEquals(pre_traversal(tree), result)


    def test_in_traversal(self):
        """ in_traversal: traverse the binary tree by in order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [3, 2, 1, 4, 5, 6, 7]

        self.assertEquals(in_traversal(tree), result)


    def test_post_traversal(self):
        """ post_traversal: traverse the binary tree by post order
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [3, 1, 2, 5, 7, 6, 4]

        self.assertEquals(post_traversal(tree), result)


if __name__ == '__main__':
    unittest.main()
