import prompt
ROUNDS_QUANTITY = 3


def launch(game):
    print('Welcome to the Brain Games!')
    name_of_gamer = prompt.string('May I have your name? ')
    print(f'Hello, {name_of_gamer}!')
    print(game.RULES_OF_GAME)

    for _ in range(ROUNDS_QUANTITY):
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        gamer_answer = prompt.string('Your answer: ')

        if gamer_answer != correct_answer:
            print(f"'{gamer_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name_of_gamer}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name_of_gamer}!')
