""" Basic binary tree data structure and functions.
"""

# Constants

#: characters of line ending
END_LINE = "\n"

#: length for a string of a printed node
LEN_NODE = 3

# // Constants


class Node(object):
    """ A binary search tree node.
    """
    def __init__(self, data, left=None, right=None):
        """ Constructor.

            :param data: the data of the node
            :param Node left: the left subtree first node
            :param Node right: the right subtree first node
        """
        self.data  = data
        self.left  = left
        self.right = right

    def __str__(self, len_node=LEN_NODE):
        """ To convert into str.
        """
        return str(self.data).center(len_node)


def min_height(nodes):
    """ :returns: the minimum height of the binary tree

        :param Node nodes: the root node of a binary tree
    """
    current_height = 0

    if nodes is not None:
        current_height = min(height(nodes.left), height(nodes.right)) + 1


    return current_height


def height(nodes):
    """ :returns: the height of the binary tree

        :param Node nodes: the root node of a binary tree
    """
    current_height = 0

    if nodes is not None:
        current_height = max(height(nodes.left), height(nodes.right)) + 1


    return current_height


def nodes_to_str(nodes, len_node=LEN_NODE, end_line=END_LINE, blank=" "):
    """ :returns: a str representing the binary tree starting with <node>.

        :param Node nodes: the root node of a binary tree
    """
    to_str = ""

    bt_height = height(nodes)
    nodes     = [nodes]
    while bt_height:
        blanks     = blank * (2 ** bt_height - 1) * len_node
        next_nodes = []
        for index, node in enumerate(nodes):
            if node is None:
                data = blank * len_node
            else:
                data = str(node)
            if index == 0:
                to_str += blanks[:-len(blanks) / 2] + data
            else:
                to_str += blanks + data

            if node:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
        to_str += end_line

        nodes      = next_nodes
        bt_height -= 1

    return to_str


def add_to_nodes(nodes, node):
    """ Add a node to a binary tree.

        :returns: the root node of the binary tree

        :param Node nodes: the root node of a binary tree
        :param Node node: the node to add
    """
    if nodes:
        if min_height(nodes.left) <= min_height(nodes.right):
            nodes.left = add_to_nodes(nodes.left, node)
        else:
            nodes.right = add_to_nodes(nodes.right, node)
    else:
        nodes = node

    return nodes


def create_nodes(data=None):
    """ Create a binary tree list where each node represents a value of <data>.

        :returns: the root node of a binary tree

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


def pre_traversal(nodes, current=None):
    """ Traversal the binary tree.

        :returns: the list of the nodes in order of traversal

        :param Node nodes: the root node of the binary tree
    """
    if current is None:
        current = []

    if nodes is not None:
        current.append(nodes.data)
        current = pre_traversal(nodes.left, current)
        current = pre_traversal(nodes.right, current)

    return current


def in_traversal(nodes, current=None):
    """ Traversal the binary tree.

        :returns: the list of the nodes in order of traversal

        :param Node nodes: the root node of the binary tree
    """
    if current is None:
        current = []

    if nodes is not None:
        current = in_traversal(nodes.left, current)
        current.append(nodes.data)
        current = in_traversal(nodes.right, current)

    return current


def post_traversal(nodes, current=None):
    """ Traversal the binary tree.

        :returns: the list of the nodes in order of traversal

        :param Node nodes: the root node of the binary tree
    """
    if current is None:
        current = []

    if nodes is not None:
        current = post_traversal(nodes.left, current)
        current = post_traversal(nodes.right, current)
        current.append(nodes.data)

    return current
