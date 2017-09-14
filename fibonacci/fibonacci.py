# Return the nth term in the fibonacci sequence
# 1, 1, 2, 3, 5, 8...

def fib_slow(n):
    if n in (1,2):
        return 1
    else:
        return fib_slow(n-1) + fib_slow(n-2)

def fib_fast(n):
    fib = [1,1]
    if n in (1,2):
        return 1
    else:
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]