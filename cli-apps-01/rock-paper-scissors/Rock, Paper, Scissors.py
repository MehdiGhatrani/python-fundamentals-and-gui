# import librarys and static varieables
import random
choice = ("Rock", "Paper", "Scissors")

# get choice from user
def get_user_choice():
    user_choice = input("Pick your Choice (\"Rock\", \"Paper\", \"Scissors\"): ")
    while user_choice not in choice:
        print("pick True choice")
        user_choice = input("Pick your Choice (\"Rock\", \"Paper\", \"Scissors\"): ")

    return user_choice


# get choice from Computer
def get_Com_choice():
    Com_choice = random.choice(choice)
    print(f"Computer choice is {Com_choice}")
    return Com_choice



# compare results
def Compare(user_choice, Com_choice):
    if user_choice == Com_choice:
        print("DRAW!!!!!!!!")

    elif (user_choice == "Rock" and Com_choice == "Scissors ") or \
        (user_choice ==  "Paper" and Com_choice == "Rock") or \
        (user_choice ==  "Scissors" and Com_choice == "Paper"):
        print("You win")

    else:
        print("Computer win")


# main func
def main():
    user_choice = get_user_choice()
    Com_choice = get_Com_choice()
    Compare_choice = Compare(user_choice, Com_choice)


# make an iteration for doing the game as much we need

answer = "y"

while answer is "y":
    main()
    answer = input("do you want to continue? (y/n) ")
    if answer != "y":
        print("bye")
