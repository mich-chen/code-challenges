from typing import List

def sortedSquares(A: List[int]) -> List[int]:

    # # O(n log n) solution
    # output = []
    # for num in A:
    #     output.append(num*num)

    # return sorted(output)

    # O(n) solution

    output = []
    
    #if all neg or positive, just square everything and return
    if A[0] >= 0:
        for num in A:
            output.append(num**2)
        return output
    
    if A[-1] < 0:
        for num in A[::-1]:
            output.append(num**2)
        return output

    # 1st pass to set pointers to first positive num and largest neg num
    left = right = 0
    for i in range(len(A)):
        if A[i] >= 0:
            right = i
            left = i - 1
            break
            
    while left >= 0 and right < len(A):
        # append the square of whichever abs value of num is smaller
        if abs(A[left]) < abs(A[right]):
            output.append(A[left] ** 2)
            left -= 1
        else: # A[right] <= A[left]
            output.append(A[right] ** 2)
            right += 1
    # append remaining of beginning
    while left >= 0:
            output.append(A[left] ** 2)
            left -= 1
    # append remaining of end
    while right < len(A):
            output.append(A[right] ** 2)
            right += 1
        
    return output



if __name__ == '__main__':
    
    print(sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
    print(sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]
    print(sortedSquares([-1,1])) # [1,1]
