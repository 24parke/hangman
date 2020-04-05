import getpass

print("Welcome to Hangman! Player1 will choose the word, and Player2 will guess the letters. *6 mistakes* . Good Luck!")

word = getpass.getpass("Player1 choose a word: ")
if len(word) > 19:
    print("Please choose a shorter word.")
    word = getpass.getpass("Player1 choose a word: ")
if not word.isalpha:
    print("Please choose a word with only letters.")
    word = getpass.getpass("Player1 choose a word: ")

letters_guessed = ""
mistakes = 0
underscore_word = []
increment = 0
lose = False

for i in range(len(word)):
    underscore_word += "_"

while mistakes <= 6 and "_" in underscore_word and lose == False:
    for i in range(20):
        suffix = ""

        if increment == 0:
            suffix = "st"
        elif increment == 1:
            suffix = "nd"
        elif increment == 2:
            suffix = "rd"
        elif 19 > increment > 3:
            suffix = "th"
        increment += 1
        ask_guesser = "Player2 " + str(i + 1) + suffix + " guess: "
        guess = input(ask_guesser)


        if guess in word:

            for idx, char in enumerate(word):
                if char == guess:
                    underscore_word[idx] = guess

            if guess not in letters_guessed:
                letters_guessed += guess
            print("Word: " + " ".join(underscore_word))
            print("Letters guessed: " + ", ".join(letters_guessed))
            print("Mistakes: " + str(mistakes))

            if "".join(underscore_word).isalpha():
                print("Player2 wins!🙂")
                break

        else:
            mistakes += 1
            letters_guessed += guess
            print("Word: " + " ".join(underscore_word))
            print("Letters guessed: " + ", ".join(letters_guessed))
            print("Mistakes: " + str(mistakes))

            if mistakes == 6:
                print("Player2 loses!🙁")
                lose = True
                break
