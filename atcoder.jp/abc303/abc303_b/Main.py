import math

def pairwise(lst):
    return [(lst[i], lst[i+1]) for i in range(0, len(lst)-1)]

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

ansaa = []

for aa in a:
    for aaa, aab in pairwise(aa):
        ansaa.append(sorted([aaa, aab]))

print(math.comb(n, 2) - len(get_unique_list(ansaa)))