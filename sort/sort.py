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


def partition(table, first, last):
    """ :returns: table, pivot with pivot a element of table at its sorted 
            place

        :param list table: a list
        :param int first: first index of the list to take into account
        :param int last: last index of the list to take into account
    """
    pivot = (first + last) / 2

    table[pivot], table[last] = table[last], table[pivot]
    index = first
    for jndex in range(first, last):
        if table[jndex] <= table[last]:
            table[index], table[jndex] = table[jndex], table[index]
            index += 1
    table[index], table[last] = table[last], table[index]

    return table, index


def quick_sort(table, first=0, last=None):
    """ :returns: <table> sorted

        Use quick sort.
        Time complexity : o(nlogn)

        :param list table: a list of values

    """
    if last is None:
        last = len(table) - 1
    if first < last:
        table, pivot = partition(table, first, last)
        table = quick_sort(table, first, pivot - 1)
        table = quick_sort(table, pivot + 1, last)

    return table
