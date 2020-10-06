def twoStrings(s1, s2):
    """Return boolean if both strings share a common substring."""

    set1 = set(s1)
    set2 = set(s2)

    for char in set1:
        if char in set2:
            return True

    return False


if __name__ == '__main__':
    
    print(twoStrings('hello', 'world'))  # True
    print(twoStrings('hi', 'world'))  # False