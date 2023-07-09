h,w=map(int,input().split())
a=sum([list(map(int, input().split())) for _ in range(h)], [])
min = min(a)
print(sum([i-min for i in a]))