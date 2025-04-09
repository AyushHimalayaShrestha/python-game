import random

def generate_code():
    digits = [str(i) for i in range(10)]
    code = random.sample(digits, 3)  # Unique digits
    return code

def get_clues(code, guess):
    clues = []

    for i in range(3):
        if guess[i] == code[i]:
            clues.append("Correct")
        elif guess[i] in code:
            clues.append("Close")
        else:
            clues.append("Wrong")

    return clues

# Game starts
secret_code = generate_code()
print("🔐 Welcome to Code Breaker!")
print("Guess the 3-digit code. Digits are unique.")

while True:
    user_input = input("Enter your guess (3 digits): ")

    if len(user_input) != 3 or not user_input.isdigit():
        print("Please enter exactly 3 digits.")
        continue

    guess = list(user_input)
    clues = get_clues(secret_code, guess)

    print("Clues:", ' | '.join(clues))

    if guess == secret_code:
        print("🎉 You cracked the code! Well done.")
        break
