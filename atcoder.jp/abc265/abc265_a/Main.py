X,Y,N=map(int,input().split())

if X*3>Y:
    _Y = N//3
    print(X*(N-3*_Y)+Y*_Y)
else:
    print(X*N)