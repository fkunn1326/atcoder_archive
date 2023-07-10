S = list(input())
ans = -1
for i in set(S):
    if S.count(i) == 1:
        ans = i
        break

print(ans)