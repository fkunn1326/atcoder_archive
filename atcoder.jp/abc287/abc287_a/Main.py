N = int(input())
AB = [input() for _ in range(N)]

if AB.count("For") < AB.count("Against"):
    print("No")
else:
    print("Yes")