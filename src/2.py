import random

def get_random_math_problem():
    numbers = list(range(1, 10))
    operands = ["+", "-", "*", "/"]
    number_of_operands = random.choice(numbers)

    problem = ""
    for i in range(number_of_operands):
        problem += f"{random.choice(numbers)} {random.choice(operands)} "

    return eval(problem)
