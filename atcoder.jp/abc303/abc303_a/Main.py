n = int(input())
s = input().rstrip()
t = input().rstrip()

for i in range(n):
    if s[i] == t[i]:
        continue
    if (s[i] == '0' and t[i] == 'o') or (s[i] == 'o' and t[i] == '0'):
        continue
    if (s[i] == '1' and t[i] == 'l') or (s[i] == 'l' and t[i] == '1'):
        continue
    print('No')
    exit()
print('Yes')