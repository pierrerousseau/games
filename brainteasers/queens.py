""" Write an algorithm to print all ways of arranging eight queens on a chess
    board so that none of them share the same row, column or diagonal.

    from : Craking the Coding Interview, 4th edition, Gayle Laakmann
"""

# Constants

#: number of queens to place
NB_QUEENS = 8
#: how to display an empty cell
EMPTY     = " - "
#: how to display a cell with a queen
QUEEN     = " Q "
#: the character used to draw a title line
LINE      = "="
#: end of a row
END_LINE  = "\n"

# // Constants


def check_place(placed, col, row):
    """ :returns: True if the queen can be placed in (<col>, <row>)

        :param list placed: the queens already on the chessboard
        :param int col: a column number
        :param int row: a row number
    """
    is_allowed = True
    for i in range(0, col):
        diff       = abs(row - placed[i])
        is_allowed = diff and diff != abs(col - i)  # not same row or diagonal
        if not is_allowed:
            break

    return is_allowed


def place_queen(placed, col, nb_queens, found=None):
    """ Find all ways to place the queens.

        :param list placed: the queens already on the chessboard
        :param int col: the column where to place the queen
            (a queen per column)
        :param int nb_queens: the number of queens to place on the chessboard
        :param list found: the ways to place the queens already found.
    """
    if col == nb_queens:
        if found is None:
            found = [placed[:]]
        else:
            found.append(placed[:])
    else:
        for row in range(0, nb_queens):
            if check_place(placed, col, row):
                placed[col] = row
                found = place_queen(placed,
                                    col + 1,  # not the same column
                                    nb_queens,
                                    found)
                placed[col] = None

    return found


def place_queens(nb_queens):
    """ :returns: a list of all ways to place the queens
            for one way : a list of length nb_queens with index as column and
            value as row.

        :param int nb_queens: the number of queens to place on the chessboard
    """
    placed = [None] * nb_queens

    return place_queen(placed, 0, nb_queens)


def title(num, nb_queens, line=LINE):
    """ :returns: the title line of a chessboard

        :param int num: the number of the chessboard
        :param int nb_queens: the number of queens to place on the chessboard
    """
    line_size = (nb_queens - 1) * 3 - len(str(num))

    return str(num) + (line * line_size).rjust(line_size + 2)


def print_games(found, nb_queens, empty=EMPTY, queen=QUEEN, end_line=END_LINE):
    """ Print all ways to place the queens.

        :param list found: the result of <place_queens>
        :param int nb_queens: the number of queens to place on the chessboard
        :param str empty: how to display an empty cell
        :param str queen: how to display a cell with a queen
        :param str end_line: end of a line char
    """
    for index, placed in enumerate(found):
        game = title(index + 1, nb_queens) + end_line
        for col in range(0, nb_queens):
            for row in range(0, nb_queens):
                if placed[col] == row:
                    game += queen
                else:
                    game += empty
            game += end_line

        print(game)


if __name__ == '__main__':
    print_games(place_queens(NB_QUEENS), NB_QUEENS)
