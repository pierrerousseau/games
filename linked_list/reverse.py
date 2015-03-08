""" Implement a function to reverse a linked list, and return the head of the 
    reversed list.
    
    from : http://codercareer.blogspot.fr/2011/10/no-18-reverse-linked-list.html
"""
from node import List


def reverse_aux(nodes):
    """ :returns: a couple : end, start of the reversed list

        :param Node nodes: the start of a list of linked nodes.
    """
    head = None
    if nodes is not None:
        previous, head = reverse_aux(nodes.next)
        if previous is None:
            head = nodes
        else:
            previous.next = nodes
        nodes.next = None

    return nodes, head 


def reverse(nodes):
    """ :returns: the reversed list of <nodes>

        :param Node nodes: the start of a list of linked nodes.
    """
    return reverse_aux(nodes)[1]


def answer(nodes):
    """ :returns: a readable answer

        :param List nodes: the linked list to reverse.
    """
    message = "reverse of {} is ".format(nodes)
    reversed_list       = List([])
    reversed_list.start = reverse(nodes.start)

    return message + str(reversed_list)


if __name__ == '__main__':
    print(answer(List([])))
    print(answer(List([1])))
    print(answer(List([1, 2, 3, 4, 5, 6])))
