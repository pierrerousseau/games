""" Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures

    from : Craking the Coding Interview, 4th edition, Gayle Laakmann
"""


def has_unique(word):
    """ :returns: True if the <word> has all unique characters,
            False otherwise
            without additional structure

        :param str word: a string
        O(n2)
    """
    all_unique = True
    for index, letter in enumerate(word):
        for next_letter in word[index + 1:]:
            if letter == next_letter:
                all_unique = False
                break
        if not all_unique:
            break

    return all_unique


def has_unique_bis(word):
    """ :returns: True if the <word> has all unique characters,
            False otherwise
            without additional structure, more clever

        :param str word: a string
        O(nlogn)
    """
    all_unique = True
    letters    = sorted(word)  # let's pretend it's O(nlogn)
    for index, letter in enumerate(letters):
        if letter == letters[index + 1]:
            all_unique = False
            break

    return all_unique


def has_unique_ter(word):
    """ :returns: True if the <word> has all unique characters,
            False otherwise
            with additional structure

        :param str word: a string
        O(n)
    """
    all_unique = True
    letters    = {}
    for letter in word:
        if letters.get(letter) is None:
            letters[letter] = 1
        else:
            all_unique = False
            break

    return all_unique


def answers(word):
    """ :returns: a readable answer, for all versions

        :param str word: the word to test against different versions
    """
    version_1 = has_unique(word)
    version_2 = has_unique(word)
    version_3 = has_unique(word)
    return "{} has only unique characters : {}, {}, {}".format(word,
                                                               version_1,
                                                               version_2,
                                                               version_3)


if __name__ == "__main__":
    print(answers("abcdefg"))
    print(answers("abcdefa"))
    print(answers("aaaaaaa"))
    print(answers("abbbbbb"))
    print(answers("abccefg"))
    print(answers("abcdebg"))
    print(answers("aacdefg"))
    print(answers("a"))
    print(answers(""))
