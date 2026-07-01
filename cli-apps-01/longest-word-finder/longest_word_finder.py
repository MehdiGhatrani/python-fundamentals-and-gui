# import modules and global variable

# get and split text 
def split_text(text:str):
    clean_text = text.split()
    return clean_text

# count character
def find_longest_words(words:list):
    max_len = max(len(word) for word in words)
    
    longest_words = [word for word in words if len(word) == max_len]
    return longest_words, max_len

# main
def main():
    text = input("enter your text: ")
    words = split_text(text)
    longest_words, max_len = find_longest_words(words)
    print("Longest word(s):")
    for i in longest_words:
        print(f"{i} ({max_len} letters)")


if __name__ == "__main__":
    main()