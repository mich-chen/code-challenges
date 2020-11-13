from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    if len(strs) == 1 and strs[0] == '':
        return [['']]

    output = []
    d = {}

    for i in range(len(strs)):
        count = [0] * 26
        # iterate current word and get count
        for j in strs[i]:
            count[ord(j) - ord('a')] += 1
        # change count into tuple
        count = tuple(count)
        # if anagram exists in dict, append to list
        if count in d:
            d[count].append(strs[i])
        else:
            d[count] = [strs[i]]

    return list(d.values())


if __name__ == '__main__':
    
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(groupAnagrams(["a"]))  # [["a"]]
    print(groupAnagrams([""])) # [[""]]
