import random

def get_random_math_problem():
    numbers = list(range(1, 10))
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    operation = random.choice(["+", "-", "*", "/"])
    result = eval(f"{number1} {operation} {number2}")
    return f"What is {number1} {operation} {number2}?"
