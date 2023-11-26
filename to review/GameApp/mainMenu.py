from tkinter import *


def game_rps():
    new_window = Tk()
    print('rps selected')


def game_quiz():
    new_window = Tk()
    print('quiz selected')


def game_guessnum():
    new_window = Tk()
    print('guess num selected')


mainMenu = Tk()
mainMenu.title('Games')
mainMenu.geometry('350x500')
mainMenu.config(background='black')

frame_intro = Frame(mainMenu, bg="black")
frame_intro.pack(anchor='n')
frame_space = Frame(mainMenu, bg='black')
frame_space.config(height=1, width=200, bg='silver')
frame_space.pack()

frame_game1 = Frame(mainMenu, bg='black')
frame_game1.config()
frame_game1.pack(anchor='w')
frame_game2 = Frame(mainMenu, bg='black')
frame_game2.config(height=20)
frame_game2.pack(anchor='w')
frame_game3 = Frame(mainMenu, bg='black')
frame_game3.config(height=20)
frame_game3.pack(anchor='w')

frame_foot = Frame(mainMenu)
frame_foot.config()
frame_foot.pack(side=BOTTOM)
frame_space = Frame(mainMenu, bg='black')
frame_space.config(height=1, width=200, bg='silver')
frame_space.pack(side=BOTTOM)


label_hello = Label(frame_intro,
                    text='Hello',
                    font=('Avenir', 25),
                    fg='silver',
                    bg='black')
label_hello.pack()

label_instructions = Label(frame_intro,
                           text='Please, choose a game:',
                           font=('Avenir', 20),
                           fg='silver',
                           bg='black')
label_instructions.pack()


label_game_rps = Label(frame_game1,
                       text='Rock, Paper, Scissors',
                       font=('Avenir', 13),
                       fg='white',
                       height=1,
                       width=25,
                       anchor='w',
                       padx=10,
                       bg='black',
                       relief='flat',)
label_game_rps.pack(side=LEFT)
button_game_rps = Button(frame_game1,
                         command=game_rps,
                         text='Select',
                         font=('Avenir', 13),
                         fg='white',
                         height=1,
                         width=10,
                         bg='black',
                         activebackground='black',
                         activeforeground='orange',
                         relief='flat')
button_game_rps.pack(side=RIGHT)


label_game_quiz = Label(frame_game2,
                        text='Quiz',
                        font=('Avenir', 13),
                        fg='white',
                        anchor='w',
                        padx=10,
                        height=1,
                        width=25,
                        bg='black',
                        relief='flat')
label_game_quiz.pack(side=LEFT)
button_game_quiz = Button(frame_game2,
                          command=game_quiz,
                          text='Select',
                          font=('Avenir', 13),
                          fg='white',
                          height=1,
                          width=10,
                          bg='black',
                          activebackground='black',
                          activeforeground='orange',
                          relief='flat')
button_game_quiz.pack(side=RIGHT)


label_game_guessnum = Label(frame_game3,
                            text='Guess the number',
                            font=('Avenir', 13),
                            fg='white',
                            height=1,
                            width=25,
                            anchor='w',
                            padx=10,
                            bg='black',
                            relief='flat')
label_game_guessnum.pack(side=LEFT)
button_game_guessnum = Button(frame_game3,
                              command=game_guessnum,
                              text='Select',
                              font=('Avenir', 13),
                              fg='white',
                              height=1,
                              width=10,
                              bg='black',
                              activebackground='black',
                              activeforeground='orange',
                              relief='flat')
button_game_guessnum.pack(side=RIGHT)


label_foot = Label(frame_foot,
                   text='Joao Silva - 2023',
                   font=('Consolas', 9),
                   fg='silver',
                   bg='black')
label_foot.pack()

mainMenu.mainloop()
