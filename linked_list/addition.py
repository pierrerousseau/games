""" Nodes in a list represent a number. Please implement a function/method to 
    add numbers in two lists, and store the sum into a new list.
    
    from : http://codercareer.blogspot.fr/2013/02/no-40-add-on-lists.html
"""
from node import List, Node, nodes_to_str
from reverse import reverse_aux as reverse


def add_aux(number1, number2, more=0):
    """ :returns: the result of the additon of <number1> and <number2>

        :param List number1: the linked list representing a number
        :param List number2: the linked list representing a number
        :param int more: a value to add (from previous number)
    """
    node = None
    if number1 == None and number2 == None:
        if more:
            node = Node(more, None)
    else:
        if number1 == None:
            current = number2.data + more
            node = Node(current % 10, add_aux(None, number2.next, current / 10))
        elif number2 == None:
            current = number1.data + more
            node = Node(current % 10, add_aux(None, number1.next, current / 10))
        else:
            current = number1.data + number2.data + more
            node = Node(current % 10, 
                        add_aux(number1.next, number2.next, current / 10))

    return node


def add(number1, number2):
    """ :returns: the result of the additon of <number1> and <number2>

        :param List number1: the linked list representing a number
        :param List number2: the linked list representing a number
    """
    str_number1 = str(number1)
    str_number2 = str(number2)
    added = add_aux(reverse(number1.start)[1], reverse(number2.start)[1])
    return "{} + {} = {}".format(str_number1, 
                                 str_number2, 
                                 nodes_to_str(reverse(added)[1]))


def main():
    """ Main function.
    """
    print(add(List([4, 5, 6, 7]), List([1, 2, 3])))
    print(add(List([1, 2, 3]), List([4, 5, 6, 7])))
    print(add(List([0]), List([1, 2, 3])))
    print(add(List([]), List([])))


if __name__ == '__main__':
    main()
