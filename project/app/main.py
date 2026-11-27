def pack_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return {'result': res, 'status': 'success'}
    return wrapper

@pack_result
def add(a, b):
    return a + b

@pack_result
def multiply(a, b, c):
    return a * b * c

@pack_result
def greet(name):
    return f"Привіт, {name}!"

print(add(2, 3))
print(multiply(2, 3, 4))
print(greet("Оля"))