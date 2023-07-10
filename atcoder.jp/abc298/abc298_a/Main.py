n,s=int(input()), input()

def check(n):
    if "x" in s:
        return False
    elif not "o" in s:
        return False
    else:
        return True


if check(n):
    print('Yes')
else:
    print('No')
