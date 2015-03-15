""" Find a given word in a matrix of letters.

    from : Data Structures and Algorithms Made Easy, Narasimha Karumanchi
"""
from matrix import to_str


def find_aux(word, matrix, row, col, path):
    """ :returns: the ordered coordinates of the letter of the <word>, or None

        :param str word: a string
        :param list matrix: a matrix of letters
        :param int row: the current row of the search
        :param int col: the current col of the search
        :param list path: the letter already found
    """
    full_path = None
    in_matrix = row < len(matrix) and col < len(matrix[0])
    if in_matrix and (row, col) not in path and word[0] == matrix[row][col]:
        step_path = path + [(row, col)]
        tail      = word[1:]
        if len(word) > 1:
            full_path = find_aux(tail, matrix, row + 1, col, step_path)
            if full_path is None:
                full_path = find_aux(tail, matrix, row - 1, col, step_path)
            if full_path is None:
                full_path = find_aux(tail, matrix, row, col + 1, step_path)
            if full_path is None:
                full_path = find_aux(tail, matrix, row, col - 1, step_path)
        else:
            full_path = step_path

    return full_path


def find(word, matrix):
    """ :returns: the ordered coordinates of the letter of the <word>, or None

        :param str word: a string
        :param list matrix: a matrix of letters
    """
    path = None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            path = find_aux(word, matrix, row, col, [])
            if path:
                break
        if path:
            break

    return path


def answer(word, matrix):
    """ :returns: a readable answer

        :param str word: a string
        :param list matrix: a matrix of letters
    """
    path = find(word, matrix)

    return "{}\n\n the path to find {} is {}\n\n".format(to_str(matrix),
                                                         word, 
                                                         path)


if __name__ == '__main__':
    mat = [
            ["h", "e", "l", "l", "o"],
            ["a", "b", "a", "c", "d"],
            ["a", "b", "f", "c", "d"],
            ["a", "b", "a", "c", "d"],
            ["a", "k", "b", "e", "d"],
            ["a", "o", "o", "e", "d"],
            ["b", "y", "b", "y", "e"]
    ]
    print(answer("hello", mat))
    print(answer("goodbye", mat))
    print(answer("facebook", [[]]))
    print(answer("facebook", mat))
    print(answer("bye", mat))
