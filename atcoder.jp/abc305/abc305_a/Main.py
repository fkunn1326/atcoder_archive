import math

n = int(input())

p = math.floor(n/5) * 5
s = math.ceil(n/5) * 5

if n-p < 2.5:
    print(p)
else:
    print(s)
