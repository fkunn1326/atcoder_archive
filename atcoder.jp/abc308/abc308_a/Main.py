n = list(map(int, input().split()))

if n == sorted(n) and sum([s%25 for s in n]) == 0 and sum([100<=s<=675 for s in n]) == len(n):
    print("Yes")
else:
    print("No")