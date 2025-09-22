def _is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)

def _require_numbers(*vals):
    if not all(_is_number(v) for v in vals):
        raise ValueError("All inputs must be numbers (int or float).")

def fun1(x, y):
    """
    Adds two numbers and returns x + y.
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y)
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers and returns x - y.
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y)
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers and returns x * y.
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y)
    return x * y

def fun4(x, y, z):
    """
    Returns a metrics dictionary for three numbers:
    {
        'sum': x + y + z,
        'mean': (x + y + z) / 3,
        'min': min(x, y, z),
        'max': max(x, y, z),
        'range': max - min
    }
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y, z)
    s = x + y + z
    mn = min(x, y, z)
    mx = max(x, y, z)
    return {
        "sum": s,
        "mean": s / 3,
        "min": mn,
        "max": mx,
        "range": mx - mn,
    }

def safe_divide(x, y):
    """
    Returns x / y, raising ZeroDivisionError if y == 0.
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def power(x, y):
    """
    Returns x ** y.
    Raises ValueError if inputs are not numbers.
    """
    _require_numbers(x, y)
    return x ** y
