N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for i in AB:
    print(i[0]+i[1])