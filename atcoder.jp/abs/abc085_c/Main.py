n, y = map(int, input().split())

r1000, r5000, r10000 = -1, -1, -1

for i in range(n+1):
    for j in range(n-i+1):
        k = n-i-j
        if 10000*i+5000*j+1000*k == y:
            r10000 = i
            r5000 = j
            r1000 = n-i-j

print(r10000, r5000, r1000)