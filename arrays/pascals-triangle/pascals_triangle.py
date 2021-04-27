from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        output = [[1]] # always already have initialized the first row
        for i in range(numRows - 1): # so when iterating, do numRows - 1
            output.append(self.calculate(output[-1]))
        return output
        
    def calculate(self, prev_row):
        """Return new row"""
        # initiate new row with 1
        new_row = [1]
        # iterate through previous row, add adjacent numbers
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i+1])
        return new_row + [1]

if __name__ == '__main__':
    example = Solution()
    print(example.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(example.generate(1)) # [[1]]
    print(example.generate(0)) # [[]]