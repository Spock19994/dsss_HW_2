import random

def generate_random_number(min_val, max_val):
    """
    Generates a random integer between min_val and max_val.       
    Returns:
        int: A random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def generate_random_operator():
    """
    Randomly selects an arithmetic operator from ['+', '-', '*'].
    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def calculate_answer(n1, n2, operator):
    """
    Calculates the result of applying an arithmetic operator to two numbers.
    Returns:
        tuple: A tuple containing the problem as a string and the calculated answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    elif operator == '*':
        answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Runs a math quiz game where the user solves basic arithmetic problems.
    The game generates random math problems, user inputs answer,
    and calculates the score. Displays the final score at the end.
    """
    score = 0
    total_questions = 5  # Total number of questions in the quiz
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate a random problem
        n1 = generate_random_number(1, 10)
        n2 = generate_random_number(1, 5)
        operator = generate_random_operator()
        # Get the problem and the correct answer
        problem, correct_answer = calculate_answer(n1, n2, operator)
        # Loop until valid input is provided
        while True:
            try:
                print(f"\nQuestion: {problem}")
                user_answer = int(input("Your answer: "))
                
                # Check if the answer is correct
                if user_answer == correct_answer:
                    print("Correct! You earned a point.")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer is {correct_answer}.")
                break  # Exit loop if valid input is received

            except ValueError:
                # Handle invalid input and prompt again
                print("Invalid input. Please enter an integer value.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")
if __name__ == "__main__":
    math_quiz()
