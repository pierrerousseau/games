""" Suppose there are two singly linked lists both of which intersect at some 
    point and become a single linked list. The head pointers of both the 
    lists are known, but the intersecting node is not known. Give an 
    algorithm for finding the merging point.    

    from : Data Structures and Algorithms Made Easy, Narasimha Karumanchi
"""
from node import List, Node, len_nodes


def intersect(nodes1, nodes2):
    """ :returns: a node where <nodes1> and <nodes2> intersect, or None

        :param Node nodes1: the starting node of a linked list
        :param Node nodes2: the starting node of a linked list
    """
    node = None
    if nodes1 and nodes2:
        len_nodes1 = len_nodes(nodes1)
        len_nodes2 = len_nodes(nodes2)
        diff       = abs(len_nodes1 - len_nodes2)

        if len_nodes1 > len_nodes2:
            while nodes1 and diff:
                nodes1 = nodes1.next
                diff -= 1
        else:
            while nodes2 and diff:
                nodes2 = nodes2.next
                diff -= 1

        while nodes1 and nodes2 and nodes1 != nodes2:
            nodes1 = nodes1.next
            nodes2 = nodes2.next
        node = nodes1

    return node


def answer(linked_list1, linked_list2):
    """ :returns: a readable answer

        :param List linked_list1: a linked list
        :param List linked_list1: a second linked list
    """
    node = intersect(linked_list1.start, linked_list2.start)

    return "{} and {} intersect in {}".format(linked_list1, 
                                              linked_list2, 
                                              node)


def main():
    """ Main function.
    """
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node5 = Node(5, None)
    node6 = Node(6, None)

    print(answer(List([]), List([])))

    list1 = List([])
    node1.next = node2
    node2.next = node4
    node4.next = node5
    node5.next = node6
    list1.start = node1
    print(answer(list1, List([])))

    list2 = List([])
    list2.start = node3
    print(answer(list1, list2))

    node3.next = node4
    print(answer(list1, list2))

if __name__ == '__main__':
    main()
