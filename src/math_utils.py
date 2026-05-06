def divide(a, b):
    # BUG: should raise ZeroDivisionError when b == 0
    if b == 0:
        return 0
    return a / b
