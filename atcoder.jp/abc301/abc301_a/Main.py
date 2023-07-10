N = int(input())
S = input()

def check(N):
    if S.count("T") == S.count("A"):
        if S.rfind("T") > S.rfind("A"):
            return "A"
        else:
            return "T"
    elif S.count("T") > S.count("A"):
        return "T"
    else:
        return "A"

print(check(N))