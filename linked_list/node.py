""" Basic linked list data structure and functions.
"""


class Node(object):
    """ A node of a linked list.
    """
    def __init__(self, data, next_node=None):
        """ Node constructor.

            :param data: the data of the node
            :param Node next_node: the next node in the list
        """
        self.data = data
        self.next = next_node

    def __str__(self):
        """ To convert into str.
        """
        return str(self.data)


def nodes_to_str(node):
    """ :returns: a str representing the linked list starting with <node>.

        :param Node node: the first node of a linked list
    """
    to_str = ""

    if node is not None:
        to_str = str(node) + nodes_to_str(node.next)

    return to_str


def create_nodes(data=None):
    """ Create a new linked list where each node represents a value of <data>.
        (initial python list order is kept)

        :returns: the first node of a linked list

        :param list data: a python list containing the values of the elements
            to add to the created linked list

        raise TypeError if data is not a list
    """
    nodes = None

    if data:
        if not isinstance(data, list):
            raise TypeError

        nodes = Node(data[0], create_nodes(data[1:]))

    return nodes


def add_to_nodes(nodes, node, begining=False):
    """ Add a node at the begining or the end of a list of linked nodes.

        :returns: the new list of linked nodes

        :param Node nodes: the start node of a linked list of nodes
        :param Node node: the node to add
        :param bool begining: if true, the node is added at the begining of the
            list, else at the end (default behavior)
    """
    if begining or not nodes:
        node.next = nodes
        nodes     = node
    else:
        nodes.next = add_to_nodes(nodes.next, node, begining)

    return nodes


def remove_from_nodes(nodes, data, first=True):
    """ Remove nodes from a list of linked nodes.

        :returns: the new list of linked nodes

        :param Node nodes: the start node of a linked list of nodes
        :param data: the value of the node to remove
        :param bool first if true, the only the first node with this value is
            removed, else all of them
    """
    if nodes:
        found = nodes.data == data
        if not (first and found):
            nodes.next = remove_from_nodes(nodes.next, data, first)
        if found:
            nodes = nodes.next

    return nodes


def len_nodes(nodes):
    """ :returns: the length of the linked list

        :param Node nodes: the start node of a linked list
    """
    length = 0
    if nodes is not None:
        length = 1 + len_nodes(nodes.next)

    return length


class List(object):
    """ Just to have a type for a linked list.
    """
    def __init__(self, data=None):
        """ List constructor.

            :param data: the initial data of the lists
        """
        self.start = create_nodes(data)

    def __str__(self):
        """ To convert into str.
        """
        return nodes_to_str(self.start)

    def __len__(self):
        """ for len()
        """
        return len_nodes(self.start)

    def add(self, node, begining=False):
        """ Add <node> to the list

            :param Node node: the node to add
            :param bool begining if true, the node is added at the begining of
                the list, else at the end (default behavior)
        """
        self.start = add_to_nodes(self.start, node, begining)

    def remove(self, data, first=True):
        """ Add <node> to the list

            :param data: the value of the node to remove
            :param bool first if true, the only the first node with this value
                is removed, else all of them
        """
        self.start = remove_from_nodes(self.start, data, first)
