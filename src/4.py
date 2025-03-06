import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operator (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])

    # Evaluate the math problem using eval()
    result = eval(f"{num1} {op} {num2}")

    return f"What is {num1} {op} {num2}?"
