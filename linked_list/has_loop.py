""" How to check whether there is a loop in a linked list?
    
    from : http://codercareer.blogspot.fr/2012/01/no-29-loop-in-list.html
"""
from node import List, Node


def has_loop(slow_node, fast_node):
    """ :returns: True if <slow_node> meets <fast_node>

        :param Node slow_node: a node moving to next node at each step
        :param Node fast_node: a node moving to 2nd next node at each step
    """
    loop = False
    if slow_node is not None and fast_node is not None:
        fast_node = fast_node.next
        loop = slow_node == fast_node
        if not loop:
            slow_node = slow_node.next
            fast_node = fast_node.next
            loop = has_loop(slow_node, fast_node)

    return loop


def get_loop(node):
    """ :returns: the loop in the path starting from <node>

        To not pollute loop search with path construction

        :param Node node: a node starting a path with a loop
    """
    path      = []
    path_node = []
    path      = [str(node)] 
    while node not in path_node:
        path_node.append(node)
        node = node.next
        path.append(str(node))

    return path


def answer(linked_list):
    """ :returns: a readable answer

        :param List linked_list: a linked list to test for loops
    """
    slow_node = linked_list.start
    loop      = has_loop(slow_node, slow_node)

    path = []
    if loop:
        path = get_loop(linked_list.start)

    return "list has a loop ? {}, {}".format(loop, path)


def main():
    """ Main function.
    """
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node5 = Node(5, None)
    node6 = Node(6, None)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    list1 = List([])
    print(answer(list1))

    list1.start = node1
    print(answer(list1))

    node6.next = node3
    print(answer(list1))

    node6.next = node5
    print(answer(list1))

    node6.next = None
    node2.next = node1
    print(answer(list1))

    node2.next = node3
    node6.next = node1
    print(answer(list1))

    node6.next = None
    node4.next = node4
    print(answer(list1))


if __name__ == '__main__':
    main()
