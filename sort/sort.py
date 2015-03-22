""" Implementation of sorting algorithms.
"""


def insertion_sort(table):
    """ :returns: <table> sorted

        Use insertion sort.
        Time complexity : o(n2)

        :param list table: a list of values

    """
    for index, elem in enumerate(table):
        jndex = index
        while jndex > 0 and table[jndex - 1] > elem:
            table[jndex] = table[jndex - 1]
            jndex -= 1
        table[jndex] = elem

    return table
