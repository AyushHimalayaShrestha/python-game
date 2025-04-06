import random

def paper_scissor_rock():
    choices = ["paper","scissor","rock"]
    computer =random.choice(choices)
    user = input("Choose paper, scissor or rock: ").lower()

    if user == computer:
        print("It's a draw. ")

    elif (user == "paper" and computer == "rock") or \
        (user == "scissor" and computer =="paper") or \
        (user == "rock" and computer == "scissor"):

        print(f"🎉 Congratulations! You won. Computer chose{computer}")

    else:
        print(f"You lose! Computer chose {computer}")

paper_scissor_rock()
