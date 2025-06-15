his script defines the safe_divide function with robust error handling.

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result}"
    except ValueError:
        return "Error: Both inputs must be numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

