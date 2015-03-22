""" Tests for basic sorting algorithms.
"""
import unittest

from sort import heap_sort, insertion_sort, quick_sort


class TestNode(unittest.TestCase):
    """ Class for testing.
    """

    def setUp(self):
        pass

    def test_insertion_sort_1(self):
        """ insertion_sort: sort a lsit
        """
        self.assertEquals(insertion_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])


    def test_insertion_sort_2(self):
        """ insertion_sort: sort an empty list
        """
        self.assertEquals(insertion_sort([]), [])


    def test_insertion_sort_3(self):
        """ insertion_sort: sort sorted list
        """
        self.assertEquals(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


    def test_insertion_sort_4(self):
        """ insertion_sort: sort reversed list
        """
        self.assertEquals(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


    def test_quick_sort_1(self):
        """ quick_sort: sort a lsit
        """
        self.assertEquals(quick_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])


    def test_quick_sort_2(self):
        """ quick_sort: sort an empty list
        """
        self.assertEquals(quick_sort([]), [])


    def test_quick_sort_3(self):
        """ quick_sort: sort sorted list
        """
        self.assertEquals(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


    def test_quick_sort_4(self):
        """ quick_sort: sort reversed list
        """
        self.assertEquals(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


    def test_heap_sort_1(self):
        """ heap_sort: sort a lsit
        """
        self.assertEquals(heap_sort([5, 1, 2, 4, 3]), [1, 2, 3, 4, 5])


    def test_heap_sort_2(self):
        """ heap_sort: sort an empty list
        """
        self.assertEquals(heap_sort([]), [])


    def test_heap_sort_3(self):
        """ heap_sort: sort sorted list
        """
        self.assertEquals(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


    def test_heap_sort_4(self):
        """ heap_sort: sort reversed list
        """
        self.assertEquals(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
