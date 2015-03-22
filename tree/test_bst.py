""" Tests for basic bst package.
"""
import unittest

from binary_tree import Node, nodes_to_str, in_traversal, post_traversal, \
    pre_traversal
from bst import create_nodes, find_max, remove


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


    def test_find_max_1(self):
        """ find_max: find the max node of a bst
        """
        tree   = create_nodes([])
        result = None

        self.assertEquals(str(find_max(tree)), str(result))


    def test_find_max_2(self):
        """ find_max: find the max node of a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        result = " 7 "

        self.assertEquals(str(find_max(tree)), result)


    def test_find_max_3(self):
        """ find_max: find the max node of a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5])
        result = " 6 "

        self.assertEquals(str(find_max(tree)), result)


    def test_remove_1(self):
        """ remove: remove a node from a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        clean  = remove(7, tree)

        self.assertEquals(in_traversal(clean), [1, 2, 3, 4, 5, 6])

    def test_remove_2(self):
        """ remove: remove a leaf from a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        clean  = remove(8, tree)

        self.assertEquals(in_traversal(clean), [1, 2, 3, 4, 5, 6, 7])


    def test_remove_3(self):
        """ remove: remove a node from an empty bst
        """
        tree   = create_nodes([])
        clean  = remove(7, tree)

        self.assertEquals(in_traversal(clean), [])


    def test_remove_4(self):
        """ remove: remove root node from a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        clean  = remove(4, tree)

        self.assertEquals(in_traversal(clean), [1, 2, 3, 5, 6, 7])


    def test_remove_5(self):
        """ remove: remove a middle node from a bst
        """
        tree   = create_nodes([4, 2, 6, 3, 1, 5, 7])
        clean  = remove(5, tree)

        self.assertEquals(in_traversal(clean), [1, 2, 3, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
