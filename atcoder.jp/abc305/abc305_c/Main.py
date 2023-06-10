h, w = map(int, input().split())
s = [input() for i in range(h)]

arr = []
narr = []

for i in s:
    sa = [n for n, v in enumerate(i) if v == "#"]
    arr.append(sa)
    if len(sa) > 0:
        narr.append(sa)

idxar = [len(s) for s in arr]
idxarz = [len(s) for s in arr if len(s) > 0]

a = [x for row in narr for x in row]
print(idxar.index(min(idxarz)) + 1, [i for i in list(set(a)) if a.count(i) == len(idxarz)-1][0] + 1)