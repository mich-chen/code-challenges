def countSwaps(a):

    swaps = 0
    for i in range(len(a) - 1):
        # the last element from current posision will be sorted
        for j in range(len(a) - 1 - i):
            # check if current element is larger than next, if so, then swap
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    
    countSwaps([3, 2, 1])
    countSwaps([1, 2, 3])