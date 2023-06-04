s = "".join(reversed(input()))
divider = ["dream", "dreamer", "erase", "eraser"]
divider = ["".join(reversed(d)) for d in divider]

while not s == "":
    can = False
    for d in divider:
        if s.startswith(d):
            s = s[len(d):]
            can = True
    if not can:
        print("NO")
        break
    if s == "":
        print("YES")
