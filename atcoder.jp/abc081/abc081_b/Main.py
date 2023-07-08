n=int(input())
s=list(map(int, input().split()))
c=0
while True:
    if sum([i%2!=0 for i in s]) == 0:
        c+=1
        s = [i/2 for i in s]
    else:
        break

print(c)