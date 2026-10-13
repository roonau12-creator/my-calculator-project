def add(a, b):
    """Cộng hai số"""
    return a + b

def subtract(a, b):
    """Trừ hai số"""
    return a - b

def multiply(a, b):
    """Nhân hai số"""
    return a * b

def divide(a, b):
    """Chia hai số"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b