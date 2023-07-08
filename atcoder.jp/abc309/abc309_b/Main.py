n=int(input())
a=[list(map(int, list(input()))) for _ in range(n)]

rotated = [[0] * n for _ in range(n)]
rotated[0] = [a[1][0]]
rotated[0].extend(a[0][:n-1])
for i in range(1, n-1):
    k = [a[i+1][0]]
    k.extend(a[i][1:n-1])
    k.append(a[i-1][n-1])
    rotated[i] = k
rotated[n-1] = a[n-1][1:]
rotated[n-1].append(a[n-2][n-1])

print("\n".join(["".join(map(str, r)) for r in rotated]))