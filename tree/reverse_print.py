""" Give an algorithm for printing the level order data in reverse order.    

    from : Data Structures and Algorithms Made Easy, Narasimha Karumanchi
"""
from collections import deque

from binary_tree import create_nodes, nodes_to_str


def reverse(nodes):
    """ :returns: a list of nodes ordered by depth

        :param Node nodes: the root node of a binary tree
    """
    ordered = []
    if nodes:
        queue = deque()
        queue.append(nodes)
        stack = []
        while queue:
            current = queue.pop()
            if current.left is not None:
                queue.appendleft(current.left)
            if current.right is not None:
                queue.appendleft(current.right)
            stack.append(current)

        while stack:
            ordered.append(stack.pop().data)

    return ordered


def answer(nodes):
    """ :returns: a readable answer

        :param Node nodes: the root node of a binary tree
    """
    str_nodes = nodes_to_str(nodes)
    ordered   = reverse(nodes)

    return "{} is from leafs to root of \n{}".format(ordered, 
                                                     str_nodes)


if __name__ == '__main__':
    print(answer(create_nodes([1, 2, 3, 4, 5, 6])))
    print(answer(create_nodes([])))
    print(answer(create_nodes([1])))
    print(answer(create_nodes([1, 2, 3, 4, 5, 6, 7, 9, 8])))
