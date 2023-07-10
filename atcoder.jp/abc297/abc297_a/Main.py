N,D=map(int,input().split())
T=list(map(int, input().split()))
ans=-1

def pairwise(lst):
    return [(lst[i], lst[i+1]) for i in range(0, len(lst)-1)]

for i,j in pairwise(T):
    if j-i<=D:
        ans = j
        break

print(ans)
