N = int(input())
A = [input().split(" ") for _ in range(N)]

ages = [int(x[1]) for x in A]
minage = min(ages)

for i in range(ages.index(minage), len(ages)):
    print(A[i][0])

for i in range(0, ages.index(minage)):
    print(A[i][0])