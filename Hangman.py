def hangman ():
    word = "cat"
    wrong_guesses = 0
    stages = ["",
              "_________",
              "|     | ",
              "|     0",
              "|    /|\ ",
              "|    / \ ",
              "| ",
              "---------"]
    letters_left = list(word)
    score_board = ['_'] * len(word)
    win = False
    print('Welcome to Hang Man')
    while wrong_guesses < len(stages) - 1:
        print(' \n ')
        guess = input("Guess a letter: ")
        if guess in letters_left:
            character_index = letters_left.index(guess)
            score_board[character_index] = guess
            letters_left[character_index] = '$'
        else:
            wrong_guesses += 1
        print(' '.join(score_board))
        print(' \n '.join(stages[0: wrong_guesses + 1]))
        if '_' not in score_board:
            print('\nYou win! The word was {}'.format(word))
            win = True
            break
    if not win:
        print(' \n '.join(stages[0: wrong_guesses + 1]))
        print('\nYou lose! The words was {}'.format(word))


hangman()
