def alternatingCharacters(s):

    min_dels = 0
    # track the index of sinlge character, no duplicates after
    marker = 0

    for i in range(1, len(s)):
        # if current character is not a duplicate
        # update new pointer to be this index
        # next iterations will compare to this character
        if s[i] != s[marker]:
            marker = i
        # if character is a duplicate, increment num of deletes
        else:
            min_dels += 1

    return min_dels


if __name__ == '__main__':
    
    print(alternatingCharacters('ABABABAB'))  # 0
    print(alternatingCharacters('AAABBB'))  # 4
    print(alternatingCharacters('ABCCBCAAB'))  # 2
