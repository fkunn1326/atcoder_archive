n=int(input())
l=1
while True:
    if n >= l*2:
        l *= 2
    else:
        break
print(l)