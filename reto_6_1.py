
class InvalidOperatorError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass

class InputTypeError(Exception):
    pass


def ensure_number(x, name):
    if not isinstance(x, (int, float)):
        raise InputTypeError(f"'{name}' must be numeric (int or float). Got: {type(x).__name__}")

def ensure_operator(op):
    valid_ops = ["+", "-", "*", "/"]
    if op not in valid_ops:
        raise InvalidOperatorError(f"Invalid operator. Use one of: {', '.join(valid_ops)}")

def ensure_divisor_not_zero(b):
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")


def operate(a, b, op):
    """Perform +, -, * or / on a and b based on 'op'."""
    ensure_number(a, "a")
    ensure_number(b, "b")
    ensure_operator(op)

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        ensure_divisor_not_zero(b)
        return a / b


if __name__ == "__main__":
    try:
        print("=== Basic Operations ===")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Enter operation (+, -, *, /): ")
        print("Result:", operate(a, b, op))
    except Exception as e:
        print("Error:", e)

