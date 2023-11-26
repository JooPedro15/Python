from tkinter import *
import random

# GAME CODE
options = ['Rock', 'Paper', 'Scissors']


def user_rock():
    user_choice.set('Rock')
    computer = random.choice(options)

    if computer == 'Rock':
        computer_choice.set(computer)
        outcome.set('DRAW')
    elif computer == 'Paper':
        computer_choice.set(computer)
        outcome.set('LOST')
    elif computer == 'Scissors':
        computer_choice.set(computer)
        outcome.set('WIN')


def user_paper():
    user_choice.set('Paper')
    computer = random.choice(options)

    if computer == 'Rock':
        computer_choice.set(computer)
        outcome.set('WIN')
    elif computer == 'Paper':
        computer_choice.set(computer)
        outcome.set('DRAW')
    elif computer == 'Scissors':
        computer_choice.set(computer)
        outcome.set('LOST')


def user_scissors():
    user_choice.set('Scissors')
    computer = random.choice(options)

    if computer == 'Rock':
        computer_choice.set(computer)
        outcome.set('LOST')
    elif computer == 'Paper':
        computer_choice.set(computer)
        outcome.set('WIN')
    elif computer == 'Scissors':
        computer_choice.set(computer)
        outcome.set('DRAW')


window = Tk()

computer_choice = StringVar()
user_choice = StringVar()
outcome = StringVar()

window.config(background='Black')

# FRAMES
frame_title = Frame(window)
frame_title.config(background='black', )
frame_title.pack()
frame_spacer = Frame(window)
frame_spacer.config(height=50, background='black')
frame_spacer.pack()
frame_output_computer = Frame(window)
frame_output_computer.config()
frame_output_computer.pack(anchor='center')
frame_output_user = Frame(window)
frame_output_user.config()
frame_output_user.pack(anchor='center')
frame_buttons = Frame(window)
frame_buttons.pack(side=BOTTOM)
frame_result = Frame(window)
frame_result.pack(side=BOTTOM)

# TITLE
label_title1 = Label(frame_title,
                     text='GAME',
                     font=('Calibri', 25),
                     bg='black',
                     fg='white')
label_title1.pack()
label_title2 = Label(frame_title,
                     text='Rock, Paper, Scissors',
                     font=('Calibri', 20),
                     bg='black',
                     fg='white')
label_title2.pack()


# OUTPUT
label_computer = Label(frame_output_computer,
                       text='COMPUTER:',
                       font=('Calibri', 20),
                       fg='white',
                       bg='black')
label_computer.pack(side=LEFT)
label_computer_output = Label(frame_output_computer,
                              textvariable=computer_choice,
                              font=('Calibri', 20),
                              fg='white',
                              bg='black')
label_computer_output.pack()

label_user = Label(frame_output_user,
                   text='YOU:',
                   font=('Calibri', 20),
                   fg='white',
                   bg='black')
label_user.pack(side=LEFT)
label_user_output = Label(frame_output_user,
                          textvariable=user_choice,
                          font=('Calibri', 20),
                          fg='white',
                          bg='black')
label_user_output.pack()

label_result = Label(frame_result,
                     textvariable=outcome,
                     font=('Calibri', 20),
                     fg='white',
                     bg='black')
label_result.pack()

# BUTTONS
button_rock = Button(frame_buttons,
                     text='Rock',
                     font=('Calibri', 20),
                     fg='white',
                     height=2,
                     width=10,
                     background='black',
                     activeforeground='black',
                     activebackground='silver',
                     command=user_rock,
                     relief='flat')
button_rock.pack(side=LEFT)

button_paper = Button(frame_buttons,
                      text='Paper',
                      font=('Calibri', 20),
                      fg='white',
                      height=2,
                      width=10,
                      background='black',
                      activeforeground='black',
                      activebackground='silver',
                      command=user_paper,
                      relief='flat')
button_paper.pack(side=LEFT)

button_scissors = Button(frame_buttons,
                         text='Scissors',
                         font=('Calibri', 20),
                         fg='white',
                         height=2,
                         width=10,
                         background='black',
                         activeforeground='black',
                         activebackground='silver',
                         command=user_scissors,
                         relief='flat')
button_scissors.pack(side=LEFT)


window.mainloop()
