# fibonacci sequence

def fibonacci(n):
    fis = [1, 2]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:

        for i in range(2, n):
            fn = fis[i-1] + fis[i-2]
            fis.append(fn)
        return fis


print(fibonacci(10))
