from answers import magic_eight_ball_answers
import random

def magic_eight_ball_game():
    while True:
        user_question = input("Ask me anything.")
        user_answer = random.choice(magic_eight_ball_answers)
        print(user_answer)
        next_step = input("Do you have more questions? y/n")
        if next_step.lower() == "y":
            continue
        elif next_step.lower() == "n":
            print("Bye")
            break
        else:
            print("Repeat the question please")
            break

def guess_the_number_game():
    numbers = list(range(1, 11, 1))
    right_number = random.choice(numbers)
    count = 1
    while count <= 3:
        user_answer = int(input("Select a number from 1 to 10: "))
        if user_answer == right_number:
            print("You won")
            break
        elif user_answer != right_number:
            print("Wrong")
            count += 1
            if count >3:
                print(f"You lost, The number was {right_number}")

