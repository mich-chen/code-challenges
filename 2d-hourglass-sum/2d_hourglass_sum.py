def hourglassSum(arr):
    """ 
    given 2d array is always 6 x 6; rows = 6, columns = 6
    arr = [
    ->j= 0, 1, 2, 3, 4, 5
        [x, x, x, 1, 1, 1], --> i = 0
        [0, x, 0, 0, 1, 0], --> i = 1
        [x, x, x, 1, 1, 1], --> i = 2
        [a, a, a, 0, 0, 0], --> i = 3
        [0, a, 0, 0, 0, 0], --> i = 4
        [a, a, a, 0, 0, 0]  --> i = 5
    ]
    hourglass is represented as Xs here ^^^^, there are 16 hourglasses total
    calculate each hourglass, return the max hourglass value
    """

    # keep track of max hourglass, and compare and update with each iteration through hourglasses; max(max_hg, current_hg)
    max_hg = 0
    
    # don't need to look at last two because top of hourglass is 3 squares
    for i in range(6 - 2):
        for j in range(6 - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            current_hg = top + middle + bottom
            max_hg = max(max_hg, current_hg)

    return max_hg