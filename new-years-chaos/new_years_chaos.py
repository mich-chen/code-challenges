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

    bribes = 0
    # track the sorted index of each element
    qsorted = {x: i for i,x in enumerate(sorted(q))}
    print(qsorted)

    # iterate through queue, if any number has swapped > 2 times then return too chaotic
    for i, element in enumerate(q):

        if qsorted[element] - i > 2:
            return 'Too chaotic'

        elif i != 0 and q[i-1] < element:
            # bribes += (qsorted[q[i-1]] - (i-1))
            # continue
        else:
            bribes += (qsorted[element] - i)

    return bribes


if __name__ == '__main__':
    

    print(minimumBribes([2, 1, 5, 3, 4]))  # 3
    print(minimumBribes([2, 5, 1, 3, 4])) # Too chaotic
    print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))  # Too chaotic
    print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])) # 7
