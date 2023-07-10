y = int(input())
ans = (y//4)*4+2
if ans < y:
    ans += 4
print(ans)