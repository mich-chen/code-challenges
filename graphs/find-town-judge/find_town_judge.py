from typing import List

def findJudge(N: int, trust: List[List[int]]) -> int:
    """Indegree - outdegree connected graph solution."""
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

def findJudge_sets(N: int, trust: List[List[int]]) -> int:
    """Use dictionary and set intersection solution."""
    # base case: if only townjudge and no trusts
    if not trust and N == 1:
        return N

    # keys = person, value = set of people they trust
    d = {i: {i} for i in range(1, N + 1)}

    # if townjudge exists, will not be part of iteration
    for person, trusts in trust:
        d[person].add(trusts)
        # remove self from trusted ppl
        # townjudge trusts "themselves" & will exist in set intersection check later
        if person in d[person]:
            d[person].remove(person)
    
    # initialize town judge with first person's trusted ppl
    town_judge = d[1]
    # intersect sets, only return the common person across all sets
    for trusted in d.values():
        town_judge = town_judge&trusted

    return town_judge.pop() if len(list(town_judge)) == 1 else -1


if __name__ == '__main__':
    
    print(findJudge(3, [[1,3],[2,3],[3,1]]))  # -1
    print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3
    print(findJudge_sets(3, [[1,3],[2,3],[3,1]])) # -1
    print(findJudge_sets(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3
    