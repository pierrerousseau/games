""" A string can be partitioned into some substrings, such that each 
    substring is a palindrome. For example, there are a few strategies to 
    split the string "abbab" into palindrome substrings, such as: 
    "abba"|"b", "a"|"b"|"bab" and "a"|"bb"|"a"|"b".

    from : http://codercareer.blogspot.fr/2013/02/no-43-minimal-number-of-splits-on-string.html
"""

def is_palyndrom(word):
    """ :returns: True if <word> is a palyndrom

        :param str word: a string
    """
    return word == word[::-1]


def palyndrom_slices(word, nb_slices):
    """ :returns: True if all slices of <word> are palyndroms

        :param str word: the word to slice
        :param int nb_slice: the number of slices to check
    """
    are_palyndroms = []
    for start in range(0, len(word)):
        if nb_slices == 0:
            if is_palyndrom(word):
                are_palyndroms.append(word)
        else:
            if is_palyndrom(word[:start]):
                others = palyndrom_slices(word[start:],
                                          nb_slices - 1)
                if others:
                    are_palyndroms = [word[:start]] + others
        if are_palyndroms:
            break

    return are_palyndroms


def first_palyndrom(word):
    """ :returns: the number of slice to use to convert <word> into a list
            of palyndrom

        :param str word: a string
    """
    nb_slices  = 0
    palyndroms = []
    for nb_slices in range(0, len(word)):
        palyndroms = palyndrom_slices(word, nb_slices)
        if palyndroms:
            break

    return nb_slices, palyndroms


def answer(palyndroms):
    """ :returns: a readable answer

        :param tuple palyndroms: (number of slice, list of palydroms)
    """
    return "number of slice : {} ({})".format(palyndroms[0], palyndroms[1])


if __name__ == '__main__':
    print(answer(first_palyndrom("cabbabc")))
    print(answer(first_palyndrom("abbab")))
    print(answer(first_palyndrom("")))
    print(answer(first_palyndrom("a")))
    print(answer(first_palyndrom("bbbbbbbbbbbbbbbb")))
    print(answer(first_palyndrom("abcdefghik")))
