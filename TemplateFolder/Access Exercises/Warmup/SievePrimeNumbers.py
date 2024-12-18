import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.
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

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(0))