""" Find all permutations of a string. For simplicity assume that each
    occurence of a character is a different character. Permutations of "aaa"
    is six times "aaa".

    from : Data Structures and Algorithms Made Easy, Narasimha Karumanchi
"""
import math

def permutations(string):
    """ :returns: all permutations of <string>

        :param str string: a string
    """
    found = []

    len_string = len(string)
    if len_string == 0:
        found = [""]
    elif len_string:
        first           = string[0]
        for word in permutations(string[1:]):
            for index in range(len(word) + 1):
                found.append(word[:index] + first + word[index:])

    return found


def answer(string):
    """ :returns: a readable answer of all permutations of string

        :param str string: a string
    """
    found   = permutations(string)
    to_find = math.factorial(len(string))
    correct = len(found) == to_find,
    return "all permutations of {} are {} ({}, {})".format(string,
                                                           found,
                                                           correct,
                                                           to_find)


if __name__ == '__main__':
    print(answer("ab"))
    print(answer("abc"))
    print(answer("abcd"))
    print(answer(""))
    print(answer("aaa"))
