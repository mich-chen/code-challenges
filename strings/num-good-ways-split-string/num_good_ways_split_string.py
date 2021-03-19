from collections import Counter

def numSplits(s: str) -> str:

    # base case
    if len(s) == 1:
        return 0

    # use hashmap to keep track of splits
    left = Counter()
    right = Counter(s)

    result = 0

    for char in s:
        # create splits
        left[char] += 1
        right[char] -= 1
        # remove character when no longer in right split
        if right[char] == 0:
            del right[char]

        # compare number of distinct characters and increment result
        result += len(left) == len(right) # if true, will increment number

    return result

if __name__ == '__main__':

    print(numSplits("aacaba")) # 2
    print(numSplits("aaaaa")) # 4
    print(numSplits("acbadbaada")) # 2
