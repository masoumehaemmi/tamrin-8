import random
items = ["Rock", "Paper", "Scissor"]

computer_score = 0
user_score = 0


print("0- Rock")
print("1- Paper")
print("2- Scissor")
print("3- Exit")

user_choice_index = int(input("Please enter number:"))

while (user_choice_index != 3):
    if(user_choice_index not in [0,1,2,3]):
        print("wrong number!!!!")
        user_choice_index = int(input("Enter number 0, 1, 2, 3:"))
        continue
    computer_choice  = random.choice(items)
    user_choice = items[user_choice_index]

    if (computer_choice == "Rock" and user_choice == "Scissor") or (computer_choice == "Scissor" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Rock"):
        computer_score += 1
        print ("Computer Won!")
    else:
        user_score += 1
        print ("You Won!" )
    user_choice_index = int(input())

if (computer_score == user_score):
    print("Equal Scores")
elif (computer_score > user_score):
    print("Computer won" ) 
else:
     print("You won" )