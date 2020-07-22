def alphabet_position(text):
    letters_to_numbers = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                          "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                          "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                          "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    list_of_letters = []
    list_of_letters.clear()

    for letter in text:
        if letter.lower() in letters_to_numbers:
            list_of_letters.append(str(letters_to_numbers.get(letter.lower())))

    return " ".join(list_of_letters)


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("Hello world!"))
print(alphabet_position("Don't tell me I can't do that because I know that I can"))

