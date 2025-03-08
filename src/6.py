import random

def generate_math_problem(difficulty):
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return num1 * num2
    elif difficulty == "medium":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        return num1 + num2
    else:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        return num1 - num2

# Test the function
print(generate_math_problem("easy"))
print(generate_math_problem("medium"))
print(generate_math_problem("hard"))