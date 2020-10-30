from collections import Counter

def reorganizeString(s: str) -> str:

    if len(s) == 1:
        return s

    i = 0
    bucket = [''] * len(s) # new output string
    # dictionary of letters with count, in descending order
    count = Counter(s)
    # list of letters, descending order by count
    # reverse=True because sorted() returns in ascedning order
    letters = sorted(count, key=count.get, reverse=True)

    for letter in letters:
        # if largest count is greater than half (if len(s) is even) or half + 1(if len(s) is odd)
        if count[letter] > (len(s) // 2 + (len(s) % 2)):
            return ''

        # place highest occuring letters in alternating place
        # iterate through letter's count
        for j in range(count[letter]):
            # reset index to 1 for alternating odd indices
            if i >= len(s):
                i = 1
            # place character at index of bucket
            bucket[i] = letter
            # alternating index
            i += 2

    return ''.join(bucket)


if __name__ == '__main__':
    
    print(reorganizeString("baaba")) # "ababa"
    print(reorganizeString("aaaab"))  # ''

