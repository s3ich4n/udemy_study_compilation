from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in strs:
    # print(''.join(sorted(word)))
    anagrams[''.join(sorted(word))].append(word)

print(anagrams)
