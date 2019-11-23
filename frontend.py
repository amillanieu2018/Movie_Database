from tkinter import*
import backend

class Front (object):
    def __init__(self, window):
        self.window = window
        self.window.title("This is my Database project")
        self.myfont = ("Times New Roman", 18)
        self.yourfont = ("Times New Roman", 14)
        # need to create backend instance
        self.bk = backend.Back()
        # lets create widgets
        self.text_title = StringVar()
        self.lb1 = Label(master=self.window, text="Title", font=self.myfont)
        self.lb1.grid(row=0, column=0, sticky="w")

        self.text_year = StringVar()
        self.lb2 = Label(master=self.window, text="Year", font=self.myfont)
        self.lb2.grid(row=0, column=2, sticky="w")

        self.text_director = StringVar()
        self.lb3 = Label(master=self.window, text="Director", font=self.myfont)
        self.lb3.grid(row=1, column=0, sticky="w")

        self.text_lead = StringVar()
        self.lb4 = Label(master=self.window, text="Actor/Actress", font=self.myfont)
        self.lb4.grid(row=1, column=2, sticky="w")

        #entry text
        self.text_title = StringVar()
        self.et1 = Entry(master=self.window, textvariable = self.text_title, font=self.myfont)
        self.et1.grid(row=0, column=1)

        self.text_year = StringVar()
        self.et2 = Entry(master=self.window, textvariable=self.text_year, font=self.myfont)
        self.et2.grid(row=0, column=3)

        self.text_director = StringVar()
        self.et3 = Entry(master=self.window, textvariable=self.text_director, font=self.myfont)
        self.et3.grid(row=1, column=1)

        self.text_lead = StringVar()
        self.et4 = Entry(master=self.window, textvariable=self.text_lead, font=self.myfont)
        self.et4.grid(row=1, column=3)

        #main screen, list box is a bigger entry box
        self.listbox = Listbox(master=self.window, font=self.yourfont, height = 10, width = 80)
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2, padx=20, pady=40)

        # need to bind action for clicking in listbox
        self.listbox.bind("<<ListboxSelect>>", action=self.get_row)

        self.scroll = Scrollbar(master=self.window)
        self.scroll.grid(row=2, column=2, rowspan = 8, columnspan=1, sticky="nsw", pady=40)
        self.scroll.configure(command=self.listbox.yview)

        # the buttons
        self.bt1 = Button(master=self.window, width= 10, text="View All", font=self.myfont, command=self.view)
        self.bt1.grid(row=2, column=3)

        self.bt2 = Button(master=self.window,width= 10, text="Delete", font=self.myfont, command=self.view)
        self.bt2.grid(row=3, column=3)

        self.bt3 = Button(master=self.window, width= 10, text="Add", font=self.myfont, command=self.view)
        self.bt3.grid(row=4, column=3)

        self.bt4 = Button(master=self.window,width= 10, text="Search", font=self.myfont, command=self.view)
        self.bt4.grid(row=5, column=3)

        self.bt5 = Button(master=self.window,width= 10, text="Update", font=self.myfont, command=self.update)
        self.bt5.grid(row=6, column=3)

        self.bt6 = Button(master=self.window,width= 10, text="Close", font=self.myfont, command=self.close)
        self.bt6.grid(row=7, column=3)

    def get_row(self, action=None):
        # curselection returns list of all selected lines
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection() [0]
        idx = self.listbox.get(line_num) [0]
        title = self.listbox.get(line_num) [1]
        year = self.listbox.get(line_num) [2]
        director = self.listbox.get(line_num) [3]
        lead = self.listbox.get(line_num) [4]
        self.text_title.set(title)
        self.text_year.set(year)
        self.text_director.set(director)
        self.text_lead.set(lead)
        self.kept_index = self.listbox.get(line_num) [0]


    def view(self):
        data = self.bk.view_all()
        self.listbox.delete(0,END)
        for line in data:
            self.listbox.insert(END, line)

    def add(self):
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_director.get()
        lead = self.text_lead.get()
        self.bk.add_element(title, year, director, lead)
        self.view()

    def close(self):
        exit(1)

    def delete(self):
        # curselection returns list of all selected lines
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]

    def update(self):
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        title = self.listbox.get()
        year = self.listbox.get()
        director = self.listbox.get()
        lead = self.listbox.get()
        self.text_title.set(title)
        self.text_year.set(year)
        self.text_director.set(director)
        self.text_lead.set(lead)

window = Tk()
Front(window)
window.mainloop()