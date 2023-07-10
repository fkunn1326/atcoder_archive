N = int(input())

def solve(N):
    if N == 0:
        return 1
    else:
        return N * solve(N-1)

print(solve(N))