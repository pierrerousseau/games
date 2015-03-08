""" Write code to remove duplicates from an unsorted linked list.
    
    from : Craking the Coding Interview, 4th edition, Gayle Laakmann
"""
from node import List


def remove_duplicates(node, found):
    """ :returns: <nodes> without duplicated element
        
        :param List linked_list: an unsorted linked list
    """
    found[node.data] = True
    if node.next is not None:
        if node.next.data in found:
            node.next = node.next.next
            remove_duplicates(node, found)
        else:
            remove_duplicates(node.next, found)


def answer(linked_list):
    """ :returns: a readable answer
        
        :param List linked_list: an unsorted linked list
    """
    start_list = str(linked_list)
    remove_duplicates(linked_list.start, {})

    return "{} without duplicates {}".format(start_list, linked_list)


if __name__ == '__main__':
    print(answer(List([1, 2, 3, 4, 5, 6])))
    print(answer(List([2, 2, 2, 2, 2, 2])))
    print(answer(List([1, 1, 1, 4, 5, 6])))
    print(answer(List([1, 2, 1, 4, 5, 6])))
    print(answer(List([1, 2, 3, 2, 5, 6])))
    print(answer(List([1, 2, 3, 4, 6, 6])))
