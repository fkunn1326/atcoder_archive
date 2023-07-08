n=int(input())
t,a = map(int, input().split())
h=list(map(int, input().split()))

def getA(h):
    return abs((t-h*0.006)-a)

l=[getA(i) for i in h]
print(l.index(min(l))+1)