""" Basic matrix data structure and functions.
"""

# Constants

#: character to end a line
END_LINE = "\n"
#: size of an elem to print
ELEM_SIZE = 3

# // Constants

def to_str(matrix, end_line=END_LINE, elem_size=ELEM_SIZE):
    """ :returns: string version of <matrix>

        :param list matrix: a matrix
        :param str end_line: end row character
        :param str elem_size: how many character to print an elemennt of the
            matrix
    """
    string = ""
    for row in matrix:
        for elem in row:
            string += str(elem).rjust(elem_size)
        string += end_line

    return string
