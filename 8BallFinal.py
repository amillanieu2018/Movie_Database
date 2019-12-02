from tkinter import *
from PIL import ImageTk, Image
import random

window = Tk()
window.minsize(800, 800)
window.title('Magic 8 Ball Game')
window.configure(bg='White')
path = 'C:/Users/Alvaro/Desktop/magic-8-ball-png-3.png'
img = ImageTk.PhotoImage(Image.open(path))




def give_ans():
    answers = {}
    answers["who"] = ["It was Teresa", "No one ever did that", "The girl behind you", "L'Rania", "Donald Trump",
                      "He who must not be named", "You-Know-Who", "Gianfranco", "Your mom",
                      "You know I cant tell you", "I don't know"]
    answers["what"] = ["She killed him", "It was an inside job", "It is pretty obvious isn't it",
                       "It is a chemically-derived substance from petroleum", "Spain won the World Cup",
                       "Patience, soon you will see", "I can't predict this"]
    answers["where"] = ["In your house", "Upstairs", "In this very room", "It is in Hawkins, Indiana",
                        "It was found in C1362"]
    answers["when"] = ["Tomorrow", "In the year of our Lord 1162", "In a few months time",
                       "It already happened. Are you living under a rock or something?",
                       "5..4..3..2..1..."]
    answers["how"] = ["Through the vents", "By divine intervention", "Utter and complete mismanagement",
                      "Because everyone is stupid","I don't even know anymore","You're actually going to ask that?"]
    answers["why"] = ["Because I said so", "Because everyone is stupid", "Cuz your momma",
                      "It can't be revealed as of now","If you were smart you would know the answer"]
    answers["is"] = ["Duh", "Nah", "Yes", "Perchance", "A little bit", "YOU WISH", "Not really",
                     "Yes, most definitely", "Seems so"]

    question = userentry.get()
    print(question)

    for question_type in answers:
        print("test to see if we have a ", question_type, "question")
        if question_type in question.lower():
            print("yes")
            answer = random.choice(answers[question_type])
            print(answer)
            lb4 = Label(window, text=answer, bg='White', fg='Blue', font='Times, 20')
            lb4.pack()
            break
        else:
            print("no")



# Buttons and entry boxes
lb1 = Label(window, text='WELCOME TO THE MAGIC 8 BALL ', bg='White', font='Times 20 ')
lb2 = Label(window, text='YOUR WISH IS MY COMMAND...', bg='White', fg='Black', font='Times 15 ')
lb3 = Label(window, text='WHAT DO YOU WISH TO KNOW?', bg='Purple', fg='White', font='Times 15')

#lb3 = Label(window, text='', bg='White', font='Black')
panel = Label(window, image = img)


# 2 buttons (quit and get-answer)
button1 = Button(window, text='Ask', bg='Red', fg='Black', font='Helvetica', command=give_ans)
button2 = Button(window, text='Exit', bg='Red', fg='Red', font='Helvetica', command=quit)

# Allows a string-variable to be added to the window
circleVar = StringVar()
userentry = Entry(window, textvariable=circleVar)

circleVar2 = StringVar()
#userentry2 = Listbox(window, bg='Black', fg='Red', font='Helvetica, 12')


# Packs everything
lb1.pack()
lb3.pack()
userentry.pack()
button1.pack()
lb2.pack()
#userentry2.pack()
button2.pack(side=BOTTOM)
panel.pack()

window.mainloop()