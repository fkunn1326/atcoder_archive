A,B=map(int, input().split())

preans = [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], []]
ans = [1, 2, 4]

for i in preans[A-1]:
    ans[i-1] = 0

for i in preans[B-1]:
    ans[i-1] = 0

print(7-sum(ans))