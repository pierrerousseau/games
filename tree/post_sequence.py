""" Determine whether an input array is a post-order traversal sequence of
    a binary tree or not.

    from : http://codercareer.blogspot.fr/2011/09/no-06-post-order-traversal-sequences-of.html
"""
from binary_tree import nodes_to_str
from bst import create_nodes


def is_post_sequence(sequence):
    """ :returns: True if <sequence> is the output of a post traversal of a bst

        :param list sequence: a list of element of a bst
    """
    is_post = True

    if sequence:
        left  = []
        right = []
        root  = sequence[-1]

        current = 0
        for index, elem in enumerate(sequence[:-1]):
            if elem > root:
                break
            left.append(elem)
            current = index + 1

        for elem in sequence[current:-1]:
            if elem < root:
                is_post = False
                break

        if is_post:
            is_post = is_post_sequence(left) and is_post_sequence(right)

    return is_post


def answer(sequence):
    """ :returns: a readable answer

        :param list sequence: a sequence of a values
    """
    is_post = "is" if is_post_sequence(sequence) else "is not"

    return "{} {} a post order traversal of a bst".format(sequence, is_post)


if __name__ == '__main__':
    print(answer([]))
    print(answer([5, 6, 7, 9, 11, 10, 8]))
    print(answer([5, 6, 7, 9, 10, 11, 8]))
    print(answer([7, 5, 6, 9, 10, 11, 8]))
    print(answer([9, 10, 8]))
