def addition(a, b):
    return a + b

def multiplication(a, b):
    return a

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def modulus(a, b):
    return a % b
