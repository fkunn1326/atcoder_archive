import math

N, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def calc_dis(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

ANS = [False] * N
ANS[0] = True

# for i in range(N):
#     if ANS[i]:
#         x1, y1 = A[i]
#         for j in range(N):
#             if not ANS[j]:
#                 x2, y2 = A[j]
#                 distance = calc_dis(x1, y1, x2, y2)
#                 if distance <= D:
#                     print(f"{j+1} was infacted from {i+1}")
#                     ANS[j] = True

# 感染させまくるぞー！
new_infected = [0]
while new_infected:
    current_infected = new_infected.copy()
    new_infected = []
    for i in current_infected:
        x1, y1 = A[i]
        for j in range(N):
            if not ANS[j]:
                x2, y2 = A[j]
                distance = calc_dis(x1, y1, x2, y2)
                if distance <= D:
                    ANS[j] = True
                    new_infected.append(j)

result = ["Yes" if ANS[i] else "No" for i in range(N)]
for i in result:
    print(i)