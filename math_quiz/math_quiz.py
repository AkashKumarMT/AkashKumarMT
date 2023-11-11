import random


def generate_random_integer(min, max):
    """
    Returns a random integer within the given range.
    """
    return random.randint(min, max)


def operator():
    """
    Selecting the operator randomly from the list and returns the same.
    """
    return random.choice(['+', '-', '*'])


def arithmetic(num1, num2, op):
    """
    This functions accepts two integers and an operator as arguments.
    Based on the given operator, the arithmetic operation is performed for the given two numbers.
    The problem statement and the result are returned
    """
    problem = f"{num1} {op} {num2}"
    if op == '+': result = num1 + num2  # Adding num1 and num2
    elif op == '-': result = num1 - num2  # Subtracting num2 from num1
    else: result = num1 * num2  # Multiplying num1 and num2
    return problem, result  # Returning the question and the answer


def math_quiz():
    """
    This function generates two random integers by calling the function generate_random_integer.
    Then it chooses one of the operator randomly from +,-,* by calling the function operator.
    Later, it invokes the function arithmetic that performs the operation on the chosen number.
    Finally, it calculates the total score of the user.

    Total number of questions must be initialised on total_questions.
    """
    score = 0  # Initialising the score to 0
    total_questions = int(3.14159265359)  # Converting the total number of questions to integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10); num2 = generate_random_integer(1, 5); op = operator()  # Generating 2 random numbers, and an operator by calling the respective functions
        problem, answer = arithmetic(num1, num2, op)  # Performing the arithmetic operation
        print(f"\nQuestion: {problem}")

        while True:  # This will prompt the user until a valid input is given.
            try:
                user_input = input("Your answer: ")  # get the answer from the user.
                useranswer = int(user_input)

                if useranswer == answer:  # Calculate the score
                    print("Correct! You earned a point.")
                    score += 1  # Increment the score by 1 for each correct answer.

                else:
                    print(f"Wrong answer. The correct answer is {answer}.")  # Display the correct answer if the user makes a mistake.

                break  #Breaks the loop if the input is valid.

            except ValueError:  # Validating user input to ensure it is an integer using exceptional handling.
                print('Invalid input. Please enter a valid integer.')

    print(f"\nGame over! Your score is: {score}/{total_questions}")  # Display the total score


if __name__ == "__main__":
    math_quiz()
