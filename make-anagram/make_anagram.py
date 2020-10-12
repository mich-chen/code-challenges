from collections import Counter

def makeAnagram(a, b):
    """Return min. number of character deletions to make both strings anagrams of each other."""

    # if allowed to use Counter()
    count_a = Counter(a)
    count_b = Counter(b)
    # Counter math to find difference in frequency for each letter
    count_a.subtract(b)  

    # counter object math to find which letters to delete, and num of differences in frequency.
    # sum up all the differences in frequency == num of deletions needed
    min_dels = sum(abs(i) for i in count_a.values())

    return min_dels

    """
    ***** Alternative solution: if not allowed to use Counter() *****

    # construct own dictionaries of each letter and its frequency
    dictA = {char: a.count(char)for char in a}
    dictB = {char: b.count(char) for char in b}

    sums = 0
    # iterate through one dictionary and find any different characters, if not present then add its frequency to sum
    for char in dictA:
        if char not in dictB:
            sums += dictA[char]
        # perform math on corresponding letter's frequencies and add to sum
        else:
           num = abs(dictA[char] - dictB[char])
           sums += num

    # iterate through second dictionary, any characters not present in first dictionary then add its frequency to sum
    for char in dictB:
        if char not in dictA:
            sums += dictB[char]

    return sums
    """


if __name__ == '__main__':
    
    print(makeAnagram('showman', 'woman'))  # 2
    print(makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))  # 30
    