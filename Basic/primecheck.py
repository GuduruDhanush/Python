def prime_check(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print('it is a prime')
    else:
        print('it is not a prime')


print(prime_check(21))
