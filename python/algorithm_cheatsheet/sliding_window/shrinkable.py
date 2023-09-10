from collections import defaultdict


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstringWithoutRepeating(s: str) -> int:
    map = defaultdict(int) # track count of each character
    j = ans = 0
    for i in range(len(s)):
        map[s[i]] += 1 # update state using s[i]
        while map[s[i]] > 1:
            map[s[j]] -= 1 
            j += 1 # shrink the left edge using s[j]
        ans = max(ans, i - j + 1) # longest window so far
    return ans # longest window

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    map = defaultdict(int) # track count of each character
    j = cnt = ans = 0
    for i in range(len(s)):
        c = s[i]
        map[c] += 1
        if map[c] == 1: cnt += 1 # update state using s[i]
        while cnt > k:
            c = s[j]
            map[c] -= 1
            if map[c] == 0: cnt -= 1 # update state using s[j]
            j += 1 # shrink the left edge while invalid
        ans = max(ans, i - j + 1) # longest window so far
    return ans # longest window


input1 = ["abcabcbb", "bbbbb", "pwwkew"]
for input in input1:
    print("lengthOfLongestSubstringWithoutRepeating(\"{}\") = {}".format(
        input,
        lengthOfLongestSubstringWithoutRepeating(input)))
print()

input2 = ["eceba", "aa"]
for input in input2:
    for k in range(1, len(input) + 1):
        print("lengthOfLongestSubstringKDistinct(\"{}\", {}) = {}".format(
            input,
            k,
            lengthOfLongestSubstringKDistinct(input, k)))
