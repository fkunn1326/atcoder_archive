N = int(input())
S = map(int, input().split())

print(" ".join([str(i) for i in S if i%2==0]))