H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

def match(A, B):
  for i in range(H):
    for j in range(W):
      if A[i][j] != B[i][j]:
        return False
  return True

def shift_vertical(A):
  last_row = A[-1]
  A.pop()
  A.insert(0, last_row)
  return A

def shift_horizontal(A):
  for i in range(H):
    last_char = A[i][-1]
    A[i] = last_char + A[i][:-1]
  return A

found = False
for s in range(H):
  for t in range(W):
    A = shift_horizontal(A)
    if match(A, B):
      found = True
      break
  if found:
    break
  A = shift_vertical(A)

if found:
  print("Yes")
else:
  print("No")