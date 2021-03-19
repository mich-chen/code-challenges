def sort_array(arr):

    indexes = []
    odds = []
    # pointer for odds and indexes arrays
    pointer = 0

    # first pass populate odds and indexes arrays
    for i, num in enumerate(arr):
        # if num is odd
        if num % 2 != 0:
            indexes.append(i)
            odds.append(num)

    # sort odds array to match the sorted indexes (sorted as they are added)
    odds.sort()
    # iterate over odds array, replace odds in orig array with the correct sorting
    for _ in odds:
        arr[indexes[pointer]] = odds[pointer]
        pointer += 1

    return arr


if __name__ == '__main__':
    
    print(sort_array([5, 3, 2, 8, 1, 4])) # [1, 3, 2, 8, 5, 4]
    print(sort_array([5, 7, 9, 3, 1]))  # [1, 3, 5, 7, 9]
