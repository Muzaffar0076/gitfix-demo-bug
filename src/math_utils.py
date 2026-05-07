def divide(a, b):
    # BUG: should raise ZeroDivisionError when b == 0
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b