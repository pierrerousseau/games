""" A string can be partitioned into some substrings, such that each 
    substring is a palindrome. For example, there are a few strategies to 
    split the string "abbab" into palindrome substrings, such as: 
    "abba"|"b", "a"|"b"|"bab" and "a"|"bb"|"a"|"b".

    from : http://codercareer.blogspot.fr/2013/02/no-43-minimal-number-of-splits-on-string.html
"""

def is_palindrome(word):
    """ :returns: True if <word> is a palindrome

        :param str word: a string
    """
    return word == word[::-1]


def palindrome_slices(word, nb_slices):
    """ :returns: True if all slices of <word> are palindromes

        :param str word: the word to slice
        :param int nb_slice: the number of slices to check
    """
    are_palindromes = []
    for start in range(0, len(word)):
        if nb_slices == 0:
            if is_palindrome(word):
                are_palindromes.append(word)
        else:
            if is_palindrome(word[:start]):
                others = palindrome_slices(word[start:],
                                           nb_slices - 1)
                if others:
                    are_palindromes = [word[:start]] + others
        if are_palindromes:
            break

    return are_palindromes


def first_palindrome(word):
    """ :returns: the number of slice to use to convert <word> into a list
            of palindrome

        :param str word: a string
    """
    nb_slices  = 0
    palindromes = []
    for nb_slices in range(0, len(word)):
        palindromes = palindrome_slices(word, nb_slices)
        if palindromes:
            break

    return nb_slices, palindromes


def answer(palindromes):
    """ :returns: a readable answer

        :param tuple palindromes: (number of slice, list of palydroms)
    """
    return "number of slice : {} ({})".format(palindromes[0], palindromes[1])


if __name__ == '__main__':
    print(answer(first_palindrome("cabbabc")))
    print(answer(first_palindrome("abbab")))
    print(answer(first_palindrome("")))
    print(answer(first_palindrome("a")))
    print(answer(first_palindrome("bbbbbbbbbbbbbbbb")))
    print(answer(first_palindrome("abcdefghik")))
