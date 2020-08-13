from tkinter import *
import backend

#adding wrapper-functions to connect the front-end to the backend
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, ( title_text.get(), author_text.get(), year_text.get(), isbn_text.get() ))


def get_selected_row(event):
    global selected_tuple #making this global to access it later in the delete function
    index = list1.curselection()[0] #curselection returns a tuple with the index value so we put [0] to get only the first index in the tuple
    selected_tuple = list1.get(index) #this selects the whole row which user clicks on via its index
    #filling the entry boxes with selected values
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def close_command():
    window.destroy()


window = Tk()
window.wm_title("BookStore")
# creating labels for the text boxes
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)
label1 = Label(window, text="Author")
label1.grid(row=0, column=2)
label1 = Label(window, text="Year")
label1.grid(row=1, column=0)
label1 = Label(window, text="ISBN")
label1.grid(row=1, column=2)

#creating text boxes corresponding to the labels in a grid layout
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)
author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)
year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)


#making a listbox/textarea which'll list out the desired output
list1= Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
#making a scrollbar for the listbox above
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)
#now configuring the two together
list1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list1.yview) #here yview means a horizontal scrollbar
#binding a function to click event to select the row user clicks on
list1.bind('<<ListboxSelect>>', get_selected_row)



#adding some buttons for app functionality
button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)
button2 = Button(window, text="Search Entry", width=12, command=search_command)
button2.grid(row=3, column=3)
button3 = Button(window, text="Add Entry", width=12, command=add_command)
button3.grid(row=4, column=3)
button4 = Button(window, text="Update Selected", width=12, command=update_command)
button4.grid(row=5, column=3)
button5 = Button(window, text="Delete Selected", width=12, command = delete_command)
button5.grid(row=6, column=3)
button6 = Button(window, text="Close", width=12, command=close_command)
button6.grid(row=7, column=3)






window.mainloop()

