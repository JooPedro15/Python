from tkinter import *
import random


def user_1():
    user = 1
    user_out.set(user)
    computer = random.randint(1, 3)
    comp_out.set(computer)
    if computer == user:
        result.set('WIN')
    else:
        result.set('LOSE')


def user_2():
    user = 2
    user_out.set(user)
    computer = random.randint(1, 3)
    comp_out.set(computer)
    if computer == user:
        result.set('WIN')
    else:
        result.set('LOSE')


def user_3():
    user = 3
    user_out.set(user)
    computer = random.randint(1, 3)
    comp_out.set(computer)
    if computer == user:
        result.set('WIN')
    else:
        result.set('LOSE')


window = Tk()
window.config(background='black')

comp_out = IntVar()
user_out = IntVar()
result = StringVar()

# Frames
frame_intro = Frame(window)
frame_intro.config(background='black')
frame_intro.pack(side=TOP)
frame_buttons = Frame(window)
frame_buttons.config(background='silver')
frame_buttons.pack(side=TOP)
frame_label1 = Frame(window)
frame_label1.config(background='black')
frame_label1.pack(side=TOP)
frame_label2 = Frame(window)
frame_label2.config(background='black')
frame_label2.pack(side=TOP)
frame_label3 = Frame(window)
frame_label3.config(background='black')
frame_label3.pack(side=TOP)

# Labels
label_intro = Label(frame_intro,
                    text='Guess the number',
                    font=('Calibri', 25),
                    fg='white',
                    background='black')
label_intro.pack()
label_instructions = Label(frame_intro,
                           text='Try to guess \na random number between 1 and 3.',
                           font=('Calibri', 10),
                           fg='white',
                           background='black')
label_instructions.pack()


# Buttons
button1 = Button(frame_buttons,
                 text='1',
                 font=('Calibri', 20),
                 fg='black',
                 background='silver',
                 width=5,
                 command=user_1)
button1.pack(side=LEFT)


button2 = Button(frame_buttons,
                 text='2',
                 font=('Calibri', 20),
                 fg='black',
                 background='silver',
                 width=5,
                 command=user_2)
button2.pack(side=LEFT)

button3 = Button(frame_buttons,
                 text='3',
                 font=('Calibri', 20),
                 fg='black',
                 background='silver',
                 width=5,
                 command=user_3)
button3.pack(anchor='nw')


# Outputs
label_computer = Label(frame_label1,
                       text='Computer:',
                       font=('Calibri', 15),
                       fg='white',
                       background='black')
label_computer.pack(side=LEFT)
label_computer_output = Label(frame_label1,
                              textvariable=comp_out,
                              font=('Calibri', 15),
                              fg='white',
                              background='black')
label_computer_output.pack(side=RIGHT)

label_user = Label(frame_label2,
                   text='User:',
                   font=('Calibri', 15),
                   fg='white',
                   background='black')
label_user.pack(side=LEFT)
label_user_output = Label(frame_label2,
                          textvariable=user_out,
                          font=('Calibri', 15),
                          fg='white',
                          background='black')
label_user_output.pack(side=RIGHT)

label_result = Label(frame_label3,
                     text='Result:',
                     font=('Calibri', 15),
                     fg='white',
                     background='black')
label_result.pack(side=LEFT)
label_result_out = Label(frame_label3,
                         textvariable=result,
                         font=('Calibri', 15),
                         fg='white',
                         background='black')
label_result_out.pack(side=RIGHT)

window.mainloop()
