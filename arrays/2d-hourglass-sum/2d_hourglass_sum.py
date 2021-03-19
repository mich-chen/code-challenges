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
    # set first hourglass as max_hg
    max_hg = arr[0][0] + arr[0][1] + arr[0][2]\
           + arr[1][1]\
           + arr[2][0] + arr[2][1] + arr[2][2]
    
    # don't need to look at last two because top of hourglass is 3 squares
    for i in range(6 - 2):
        for j in range(6 - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            current_hg = top + middle + bottom
            max_hg = max(max_hg, current_hg)

    return max_hg


if __name__ == '__main__':
    
    print(hourglassSum([
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
        ]))  # -6
