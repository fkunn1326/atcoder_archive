r, g, b = input().split()
c = int(r+g+b)
if c%4 == 0:
    print("YES")
else:
    print("NO")