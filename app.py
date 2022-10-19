# a want to create an app for parents
import datetime
from logging import info
from tkinter import *
from numpy import save
import datetime as dt
from datetime import date
import calendar


def save_info():
    first_name_info = first_name_box.get()
    last_name_info = last_name_box.get()
    grup_name_info = group_name_box.get()
    #current_date_info = date.today()

    # open a text to save the data
    file = open('user.txt', 'w')
    file.write(first_name_info.upper())
    file.write(last_name_info.upper())
    file.write(grup_name_info.upper())
    #file.write(current_date_info)
    file.close()

    # clear the form
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    group_name_box.delete(0, END)
    #current_date_box.delete(0, END)

# create the app window


window = Tk()
window.geometry('500x500')
window.title('My first app')
head = Label(text='Formular masă Grădinița Paradisul copiilor', bg='#B0E0E6', fg='#0000FF', width=200, height=3)
head.pack()


# create labels
first_name = Label(text='Nume copil')
first_name.place(x=15, y=60)
last_name = Label(text='Prenume copil')
last_name.place(x=15, y=120)
grup_name = Label(text='Grupa')
grup_name.place(x=15, y=180)
# current_date = Label(text='Data ')
# current_date.place(x=5, y=240)

# create boxes for the answer
first_name_box = StringVar()
first_name_box = Entry(textvariable=first_name, width=25)
first_name_box.place(x=100, y=60)
last_name_box = StringVar()
last_name_box = Entry(textvariable=last_name, width=25)
last_name_box.place(x=100, y=120)
group_name_box = StringVar()
group_name_box = Entry(textvariable=grup_name, width=15)
group_name_box.place(x=100, y=180)
#current_date_box = Button(text='Data ', width=30, command=date.today())
# current_date_box = Entry(textvariable=current_date)
#current_date_box.place(x=100, y=240)

# create submit button
submit = Button(text='Trimite', width=10, command=save_info)
submit.place(x=0, y=300)

window.mainloop()


# i want to add the calendar, but so far i got a box to put the date in it