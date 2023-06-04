N = int(input())
A = list(map(int, input().split()))

count = 0

while True:
    sA = [a % 2 for a in A]
    if 1 in sA:
        break
    else:
        A = [a / 2 for a in A]
        count += 1

print(count)