""" Tests for basic bst package.
"""
import unittest

from bst import Node, create_nodes, depth, in_traversal, nodes_to_str, \
    post_traversal, pre_traversal


class TestNode(unittest.TestCase):
    """ Class for testing.
    """

    def setUp(self):
        pass

    def test_depth_1(self):
        """ depth(nodes): the depth of an empty bst
        """
        bst = None

        self.assertEquals(depth(bst), 0)


    def test_depth_2(self):
        """ depth(nodes): the depth of a non empty bst
        """
        bst = Node(4, Node(3, Node(2), None), Node(7))

        self.assertEquals(depth(bst), 3)

    def test_nodes_to_str_1(self):
        """ nodes_to_str: convert a bst into a string
        """
        bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
        result = "           4 \n" + \
            "     2           6 \n" + \
            "  1     3     5     7 \n"

        self.assertEquals(nodes_to_str(bst), result)


    def test_create_nodes(self):
        """ create_nodes: create a bst from a list
        """
        node_list = [4, 2, 6, 3, 1, 5, 7]
        bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

        self.assertEquals(nodes_to_str(bst),
                          nodes_to_str(create_nodes(node_list)))


    def test_pre_traversal(self):
        """ pre_traversal: traverse the bst by pre order
        """
        bst    = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [4, 2, 1, 3, 6, 5, 7]

        self.assertEquals(pre_traversal(bst), result)


    def test_in_traversal(self):
        """ in_traversal: traverse the bst by in order
        """
        bst    = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [1, 2, 3, 4, 5, 6, 7]

        self.assertEquals(in_traversal(bst), result)


    def test_post_traversal(self):
        """ post_traversal: traverse the bst by post order
        """
        bst    = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = [1, 3, 2, 5, 7, 6, 4]

        self.assertEquals(post_traversal(bst), result)


if __name__ == '__main__':
    unittest.main()
