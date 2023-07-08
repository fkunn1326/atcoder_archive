a,b=map(int, input().split())
s = b-a

if (s==1 or s==3) and not a%3==0 and s==1:
    print("Yes")
else:
    print("No")