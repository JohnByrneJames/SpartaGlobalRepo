scrabble_dictionary = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                       "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                       "y": 4, "z": 10}

class WorkOutScrabbleScore:
    current_word_score = 0

    def __init__(self):
        pass

    def word_to_convert(self, word):
        self.current_word_score = 0
        for letter in word:
            self.current_word_score += scrabble_dictionary[letter.lower()]

    def user_interface(self):
        in_program = True
        help_info = "\nWelcome to scrabble word converter.\n" \
                    "To exit enter [E]\n" \
                    "To help enter [H]\n" \
                    "If you want to convert a word simply enter it."

        print(help_info)

        while in_program:
            user_input = input("\nWhat word would you like to convert?\n")

            try:
                if user_input.lower() == "e":
                    print("Thank you for using Converter...")
                    print("Exiting...")
                elif user_input.lower() == "h":
                    print("\n" + help_info)
                else:
                    self.word_to_convert(user_input)
                    print(self.current_word_score)
            except TypeError:
                print("\nIt seems that you have entered an unexpected letter/ character")
            except KeyError as e:
                print("\nSorry characters like " + str(e) + " are not allowed")


# Instance
user_instance = WorkOutScrabbleScore()
user_instance.user_interface()
