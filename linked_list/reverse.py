""" Implement a function to reverse a linked list, and return the head of the 
    reversed list.
    
    from : http://codercareer.blogspot.fr/2011/10/no-18-reverse-linked-list.html
"""
from node import List


def reverse(nodes):
    """ :returns: the reversed list of <nodes>

        :param Node nodes: the start of a list of linked nodes.
    """
    head = None
    if nodes is None or nodes.next is None:
        head = nodes
    else:
        # head point to the start of reversed list
        # tail is (will be) the end of the reversed list
        tail       = nodes.next
        nodes.next = None
        head       = reverse(tail)
        tail.next  = nodes
    
    return head


def answer(linked_list):
    """ :returns: a readable answer

        :param List nodes: the linked list to reverse.
    """
    start_list        = str(linked_list)
    linked_list.start = reverse(linked_list.start)

    return "reverse of {} is {}".format(start_list, linked_list)


if __name__ == '__main__':
    print(answer(List([])))
    print(answer(List([1])))
    print(answer(List([1, 2, 3, 4, 5, 6])))
