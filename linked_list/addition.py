""" Nodes in a list represent a number. Please implement a function/method to 
    add numbers in two lists, and store the sum into a new list.
    
    from : http://codercareer.blogspot.fr/2013/02/no-40-add-on-lists.html
"""
from node import List, Node, nodes_to_str
from reverse import reverse


def add(number1, number2, more=0):
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
            node = Node(current % 10, add(None, number2.next, current / 10))
        elif number2 == None:
            current = number1.data + more
            node = Node(current % 10, add(None, number1.next, current / 10))
        else:
            current = number1.data + number2.data + more
            node = Node(current % 10, 
                        add(number1.next, number2.next, current / 10))

    return node


def answer(number1, number2):
    """ :returns: a readable answer

        :param List number1: the linked list representing a number
        :param List number2: the linked list representing a number
    """
    str_number1 = str(number1)
    str_number2 = str(number2)

    added = add(reverse(number1.start), reverse(number2.start))

    return "{} + {} = {}".format(str_number1, 
                                 str_number2, 
                                 nodes_to_str(reverse(added)))


def main():
    """ Main function.
    """
    print(answer(List([4, 5, 6, 7]), List([1, 2, 3])))
    print(answer(List([1, 2, 3]), List([4, 5, 6, 7])))
    print(answer(List([0]), List([1, 2, 3])))
    print(answer(List([]), List([])))


if __name__ == '__main__':
    main()
