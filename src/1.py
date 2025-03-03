
import random

def get_random_math_problem(numbers):
    """Returns a randomly generated math problem."""
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    oper = random.choice(['+', '-', '*', '/'])
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    else:
        return num1 / num2