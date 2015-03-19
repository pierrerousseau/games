""" Basic binary search tree data structure and functions.
"""
from binary_tree import Node

def add_to_nodes(nodes, node):
    """ Add a node to a bst.

        :returns: the root node of the bst

        :param Node nodes: the root node of a bst
        :param Node node: the node to add
    """
    if nodes:
        if node.data > nodes.data:
            nodes.right = add_to_nodes(nodes.right, node)
        elif node.data < nodes.data:
            nodes.left = add_to_nodes(nodes.left, node)
    else:
        nodes = node

    return nodes


def create_nodes(data=None):
    """ Create a bst list where each node represents a value of <data>.

        :returns: the root node of a bst

        :param list data: a list of values

        raise TypeError if data is not a list
    """
    nodes = None

    if data:
        if not isinstance(data, list):
            raise TypeError
        for elem in data:
            nodes = add_to_nodes(nodes, Node(elem))

    return nodes
