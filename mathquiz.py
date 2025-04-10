import random
score = 0
num_questions = 5

print('Welcome to Math Quiz Game')
print(f'You will be asked {num_questions} questions.\n')

for i in range(num_questions):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(['+','-','*'])

    if operator =='+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    user_answer = int(input(f"Q{i+1}: What is {num1} {operator} {num2}? "))

    if user_answer == correct_answer :
        print("Correct!\n ")
        score += 1

    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")

print(f"Quiz finished! You got {score} out of {num_questions} right.")
