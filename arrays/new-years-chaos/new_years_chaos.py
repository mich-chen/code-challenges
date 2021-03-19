def minimumBribes(q):
    
    bribes = 0

    for i, num in enumerate(q):
        # if num minus its position is greater than 2, then bribed too much
        if num - (i + 1) > 2:
            print('Too chaotic')
            return
        # check how many nums are greater in range from one position in front of current num's supposed position to one in front of where it is
        # so look at how many bribes happened for current number to be where it is
        # use max() in case any negative indexing
        else:
            for j in range(max(num - 2, 0), i):
                if q[j] > num:
                    bribes += 1

    print(bribes)


if __name__ == '__main__':
    

    (minimumBribes([2, 1, 5, 3, 4]))  # 3
    (minimumBribes([2, 5, 1, 3, 4])) # Too chaotic
    (minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))  # Too chaotic
    (minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])) # 7
