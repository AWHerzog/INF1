
def is_idempotent(f, it):
    
    
    if isinstance(it, str):
        x = f(it)
        return x == it.lower()
    if isinstance(it, (float, int)):
        return (f(f(it))) == f(it)

    


print(is_idempotent(str.lower, "Hello"))
print(is_idempotent(type, "Hello"))
print(is_idempotent(abs, -5))
print(is_idempotent(lambda x: x + 1, 5))
print(is_idempotent(lambda x: True, 10))