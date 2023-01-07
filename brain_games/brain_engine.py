import prompt
QUANTITY_OF_CORRECT_ANSWERS = 3


def launch_game(game):
    print('Welcome to the Brain Games!')
    name_of_gamer = prompt.string('May I have your name? ')
    print(f'Hello, {name_of_gamer}!')
    print(game.rules_of_game)

    for _ in range(QUANTITY_OF_CORRECT_ANSWERS):
        correct_answer = game.question()
        gamer_answer = prompt.string('Your answer: ')

        if gamer_answer != correct_answer:
            print(f"'{gamer_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name_of_gamer}!")
            break
        if gamer_answer == correct_answer:
            print('Correct!')
    else:
        print(f'Congratulations, {name_of_gamer}!')
