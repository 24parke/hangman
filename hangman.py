import getpass

print("Welcome to Hangman! Player1 will choose the word, and Player2 will guess the letters. *6 mistakes* . Good Luck!")

word = getpass.getpass("Player1 choose a word: ")
letters_guessed = []
mistakes = 0
max_guesses = 6
underscore_word = {}

for i in range(len(word)):
    underscore_word[i] = "_ "

for i in range(max_guesses):
    suffix = ""

    if i == 0:
        suffix = "st"
    elif i == 1:
        suffix = "nd"
    elif i == 2:
        suffix = "rd"
    else:
        suffix = "th"

    ask_guesser = "Player2 " + str(i+1) + suffix + " guess: "
    guess = input(ask_guesser)
    if guess in word:
        for letter in word:
            if word[i] == guess:
                underscore_word[i] = guess
    print (underscore_word)

# some change