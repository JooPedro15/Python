import random
"""
Games index:
Rock, Paper, Scissors
"""


def rps():
    """
    Info: Rock, paper, Scissors game against the computer.
    :return: Computer choice, User choice and outcome.
    """
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('Type an option: rock, paper, scissors').lower()
    if win[user_choice] == computer_choice:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"You WON!")
    if win[computer_choice] == user_choice:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"You LOST!")
    else:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"DRAW!")