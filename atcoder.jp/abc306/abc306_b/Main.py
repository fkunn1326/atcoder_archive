a = list(map(int, input().split()))
ans = 0
for i in range(64):
    ans += a[i] << i
print(ans)