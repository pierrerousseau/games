""" Given an image represented by an NxN matrix, write a method to rotate the 
    image by 90 degrees. Can you do this in place?

    from : Craking the Coding Interview, 4th edition, Gayle Laakmann
"""

# Constants

#: character to end a line
END_LINE = "\n"
#: size of an elem to print
ELEM_SIZE = 3

# // Constants

def rotate(matrix, depth=0):
    """ :returns: the matrix after rotation by 90 degrees

        :param list matrix: a matrix
    """
    last = len(matrix) - depth - 1

    if last:
        for index in range(depth, last):
            lastindex = last - index + depth
            tmp                      = matrix[depth][index]
            matrix[depth][index]     = matrix[index][last]
            matrix[index][last]      = matrix[last][lastindex]
            matrix[last][lastindex]  = matrix[lastindex][depth]
            matrix[lastindex][depth] = tmp

        rotate(matrix, depth + 1)

    return matrix


def matrix_to_str(matrix, end_line=END_LINE, elem_size=ELEM_SIZE):
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


def answer(matrix):
    """ :returns: a readable answer

        :param list matrix: a matrix
    """
    str_matrix  = matrix_to_str(matrix)
    rotate(matrix)
    str_rotated = matrix_to_str(matrix)

    return "{} \n rotated is \n\n{}".format(str_matrix, str_rotated)


if __name__ == "__main__":
    mat = [
        [ 0,  1,  2,  3,  4, 5],
        [ 6,  7,  8,  9, 10, 11],
        [12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29],
        [29, 30, 31, 32, 33, 34],
    ]
    print(answer(mat))
