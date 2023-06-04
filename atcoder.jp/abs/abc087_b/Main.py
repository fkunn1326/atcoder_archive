A, B, C, X = map(int, open(0))

print(sum(i*500 + j*100 + k*50 == X for k in range(C+1) for j in range(B+1) for i in range(A+1)))