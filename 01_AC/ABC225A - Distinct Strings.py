import itertools
s = input()
all_lst = list(itertools.permutations(s))
print(len(list(set(all_lst))))
