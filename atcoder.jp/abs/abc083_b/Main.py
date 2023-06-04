n, a, b = map(int, input().split())
print(sum([i for i in range(n+1) if b >= sum(map(int, list(str(i)))) >= a]))