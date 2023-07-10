import string
n,x=map(int,input().split())

print("".join([i*n for i in list(string.ascii_uppercase)])[x-1])