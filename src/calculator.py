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


def power(base, exp):
    """Lũy thừa: base ^ exp"""
    return base ** exp


def modulo(a, b):
    """Phép chia lấy dư"""
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero")
    return a % b
