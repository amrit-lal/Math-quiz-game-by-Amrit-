import random

# Function to calculate the correct answer
def get_correct_ans(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return round(num1 / num2, 2) if num2 != 0 else None # Prevent division by zero
    elif operator == "%":
        return num1 % num2

# Operator descriptions
operator_descriptions = {
    "+": "Add",
    "-": "Subtract",
    "*": "Multiply",
    "/": "Divide (up to 2 decimal places)",
    "%": "Modulus",
}

# Initialize
operators = ["+", "-", "*", "/", "%"]
score = 0
output_lines = [] # To store outputs

# Ask user for name and number of questions
user_name = input("Enter your name: ")
num_questions = int(input("How many questions would you like to answer? "))

# Start the quiz
for i in range(num_questions):
    # Generate two random integers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    # Generate random operator
    operator = random.choice(operators)

    # Ensure no division by zero
    if operator == "/" and num2 == 0:
        num2 = random.randint(1, 9)

    # Print description of operator
    print(f"{operator_descriptions[operator]}:")

    # Get user input
    user_input = float(input(f"{num1} {operator} {num2} = "))

    # Get correct answer
    correct_ans = get_correct_ans(num1, num2, operator)

    # Check if the answer is correct
    if correct_ans is not None and user_input == correct_ans:
        score += 1
        result = "Correct"
    else:
        result = "Incorrect"

    # Append result to output_lines
    output_lines.append(f"Q{i+1}: {num1} {operator} {num2} = {correct_ans} (Your answer: {user_input}) - {result}")

# Print total score
total_score = f"Your total score is: {score}/{num_questions}"
print(total_score)
output_lines.append(total_score)

# Create a txt file and save output
file_name = f"{user_name}_math_quiz_result.txt"
with open(file_name, 'w') as file:
    file.write(f"Math Quiz Results for {user_name}\n")
    file.write("\n".join(output_lines))

print(f"Results have been saved to {file_name}.")
