from typing import List

def dailyTemperatures(T: List[int]) -> List[int]:
       
       if len(T) == 1:
           return 0
       # stack to track indices
       stack = [] 
       output = [0] * len(T) 
       
       # iterate through temperatures list 
       for i, temp in enumerate(T): 
           # while there is a temp in the stack (cooler temps)
           # and if current temp is hotter than temp in stack
           while stack and temp > T[stack[-1]]: 
               cool_idx = stack.pop() 
               output[cool_idx] = i - cool_idx 
           # add to stack
           stack.append(i)
       
       return output


if __name__ == '__main__':
  
  print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]