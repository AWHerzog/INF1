
def fib(n, memo=None):
    
    if memo is None: 
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

    if n in memo:
        return memo[n]
    
    memo[n] = fib(n-2, memo) + fib(n-1, memo) + fib(n-3, memo)

    return memo[n]

print(fib(100))
