from collections import Counter

# Complete the isValid function below.
def isValid(s):

    # base case
    if len(s) <= 2:
        print('YES')
        return 'YES'

    # if Counter() is allowed
    s_count = Counter(s)

    # keys are letter freq, values are number of occurences of that freq
    dict_cts = Counter(s_count.values())

    # all letters are same frequency, therefore len = 1
    if len(dict_cts) == 1:
        return 'YES'

    # if there is 2 different frequencies
    elif len(dict_cts) == 2:
        key1, key2 = dict_cts.keys()
        # if removing the letter with 1 occurence also becomes same freq as other
        # key subtraction to account for if removing 1 instance, does it equal the other key,
        # or if removing 1 instance, does it completely remove it so 0
        if dict_cts[key1] == 1 and ((key1 - 1) == key2 or (key1 - 1) == 0):
            return 'YES'
        if dict_cts[key2] == 1 and ((key2 - 1) == key1 or (key2 - 1) == 0):
            return 'YES'
        else:
            return 'NO'

    else:
        return 'NO'

"""
    ******* misinterpreted prompt, this solution works if can remove multiple instances *****

    s_count = Counter(s)
    # sort frequencies of each character
    sorted_counts = sorted(s_count.values())
    # dict for frequencies as keys and number of occurences as values
    ct_dict = Counter(sorted_counts) # frequency of each frequency...
    # if any values are 1, then can remove 1 instance and will be valid
    # if 1 in ct_dict.values():
    #     return 'YES'
    # set to check if all characters have same frequency
    val_set = set()
    print(s_count)
    print('sorted counts', sorted_counts)
    
    for val in sorted_counts:
        # remove one instance, add that value to set
        val_set.add(val - 1)
    # if there are any instances of 0, or length of set is 2 or less
    # after removing 1 instance, either letters have 0 or all same frequency
    print('set', val_set)
    if 0 in val_set and len(val_set) <= 2:
        return 'YES'
    else:
        return 'NO'
"""

    # 'abcdefghhgfedecba'
    # 'xxxaabbccrry'
        # ct_dict.values() = [1, 2, 2, 2, 2, 3]
        # val_set = {0, 1, 2}
    # 'aaaabbcc'
        # ct_dict.values() = [2, 2, 4]
        # val_set = {1, 3}

if __name__ == '__main__':
    
    print(isValid('xxxaabbccrry'))  # NO
    print(isValid('abcdefghhgfedecba'))  # YES
    print(isValid('aaaabbcc'))  # NO
    print(isValid('aabbcd'))  # NO