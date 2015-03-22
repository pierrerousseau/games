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
        Time complexity : o(nlogn) / o(n2)

        :param list table: a list of values

    """
    if last is None:
        last = len(table) - 1
    if first < last:
        table, pivot = partition(table, first, last)
        table = quick_sort(table, first, pivot - 1)
        table = quick_sort(table, pivot + 1, last)

    return table


def heapify(table, index, last):
    """ :returns: <table> with table[index] at his place in its subtree

        Considers table as a tree with index linked to 2 * index and
        2 * index + 1
        And exchange index with max of its children, and start again until
        index is the maximum of its children.

        :param list table: a list
        :param int index: the max node to set
        :param int last: the last element of the tree to take into account
    """
    left  = (index + 1) * 2 - 1
    right = left + 1
    maxi  = index

    if left <= last and table[maxi] < table[left]:
        maxi = left
    if right <= last and table[maxi] < table[right]:
        maxi = right

    if maxi != index:
        table[index], table[maxi] = table[maxi], table[index]
        table = heapify(table, maxi, last)

    return table


def heap_sort(table):
    """ :returns: <table> sorted

        Use heap sort.
        Time complexity : o(nlogn)

        :param list table: a list of values
    """
    last = len(table) - 1
    # build a tree where each parent is > of its children
    for index in range(last / 2, 0, -1):
        table = heapify(table, index - 1, last)
    # set the table in order
    for index in range(last, 0, -1):
        table[0], table[index] = table[index], table[0]
        table = heapify(table, 0, index - 1)

    return table
