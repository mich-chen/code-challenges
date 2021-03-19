def lengthOfLongestSubstring(s: str) -> int:
    
    # if empty string
    if not s:
        return 0
    # if string only contains one letter type
    if len(set(s)) == 1:
        return 1
    
    if len(set(s)) == len(s): # then everything in string is unique
        return len(s)
    
    # generate substrings / subsets 
    start = end = 0 # pointers
    longest = 1
    # use dictionary to keep track of non repeating substring 
    seen = {} 
    while end < len(s):
        # if character is not already in dictionary (not a repeat)
        if s[end] not in seen:
            # add character to dictionary
            seen[s[end]] = end
            # move pointer
            end += 1 
            # update the longest substring value
            longest = max(longest, len(seen)) 
        # if character is already in dictionary
        else: 
            # move start pointer by one, to restart new substring
            start += 1
            # reset end pointer and dictionary
            end = start
            seen = {}
            longest = max(longest, len(seen))
        
    return longest


if __name__ == '__main__':
    
    print(lengthOfLongestSubstring('abcabcbb'))  # 3
    print(lengthOfLongestSubstring('pwwkew'))  # 3
    print(lengthOfLongestSubstring(''))  # 0
    print(lengthOfLongestSubstring('aaaaaa'))  # 1
    print(lengthOfLongestSubstring('dvdf'))  # 3