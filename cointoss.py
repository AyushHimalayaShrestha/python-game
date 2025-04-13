import random
options =['heads', 'tails']
print("Welcome! to coin toss game")

user_choice = input('Choose heads or tails:').lower()
if user_choice not in options:
    print("Invalid choice! Please choose 'heads' or 'tails' ")

else:
    result =random.choice(options)
    print(f"Tossing the coin... It's {result}!")

if user_choice == result:
    print("You Win!")

else:
    print("You lose! Better luck next time.")
