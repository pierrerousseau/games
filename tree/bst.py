""" Basic binary search tree data structure and functions.
"""
from binary_tree import Node, nodes_to_str

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


def find_max(nodes):
    """ :returns: the node with the maximum value of the bst

        :param Node nodes: the root node of a bst
    """
    max_node = nodes
    if max_node is not None and max_node.right is not None:
        max_node = find_max(nodes.right)

    return max_node


def remove(value, nodes):
    """ :returns: <nodes> without <node>

        :param int value: the data of the node to remove
        :parma Node nodes: the root node of a bst
    """
    if nodes is not None:
        if value > nodes.data:
            nodes.right = remove(value, nodes.right)
        elif value < nodes.data:
            nodes.left = remove(value, nodes.left)
        else:
            if nodes.left:
                max_smaller       = find_max(nodes.left)
                max_smaller.left  = remove(max_smaller.data, nodes.left)
                max_smaller.right = nodes.right
                nodes = max_smaller
            else:
                nodes = nodes.right

    return nodes
