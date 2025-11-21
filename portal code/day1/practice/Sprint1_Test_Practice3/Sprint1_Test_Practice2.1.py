import itertools

n=int(input())
r=int(input())

replc = len(list(itertools.combinations(range(n),r)))


print(f"Total combinations (C({n},{r})) without replacement: {replc}")
