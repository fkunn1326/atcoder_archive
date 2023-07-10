N,K=map(int, input().split())
A=list(map(int, input().split()))

for i in range(K):
    l = A[1:]
    l.append(0)
    A=l

print(" ".join(map(str, A)))