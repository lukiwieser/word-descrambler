from itertools import permutations
from english_words import english_words_lower_set

text = "luogntt"
print("input: " + text)


perms = [''.join(p) for p in permutations(text)]
perms_set = set(perms)

for perm in perms_set:
    if perm.lower() in english_words_lower_set:
        print(perm)
