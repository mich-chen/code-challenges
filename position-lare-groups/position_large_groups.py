from typing import List

def largeGroupPositions(s: str) -> List[List[int]]:

    output = []
    start = 0 # start pointer

    # as iterate, iteration we are is end pointer
    for end in range(len(s)):
        # check if last char or if not same char
        if end == len(s) - 1 or s[end] != s[end + 1]:
            # check if is a large interval
            if end - start + 1 >= 3:
                output.append([start, end])
            # move start pointer
            start = end + 1

    return output


if __name__ == '__main__':
    
    print(largeGroupPositions("abcdddeeeeaabbbcd"))  # [[3,5],[6,9],[12,14]]
    print(largeGroupPositions("aaa"))  # [[0, 2]]
    print(largeGroupPositions("abc"))  # []

