# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
