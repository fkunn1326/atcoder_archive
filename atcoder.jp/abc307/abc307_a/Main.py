n=int(input())
a=list(map(int,input().split()))
ans=[sum(a[i*7:(i+1)*7]) for i in range(n)]

print(" ".join(map(str, ans)))