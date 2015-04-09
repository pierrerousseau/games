""" Assume you have a method isSubstring which checks if one word is a 
    substring of another. Given two strings, s1 and s2, write code to check 
    if s2 is a rotation of s1 using only one call to isSubstring 
    (i.e., "waterbottle" is a rotation of "erbottlewat").

    from : Craking the Coding Interview, 4th edition, Gayle Laakmann
"""

def is_rotation(word1, word2):
    """ :returns: True if <word1> a rotation of <word2>

        :param str word1: a string
        :param str word2: a string
    """
    return word1 in word2 + word2


def answer(word1, word2):
    """ :returns: a readable answer to the question is <word1> a rotation of
            <word2>

        :param str word1: a string
        :param str word2: a string
    """
    is_or_not = "is" if is_rotation(word1, word2) else "is not" 

    return "{} {} a rotation of {}".format(word1, is_or_not, word2)


if __name__ == '__main__':
    print(answer("waterbottle", "erbottlewat"))
    print(answer("awterbottle", "erbottlewat"))
    print(answer("", ""))
    print(answer("a", "a"))
    print(answer("a", "b"))
