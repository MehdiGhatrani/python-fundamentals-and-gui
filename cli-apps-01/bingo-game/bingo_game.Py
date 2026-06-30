# global variebles and imports
import random

MIN_NUM = 1
MAX_NUM = 10

# generate random num
def com_num():
    return random.randint(MIN_NUM, MAX_NUM)

# get user input
def user_number():
    print(f"enter your number between ({MIN_NUM}-{MAX_NUM})")
    
    while True:
        try:
            user_guess = int(input("enter your guess: "))
        except ValueError:
            print("Error: enter a valid number")
        else:
            return user_guess
        
# compare numbers
def result(user_guess, com_guess):
    return user_guess == com_guess

# main def
def main():
    MAX_USER_CHOICE = 3

    com_number = com_num()
    
    while MAX_USER_CHOICE > 0:
        user_num = user_number()
        print(com_number)

        if result(user_num, com_number):
            print("you guess right")
            break
        MAX_USER_CHOICE -= 1
        print(f"{MAX_USER_CHOICE} guess left")

    else:
        print("you couldn't guess the number, and ran out of guesses")


if __name__ == "__main__":
    main()

