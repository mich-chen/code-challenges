from typing import List

def sortedSquares(A: List[int]) -> List[int]:

    # O(n log n) solution
    output = []
    for num in A:
        output.append(num*num)

    return sorted(output)


if __name__ == '__main__':
    
    print(sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
    print(sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]
    print(sortedSquares([-1,1])) # [1,1]
