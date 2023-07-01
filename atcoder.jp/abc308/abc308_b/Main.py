n, m = map(int, input().split())
c = input().split()
d = input().split()
p = list(map(int, input().split()))

count = 0
obj = {}

for idx, i in enumerate(d):
    obj[i] = p[idx+1]

for s in c:
    if not s in d:
        count += p[0]
    else:
        count += obj[s]

print(count)