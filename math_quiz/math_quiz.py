import random
def generate_random_int(min, max):
    """
    Generates a random integer within the range
    specified by the parameters  'min' and 'max'.
    : min: minimum range
    : max: maximum range
    """
    return random.randint(min, max)

def choose_operator():
    """
    Chooses a random mathematical operator ( +, - or *).
    """
    return random.choice(['+', '-', '*'])

def calculation(number1, number2, operator):
    """
    Do mathematical operation between numbers (number1 and number2),
    with the operator 'o'.
    : number1: number 1
    : number2: number 2
    : operator: mathematical operator
    """
    question = f"{number1} {operator} {number2}"
    if operator == '+':
        problem_result = number1 + number2
    elif operator == '-':
        problem_result = number1 - number2
    else:
        problem_result = number1 * number2
    return question, problem_result

def math_quiz():
    """
    Maths quiz with a total of 3 questions, with each question carrying 1 point.
    """
    score = 0
    total_questions = 3      # Maximum number of questions in the quiz.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Generating random integers and operators for problem solving.
    for _ in range(total_questions):
        number1 = generate_random_int(1, 10) # Generates a random integer between 1 and 10.
        number2 = generate_random_int(1, 5)  # Generates a random integer between 1 and 10.
        operator = choose_operator()         # Chooses a random operator for solving the problem.

        problem, answer = calculation(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        # Verifying if the user input is an integer, else returns an error.
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            # returns error if user output isn't integer
            print("Invalid input. Please enter a valid number.")
            continue

        # Checking if the user answer matched with the actual problem_result
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1   # Score increases by 1 point for each correct answers.
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Final display of the game score.
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()