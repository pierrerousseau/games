""" Find all combination of a string. For simplicity assume that each
    occurence of a character is a different character. Combinations of "aaa"
    is three times "aaa".

    from : Data Structures and Algorithms Made Easy, Narasimha Karumanchi
"""
import math

def combinations(string):
    """ :returns: all combinations of <string>

        :param str string: a string
    """
    found = []

    len_string = len(string)
    if len_string == 1:
        found = [string]
    elif len_string:
        first = string[0]
        subs  = combinations(string[1:])
        for word in subs:
            found.append(first + word)
        found += [first] + subs

    return found


def answer(string):
    """ :returns: a readable answer of all combinations of string

        :param str string: a string
    """
    found      = combinations(string)
    to_find    = 0
    len_string = len(string)
    for nb_letters in range(len_string):
        to_find += math.factorial(len_string) / \
            (math.factorial(nb_letters) *
             math.factorial(len_string - nb_letters))
    correct = len(found) == to_find,
    return "all combinations of {} are {} ({}, {})".format(string,
                                                           found,
                                                           correct,
                                                           to_find)


if __name__ == '__main__':
    print(answer("ab"))
    print(answer("abc"))
    print(answer("abcd"))
    print(answer(""))
    print(answer("aaa"))
