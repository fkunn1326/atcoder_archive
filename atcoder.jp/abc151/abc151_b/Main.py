n, k, m = map(int, input().split())
a = map(int, input().split())

s = n*m - sum(a)
if s > k:
    s = -1
elif s < 0:
    s = 0

print(s)