import random

rounds = 5
user_score = 0
computer_score = 0

print("🎲 Welcome to Dice War!")
print(f"You'll battle the computer for {rounds} rounds!\n")

for i in range(1, rounds + 1):
    input(f"🔁 Press Enter to roll for Round {i}...")

    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)

    print(f"🧍 You rolled: {user_roll}")
    print(f"💻 Computer rolled: {comp_roll}")

    if user_roll > comp_roll:
        print("✅ You win this round!\n")
        user_score += 1
    elif comp_roll > user_roll:
        print("❌ Computer wins this round.\n")
        computer_score += 1
    else:
        print("⚖️ It's a tie!\n")

# Final result
print("🏁 Game Over!")
print(f"Your Score: {user_score} | Computer Score: {computer_score}")

if user_score > computer_score:
    print("🎉 You win the Dice War!")
elif computer_score > user_score:
    print("😞 Computer wins the Dice War!")
else:
    print("🤝 It's a draw!")

