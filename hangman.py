import getpass
from random_word import RandomWords

mode = -1

while mode == -1:
    try:
        mode = int(input(
            '''
Welcome to Hangman! Please choose a mode: 1 (Player1 choose word, player2 guess)
                                          2 (Both players choose a word and guess)
                                       or 3 (CPU choose word, player guess)
            '''
        ))
        if mode not in (1, 2, 3):
            mode = -1
            print("Please choose either 1, 2, or 3.")

    except ValueError:
        print("Please choose either 1, 2, or 3.")

if mode == 1:
    print(
        "Welcome to Hangman! Player1 will choose the word, and Player2 will guess the letters. *6 mistakes* Good Luck!")

    word = getpass.getpass("Player1 choose a word: ")
    if len(word) > 19:
        print("Please choose a shorter word.")
        word = getpass.getpass("Player1 choose a word: ")
    if not word.isalpha:
        print("Please choose a word with only letters.")
        word = getpass.getpass("Player1 choose a word: ")

    letters_guessed = ""
    lives = 6
    underscore_word = ["_ " for i in word]
    increment = 0
    lose = False

    while lives > 0 and "_ " in underscore_word and lose is False:
        for i in range(20):
            suffix = ""

            if increment == 0:
                suffix = "st"
            elif increment == 1:
                suffix = "nd"
            elif increment == 2:
                suffix = "rd"
            elif 4 <= increment < 19:
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
                print("Lives: " + str(lives))

                if "".join(underscore_word).isalpha():
                    print("Player2 wins!🙂")
                    break

            else:
                lives -= 1
                letters_guessed += guess
                print("Word: " + " ".join(underscore_word))
                print("Letters guessed: " + ", ".join(letters_guessed))
                print("Lives: " + str(lives))

                if lives == 0:
                    print("Player2 loses!🙁")
                    lose = True
                    break

                # ______________________________________________________________________________________________
                # M O D E 2

elif mode == 2:
    print(
        "Welcome to Hangman! Choose a word, then guess the other player's word. First to guess wins!")

    p1word = getpass.getpass("Player1 choose a word: ")
    if len(p1word) > 19:
        print("Please choose a shorter word.")
        p1word = getpass.getpass("Player1 choose a word: ")
    if not p1word.isalpha:
        print("Please choose a word with only letters.")
        p1word = getpass.getpass("Player1 choose a word: ")

    p2word = getpass.getpass("Player2 choose a word: ")
    if len(p2word) > 19:
        print("Please choose a shorter word.")
        p2word = getpass.getpass("Player2 choose a word: ")
    if not p2word.isalpha:
        print("Please choose a word with only letters.")
        p2word = getpass.getpass("Player2 choose a word: ")

    p1letters_guessed = ""
    p1underscore_word = ["_ " for i in p1word]
    p1increment = 0
    p1lives = 6
    p1win = False

    p2letters_guessed = ""
    p2underscore_word = ["_ " for i in p2word]
    p2increment = 0
    p2lives = 6
    p2win = False

    while p2win is False and p1win is False:
        # PLAYER 1 TURN

        print("\n" + "__________player1 turn__________")
        print("Word: {}\nLetters guessed: {}\nLives: {}".format(" ".join(p2underscore_word), ", ".join(p1letters_guessed), p1lives))
        p1guess = input("player1 guess: ")

        if len(p1guess) > 1:
            if p1guess == p2word:
                print("\n" + "Player1 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p1win = True
                break
            else:
                print("\n" + "Player2 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p2win = True
                break

        if p1guess in p2word and p1guess not in p1letters_guessed:

            for idx, char in enumerate(p2word):
                if char == p1guess:
                    p2underscore_word[idx] = p1guess

            p1letters_guessed += p1guess
            print("Word after guess: " + " ".join(p2underscore_word))
            print("Letters guessed: " + ", ".join(p1letters_guessed))
            print("Lives: " + str(p1lives))

            if "".join(p2underscore_word).isalpha() or p2lives == 0:
                print("\n" + "Player1 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p1win = True
                break

        else:
            p1letters_guessed += p1guess
            p1lives -= 1
            print("Word after guess: " + " ".join(p2underscore_word))
            print("Letters guessed: " + ", ".join(p1letters_guessed))
            print("Lives: " + str(p1lives))
            if p1lives == 0:
                print("\n" + "Player2 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p2win = True
                break

            # PLAYER 2 TURN
        # _____________________________________________________________________________________________________

        print("\n" + "__________player2 turn__________")
        print("Word: {}\nLetters guessed: {}\nLives: {}".format(" ".join(p1underscore_word), ", ".join(p2letters_guessed), p2lives))
        p2guess = input("player2 guess: ")

        if len(p2guess) > 1:
            if p2guess == p1word:
                print("\n" + "Player2 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p2win = True
                break
            else:
                print("\n" + "Player1 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p1win = True
                break

        if p2guess in p1word and p2guess not in p2letters_guessed:

            for idx, char in enumerate(p1word):
                if char == p2guess:
                    p1underscore_word[idx] = p2guess

            p2letters_guessed += p2guess
            print("Word after guess: " + " ".join(p1underscore_word))
            print("Letters guessed: " + ", ".join(p2letters_guessed))
            print("Lives: " + str(p2lives))

            if "".join(p1underscore_word).isalpha() or p1lives == 0:
                print("\n" + "Player2 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p2win = True
                break

        else:
            p2letters_guessed += p2guess
            p2lives -= 1
            print("\n" + "Word after guess: " + " ".join(p1underscore_word))
            print("Letters guessed: " + ", ".join(p2letters_guessed))
            print("Lives: " + str(p2lives))
            if p2lives == 0:
                print("\n" + "Player1 wins!🙂" + "\n" + "player1 word: " + p1word + "\n" + "player2 word: " + p2word)
                p1win = True
                break

                # ______________________________________________________________________________________________
                # M O D E 3

elif mode == 3:
    generator = RandomWords()
    CPU = generator.get_random_word()

    letters_guessed = ""
    lives = 6
    underscore_word = ["_ " for i in CPU]
    increment = 0
    lose = False

    print("\n" + "".join(underscore_word))

    while lives > 0 and "_ " in underscore_word and lose is False:
        for i in range(20):
            suf = ""

            if increment == 0:
                suf = "st"
            elif increment == 1:
                suf = "nd"
            elif increment == 2:
                suf = "rd"
            elif 3 <= increment < 19:
                suf = "th"
            increment += 1
            print("\n" + "Letters guessed so far: " + ", ".join(letters_guessed))
            ask_player = "Your " + str(i + 1) + suf + " guess: "
            guess_char = input(ask_player)

            if guess_char in CPU:

                for idx, char in enumerate(CPU):
                    if char == guess_char:
                        underscore_word[idx] = guess_char

                if guess_char not in letters_guessed:
                    letters_guessed += guess_char
                print("Word: " + " ".join(underscore_word))
                print("Letters guessed: " + ", ".join(letters_guessed))
                print("Lives: " + str(lives))

                if "".join(underscore_word).isalpha():
                    print("You win!🙂")
                    break

            else:
                lives -= 1
                letters_guessed += guess_char
                print("Word: " + " ".join(underscore_word))
                print("Letters guessed: " + ", ".join(letters_guessed))
                print("Lives: " + str(lives))

                if lives == 0:
                    print("You lose!🙁")
                    print(CPU)
                    lose = True
                    break
