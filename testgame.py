# A re-creation of the standard Python Magic 8 Ball Program

from tkinter import *
import random
# Set up the main (top) window's settings
window = Tk()
window.minsize(300, 300)
window.title('Magic 8 Ball Game')
window.configure(bg='Grey')


path = 'C:/xxxx/xxxx.jpg'
import ImageTk, Image
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

answers = ["Yes, Most Definetely!",
           "The Chances Are High!",
           "Not Likely!",
           "The Odds Look Good!",
           "Is That Your Question?",
           "You Have To Wait And See!",
           "23% Chance!",
           "99.9% Success Rate!",
           "It looks good!",
           "Computer Says NO!",
           "Unable to Decide!"
           "Ask Again Later!",
           "Better Not Tell You Now!",
           "Cannot Predict Result!",
           "Concentrate & Ask Again!",
           "Dont Count On It!",
           "No Chance!",
           "Only Smarties Have The Answer!"]

# Write new function to print out random choice from above or display error if user doesn't enter text????????
def get_answer():
        msg = "ERROR: Your question must be in text format. Try again"
        i = userentry.get()
        y = i.isdigit()
        l = len(userentry.get())
        if y == True or 1 == 0:
             userentry.insert(0,(msg))
        else:
                x = random.choice(answers)
                userentry2.delete(0, END)   # Clear previous output
                userentry2.insert(0,str(x)) # Insert response

def give_ans():
    who=["Who"]  # Can include Who WIll and give future responses or Who DID and give past responses?
    what=["What"] # What IS and What HAPPENED
    where=["Where"] # Where WAS/DID HAPPEN and Where IS
    when=["When"] # When DID and When WILL
    how=["How"]
    why=["Why"]
    is_is=["Is"]
    
    try:
      question = userentry.get()
         if question in who:
             answer_who = ["It was Teresa", "No one ever did that", "The girl behind you", "L'Rania"
                          "Donald Trump", "He who must not be named", "You-Know-Who", "Gianfranco", "Your mom"] #add more here
             ans = random.choice(answer_who)
             userentry2.delete(0, END)
             userentry2.insert(0, str(ans))
         if question in what:
                        answer_what = ["She killed him", "It was an inside job", "It is pretty obvious isn't it",
                                       "It is a chemically-derived substance from petroleum", "Spain won the World Cup"] #add more here
                        ans = random.choice(answer_what)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
         if question in where:
                        answer_where = ["In your house", "Upstairs", "In this very room", "It is in Hawkins, Indiana",
                                        "It was found in C1362"] #add more here
                        ans = random.choice(answer_where)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
         if question in when:
                        answer_when = ["Tomorrow", "In the year of our Lord 1162", "In a few months time",
                                       "It already happened. Are you living under a rock or something?", "5..4..3..2..1..."] #add more here
                        ans = random.choice(answer_when)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
         if question in how:
                        answer_how = ["Through the vents", "By divine intervention", "Utter and complete mismanagement"
                                      "Because everyone is stupid", "I dont even know anymore"] #add more here
                        ans = random.choice(answer_how)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
         if question in why:
                        answer_why = ["Because I said so", "Because everyone is stupid", "Cuz your momma"] #add more here
                        ans = random.choice(answer_why)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
         if question in is_is:
                        answer_is = ["Duh", "Nah", "Yes", "Perchance", "A little bit", "YOU WISH"] #add more here
                        ans = random.choice(answer_is)
                        userentry2.delete(0, END)
                        userentry2.insert(0, str(ans))
    exceptValueError:\
        print("Congratulations, you asked a question I don't know the answer to.")


# Make the buttons and entry boxes
lb1 = Label(window, text='Enter Your Question', bg='Black', fg='Red', font='Helvetica')
lb2 = Label(window, text='Answer', bg='Black', fg='Red', font='Helvetic')
lb3 = Label(window, text='0\n-\n0', bg='Black', font='Black')

# These are the two buttons (quit and get-answer)
button1 = Button(window, text='What is the Answer', bg='darkBlue', fg='Red', font='Helvetica', command=get_answer)
button2 = Button(window, text='Exit', bg='Red', fg='Black', font='Helvetica', command=quit)

# This allows a string-variable to be added to the window
circleVar = StringVar()
userentry = Entry(window, textvariable=circleVar)

circleVar2 = StringVar()
userentry2 = Entry(window, bg='Black', fg='Red', font='freesansbold, 12')


# Pack everything into the window (in order)
lb1.pack()
userentry.pack()
button1.pack()
lb3.pack()
lb2.pack()
userentry2.pack()
button2.pack(side=BOTTOM)

window.mainloop()