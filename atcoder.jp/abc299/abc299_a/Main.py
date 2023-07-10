import re
N, S = input(), input()
print('in' if re.search('\|.*\*.*\|', S) else 'out')