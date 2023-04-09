def hangman (word):
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
    print('Вітаємо в грі Шибениця')
    while wrong_guesses < len(stages) - 1:
        print(' \n ')
        guess = input("Вгадайте літеру: ")
        if guess in letters_left:
            character_index = letters_left.index(guess)
            score_board[character_index] = guess
            letters_left[character_index] = '$'
        else:
            wrong_guesses += 1
        print(' '.join(score_board))
        print(' \n '.join(stages[0: wrong_guesses + 1]))
        if '_' not in score_board:
            print('\nВи перемогли! Слово було "{}"\n'.format(word))
            win = True
            break
    if not win:
        print(' \n '.join(stages[0: wrong_guesses + 1]))
        print('\nВи програли! Слово було "{}"\n'.format(word))


if __name__ == "__main__":
    while True:
        word = input("Введіть слово, щоб грати в гру Шибениця: ")
        hangman(word)
    
