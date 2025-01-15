def length_of_last_word(string):
    string = string.strip()
    words = string.split()
    return len(words[-1]) if words else 0

def main():
    user_input = input("Enter a string : ")
    print("Length of the last word :", length_of_last_word(user_input))

if __name__ == "__main__":
    main()
