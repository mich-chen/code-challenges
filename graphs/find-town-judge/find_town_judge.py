from typing import List

def findJudge(N: int, trust: List[List[int]]) -> int:

    # initialize an array to keep track of trust count for each person
    # N + 1 because indexing, and each person starts at 1
    trusts = [0] * (N + 1)

    # unpack each pair in trusts
    for (a, b) in trust:
        # use indexing to increment or decrement trust count
        # person a decrement
        # person b increment trust
        trusts[a] -= 1
        trusts[b] += 1

    for i in range(1, len(trusts)):
        # return the person/index which is 1 less than N 
        # everybody except judge trusts town judge
        if trusts[i] == N - 1:
            return i

    return -1


if __name__ == '__main__':
    
    print(findJudge(3, [[1,3],[2,3],[3,1]]))  # -1
    print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3