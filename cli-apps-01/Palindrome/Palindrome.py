# modules and global variable

# check palindrome
def check_palindrome(word:str):
    word = word.lower()
    reverse_word = word[::-1]
    if word == reverse_word:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."
    
# main 

def main():
    while True:

        word = input("Please enter a word to check if it's a palindrome or not: ")
        
        print(check_palindrome(word))

        question = input("Do you want to continue? (y/n): ").lower()
        if question != "y":
            print("Bye!")
            break   


main()