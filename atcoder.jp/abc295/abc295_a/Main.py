N = int(input())
S = input().split()

def check(N):
    for i in ["and", "not", "that", "the", "you"]:
        if i in S:
            return True
    return False

if check(N):
    print('Yes')
else:
    print('No')