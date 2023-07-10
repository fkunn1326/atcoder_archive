H,W=map(int, input().split())
S = [input() for _ in range(H)]

print("".join(S).count("#"))