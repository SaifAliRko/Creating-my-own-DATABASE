from tkinter import *
import backendwork


# to view anything in the listbox you need to insert it into the listbox



def get_selected_row(event):
    # declaring a global variable within a function, which will get the indices
    global selected_row
    # now we declare a variable which will get the indexes of our list
    # since we will select items based on their ids which is at 0 index so ....
    index = list.curselection()[0]  # to get id
    selected_row = list.get(index)   # to get all information of the selected row, ie date , exercise etc
    e1.delete(0,END)
    e1.insert(END,selected_row[1])   # 1 here for date as 0 is for index ie of no use
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backendwork.delete(selected_row[0]) # as selected row as all info so [0] is the id which we need for delete

def view_command():
    # emtpying the list as we will fill it
    list.delete(0,END)
    # inorder to view everyting in the database you need to call the view function created
    # and the other thing is to view everything in the list box , and only way is to insert every row into list
    for row in backendwork.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    # you got all rows from the search then you deploy for loop to insert all searched rows into empty table
    for row in backendwork.search(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
        list.insert(END,row)


# now as anything is entered into Entry we need to call the textvariable and get everything entered
# you will add data to both database and list as well
def add_command():
    backendwork.insert(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())

    # now remeber always whenever you update list you delete it uptill END and then from END you insert items
    # insert same into list
    list.delete(0,END)
    list.insert(END,(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()))

win = Tk()

win.wm_title('MY myDatabase DATABASE')

l1 = Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = Label(win, text='Earnings')
l2.grid(row=0,column=2)
l3 = Label(win, text='Exercise')
l3.grid(row=1,column=0)
l4 = Label(win, text='Study')
l4.grid(row=1,column=2)
l5 = Label(win, text='Diet')
l5.grid(row=2,column=0)
l6 = Label(win, text='Python')
l6.grid(row=2,column=2)

date_text = StringVar()
# to add the data into the text field next to label , we use entry
e1 = Entry(win, textvariable=date_text) # the things that user enters can be stored in a parameter as textvariable
e1.grid(row=0,column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable=earning_text)
e2.grid(row=0,column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1,column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2,column=1)

python_text = StringVar()
e6 = Entry(win, textvariable=python_text)
e6.grid(row=2,column=3)

list = Listbox(win,height=8,width=35)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)



#When a user changes the selection,
#a <<ListboxSelect>> virtual event is generated.
#You can bind to this to take any action you need.
list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2 = Button(win,text='Search',width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)

b4 = Button(win,text='View all',width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)

# .destroy to close the window opened
b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=7,column=3)

win.mainloop()
