""" Remove all duplicates from a list.
"""
def pythonic_remove(table):
    """ :returns: <table> without duplicates

        Do it using a pythonic idiom.

        :param list table: an array
    """
    return list(set(table))


def answer(table, version=0):
    """ :returns: a readable answer of a call to one of the function removing
            duplicates from a list

        :param list table: an array
        :param int version: le version of the answer to use
    """
    no_duplicates = pythonic_remove(table)
    return "{} without duplicates is {}".format(table, no_duplicates)


if __name__ == '__main__':
    print(answer([1, 2]))
    print(answer([2, 1]))
    print(answer([]))
    print(answer([1]))
    print(answer([1, 1, 1, 1, 1]))
    print(answer([1, 2, 1]))
    print(answer([1, 1, 2, 2]))
    print(answer([2, 1, 3, 4, 5, 6, 1, 7, 8, 2]))
