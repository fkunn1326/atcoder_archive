N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

print(sum([A[i-1] for i in B]))