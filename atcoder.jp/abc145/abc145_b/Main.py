n = int(input())
s = input()
h = int(n/2)

print("Yes" if s[:h] == s[h:] else "No")