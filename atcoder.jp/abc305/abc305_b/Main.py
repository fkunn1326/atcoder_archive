p, q = input().split()

abc = "ABCDEFG"
ax = [3,1,4,1,5,9]
sss = [abc.index(p), abc.index(q)]

print(sum([ax[i] for i in range(min(sss), max(sss))]))