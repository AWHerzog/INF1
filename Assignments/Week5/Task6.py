import math

def sieve_of_eratosthenes(n):

    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
   

    for p in range(2, n+1):
        if is_prime[p]:
            multiple = p*p
            while multiple <= n:
                is_prime[multiple] = False
                multiple += p

    primes_up_to_n = [number for number, prime in enumerate(is_prime) if prime]

    return primes_up_to_n



print(sieve_of_eratosthenes(0))