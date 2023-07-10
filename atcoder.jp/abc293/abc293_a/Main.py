S = list(input())

for i in range(int(len(S)/2)):
    S[2*i], S[2*i+1] = S[2*i+1], S[2*i]

print("".join(S))