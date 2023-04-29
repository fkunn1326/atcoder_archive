N, A, B = map(int, input().split())
C = list(map(int, input().split()))

for i in range(N):
    if A + B == C[i]:
        # 番号を出力する
        print(i + 1)
        # ループを抜ける
        break