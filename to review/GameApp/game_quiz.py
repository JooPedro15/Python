from tkinter import *

questions = {"What is the capital of Portugal": "A",
             "Is the earth round?": "C",
             'who is the owner of tesla?': 'C'}

options = [["A. Lisbon", "B. Porto", "C. Faro", "C. Coimbra"],
           ["A. NO", "B. Maybe", "C. Yes", "D. I don't know"],
           ['Me', 'Manuel', 'Elon', 'Biden']]

var = ['q1', 'q2', 'q3']


def review_q1():
    pass



window = Tk()
window.config()
var = ['q1', 'q2', 'q3']
q1 = StringVar()
q2 = StringVar()
q3 = StringVar()

# Frames
frame_title = Frame(window)
frame_title.pack(side=TOP)
frame_questions = Frame(window)
frame_questions.pack(side=TOP, anchor=W)

# Labels
label_title = Label(frame_title,
                    text='QUIZ',
                    font=('Hack', 30))
label_title.pack()

# Questions
rounds = 0
correct_answers_count = 0
user_answers = []
correct_answers = []

for key in questions:
    # Q1

    label_question1 = Label(frame_questions,
                            text=key,
                            font=('Hack', 15))
    label_question1.pack(anchor=W)
    for i in options[rounds]:
        answers1 = Radiobutton(frame_questions,
                               text=i,
                               variable=var[rounds],
                               value=i)
        answers1.pack(anchor=W)
    rounds += 1
    submitButton_q1 = Button(frame_questions,
                             text='Submit',
                             font=('Hack', 10),
                             command=review_q1)
    submitButton_q1.pack(anchor=W)
    score_q1 = Label(frame_questions,
                     text='score',
                     font=('Hack', 15))
    score_q1.pack(anchor=W)

# Q2

window.mainloop()
