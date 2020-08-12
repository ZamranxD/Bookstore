from tkinter import *

window = Tk()
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






window.mainloop()

