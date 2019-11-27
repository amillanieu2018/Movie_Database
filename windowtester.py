from tkinter import *
from PIL import ImageTk, Image
import random

window = Tk()
window.minsize(300, 300)
window.title('Magic 8 Ball Game')
window.configure(bg='White Smoke')
path = 'C:/Users/Alvaro/Desktop/magic-8-ball-png-3.png'
img=ImageTk.PhotoImage(Image.open(path))



def give_ans():
    who = ["Who"]  # Can include Who WIll and give future responses or Who DID and give past responses?
    what = ["What"]  # What IS and What HAPPENED
    where = ["Where"]  # Where WAS/DID HAPPEN and Where IS
    when = ["When"]  # When DID and When WILL
    how = ["How"]
    why = ["Why"]
    is_is = ["Is"]

    question = userentry.get()

    if question in who:
            answer_who = ["It was Teresa", "No one ever did that", "The girl behind you", "L'Rania","Donald Trump",
                          "He who must not be named", "You-Know-Who", "Gianfranco", "Your mom",
                          "You know I cant tell you", "I don't know"]  # add more here
            ans = random.choice(answer_who)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in what:
            answer_what = ["She killed him", "It was an inside job", "It is pretty obvious isn't it",
                           "It is a chemically-derived substance from petroleum", "Spain won the World Cup",
                           "Patience, soon you will see", "I can't predict this"]  # add more here
            ans = random.choice(answer_what)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in where:
            answer_where = ["In your house", "Upstairs", "In this very room", "It is in Hawkins, Indiana",
                            "It was found in C1362"]  # add more here
            ans = random.choice(answer_where)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in when:
            answer_when = ["Tomorrow", "In the year of our Lord 1162", "In a few months time",
                           "It already happened. Are you living under a rock or something?",
                           "5..4..3..2..1..."]  # add more here
            ans = random.choice(answer_when)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in how:
            answer_how = ["Through the vents", "By divine intervention", "Utter and complete mismanagement",
                          "Because everyone is stupid","I don't even know anymore","You're actually going to ask that?"]
                           # add more here
            ans = random.choice(answer_how)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in why:
            answer_why = ["Because I said so", "Because everyone is stupid", "Cuz your momma",
                          "It can't be revealed as of now","If you were smart you would know the answer"]
                          # add more here
            ans = random.choice(answer_why)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))

    elif question in is_is:
            answer_is = ["Duh", "Nah", "Yes", "Perchance", "A little bit", "YOU WISH", "Not really",
                         "Yes, most definitely", "Seems so"]  # add more here
            ans = random.choice(answer_is)
            userentry2.delete(0, END)
            userentry2.insert(0, str(ans))


# Make the buttons and entry boxes
lb1 = Label(window, text='Enter Your Question', bg='Grey', fg='Black', font='Helvetica')
lb2 = Label(window, text='Answer', bg='Grey', fg='Black', font='Helvetica')
lb3 = Label(window, text='Welcome to the Magic 8 Ball Game, ask away!', bg='White Smoke', font='Helvetica, 20')
#lb3 = Label(window, text='', bg='White', font='Black')
panel = Label(window, image = img)

# These are the two buttons (quit and get-answer)
button1 = Button(window, text='What is my answer', bg='Black', fg='Red', font='Helvetica', command=give_ans)
button2 = Button(window, text='Exit', bg='Red', fg='Black', font='Helvetica', command=quit)

# This allows a string-variable to be added to the window
circleVar = StringVar()
userentry = Entry(window, textvariable=circleVar)

circleVar2 = StringVar()
userentry2 = Entry(window, bg='Black', fg='Red', font='Helvetica, 12')

# Pack everything into the window (in order)
lb1.pack()
userentry.pack()
button1.pack()
lb3.pack()
lb2.pack()
userentry2.pack()
button2.pack(side=BOTTOM)
panel.pack()

window.mainloop()