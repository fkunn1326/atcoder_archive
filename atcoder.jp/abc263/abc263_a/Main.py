a=list(map(int, input().split()))

def check(a):
    if a.count(a[0]) == 3 or a.count(a[0]) == 2:
        if len(set([i for i in a if i != a[0]])) == 1:
            return True
    return False

if check(a):
    print('Yes')
else:
    print('No')