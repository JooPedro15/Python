from games import guess_the_number_game
from games import magic_eight_ball_game

user_answer = int(input('''
Enter an option what to play
1. Magic 8 ball game
2. Guess the number game
'''))

if user_answer == 1:
    magic_eight_ball_game()
elif user_answer == 2:
    guess_the_number_game()