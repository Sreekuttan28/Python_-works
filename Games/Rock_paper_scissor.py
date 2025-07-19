
import random
print("Welcome to the Rock, Paper & Scissor".center(60))
print("There are 5 rounds winner will be decide of Best of 5 rounds 😉".center(60))

Choices = ["rock","paper","scissor"]

icons ={
    "rock":"🪨",
    "paper":"🗞️",
    "scissor":"✂️"
}

rounds = 5
user_score = 0
cmp_score = 0
for rounds in range(1,rounds+1):
    print(f" Round {rounds}")
    user_choice = input("Please choose 'Rock', 'Paper','Scissor' or 'Q' for Quit: ").lower()

    if user_choice == "q":

        print("Thanks for playing!!".center(60))
        break
    if user_choice not in Choices:
        print("Invalid value entered try again".center(60))
        continue
    cmp_choice = random.choice(Choices)
    print(f" You have choosen:{icons[user_choice]}   VS  Computer has choosen:{icons[cmp_choice]}".center(60))
    if user_choice == cmp_choice:

        print("Oopsie it's a tie ".center(60))
    elif ((user_choice == "rock" and cmp_choice =="scissor") or ( user_choice=="scissor" and cmp_choice == "paper") or (user_choice == "paper" and cmp_choice =="rock") ):
        print(" You have won🥳!!!! ".center(60))
        user_score += 1
    
    else:
        print("Oopsiee This time Computer won! try again ".center(60))

        cmp_score += 1

print("\n")
print(" All Rounds over ".center(60))

if user_score == cmp_score:
    print(F"Well played both sccore {cmp_score} Scores Tie breaker!!!".center(60))

elif user_score > cmp_score:
    print(f" The champion for the day is you🥳 with the score of {user_score}".center(60))

else:
    print(f"Unfortunately the winner is the computer with the score of {cmp_score}, well played bruhhhh!!".center(60))

print("Thanks for participating cheerss!!!!!".center(60))


