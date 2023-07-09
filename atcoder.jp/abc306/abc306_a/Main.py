n=int(input())
s=list(input())

print("".join(sum([[i, i] for i in s], [])))