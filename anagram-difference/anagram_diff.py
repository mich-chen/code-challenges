from collections import Counter

def helper_count_diff(str1, str2):
    # to be valid anagram, must be same length
    if len(str1) != len(str2):
        return -1

    count = 0 
    ct_str1 = Counter(str1) 

    # iterate through second string
    # if char in string 1 dictionary then decrement
    for char in str2:
        if char in ct_str1 and ct_str1[char] > 0:
            ct_str1[char] -= 1
        # if char exceeds freq in string 1, increase count
        # if char not in string 1 dict then increase count
        else:
            count += 1
    return count


def helper2(str1, str2):
    # to be valid anagram, must be same length
    if len(str1) != len(str2):
        return -1

    # use bucket to track counts of each alphabetical char
    ch_counts = [0] * 26 # bucket
    for char in str1:
        # increment count for each char in string 1
        ch_counts[ord(char) - ord('a')] += 1

    for char in str2:
        # decrement count for each char in string 2
        ch_counts[ord(char) - ord('a')] -= 1

    count = 0
    for c in ch_counts:
        if c > 0:
            count += c
    return count

def anagram_diff(a, b):
    
    output = []
    for i in range(len(a)):
        output.append(helper2(a[i], b[i]))
    return output




if __name__ == '__main__':
    
    a = ['a', 'jk', 'abb', 'mn', 'abc']
    b = ['bb', 'kj', 'bbc', 'op', 'def']
    print(anagram_diff(a, b))  # [-1, 0, 1, 2, 3]
