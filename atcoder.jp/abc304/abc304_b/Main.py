N = int(input())

def approximate_value(N):
    if N <= 10**3 - 1:
        return N
    elif N <= 10**4 - 1:
        return N // 10 * 10
    elif N <= 10**5 - 1:
        return N // 100 * 100
    elif N <= 10**6 - 1:
        return N // 1000 * 1000
    elif N <= 10**7 - 1:
        return N // 10000 * 10000
    elif N <= 10**8 - 1:
        return N // 100000 * 100000
    else:
        return N // 1000000 * 1000000
    
print(approximate_value(N))