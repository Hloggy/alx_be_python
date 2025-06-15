# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return f"Result: {result}"

    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
