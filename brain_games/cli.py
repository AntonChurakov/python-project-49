import prompt


def welcome_user():
    name_of_gamer = prompt.string('May I have your name? ')
    print(f'Hello, {name_of_gamer}!')
