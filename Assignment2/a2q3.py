def count_chars(text):
    return len(text)

def main():
    user_input = input("Give a string. ")
    number_of_chars = count_chars(user_input)
    print(f'That word has "{number_of_chars}" characters in it.')

if __name__ == "__main__":
    main()