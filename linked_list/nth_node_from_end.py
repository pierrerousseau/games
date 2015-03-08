""" Get the Kth node from end of a linked list. 
    
    It counts from 1 here, so the 1st node from end is the tail of list.  For 
    instance, given a linked list with 6 nodes, whose value are 1, 2, 3, 4, 5, 
    6, its 3rd node from end is the node with value 4.

    from : http://codercareer.blogspot.fr/2011/10/no-10-k-th-node-from-end.html
"""
from node import List


def find_nth_from_end_aux(nodes, index):
    """ :returns: the kth node from the end of a linked list

        :param Node nodes: the start of a list of linked nodes.
        :param int index: the nth element from the end
    """
    current = (0, None)
    if nodes is not None:
        current_index, current_node = find_nth_from_end_aux(nodes.next, index)

        if current_index == index - 1:
            current = index + 1, str(nodes)
        else:
            current = current_index + 1, current_node

    return current 


def find_nth_from_end(nodes, index):
    """ :returns: the kth node from the end of a linked list

        :param Node nodes: the start of a list of linked nodes.
        :param int index: the nth element from the end
    """
    return find_nth_from_end_aux(nodes, index)[1]


def answer(nodes, index):
    """ :returns: a readable answer

        :param Node nodes: the start of a list of linked nodes.
        :param int index: the nth element from the end
    """
    nth = find_nth_from_end(nodes.start, index)

    return "{} from the end of {} is {}".format(index, nodes, nth)


if __name__ == '__main__':
    print(answer(List([1, 2, 3, 4, 5, 6]), 3))
    print(answer(List([1, 2, 3, 4, 5, 6]), 1))
    print(answer(List([1, 2, 3, 4, 5, 6]), 6))
    print(answer(List([1, 2, 3, 4, 5, 6]), 0))
    print(answer(List([1, 2, 3, 4, 5, 6]), 7))
