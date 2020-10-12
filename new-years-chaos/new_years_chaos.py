def minimumBribes(q):
    """
    queue for roller coaster, starting from 1 --> len(q)
    each element can only max swap 2 times. 
    one element can bribe element in front of it to swap.
    find the min num of bribes that took place for current q
    Return min bribes, or 'Too Chaotic' if line config is not possible (based on these conditions)
    test cases:
        >>> q = 2, 1, 5, 3, 4
        min bribes = 3

        >>> q = 2, 5, 1, 3, 4
        'Too Chaotic' --> 5 cannot be in current position because swapped > 2 times
    """