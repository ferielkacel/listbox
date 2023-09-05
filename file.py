from tkinter import *

window = Tk()
listbox = Listbox(window,
                  fg="#900C3F",
                  bg="#FFFEFF",
                  selectmode=MULTIPLE)


def submit():

    food = []

    for index in listbox.curselection(): #getbthe selected items
      food.insert(index,listbox.get(index)) #insert them into the list food
    print("You have ordered: ")
    for index in food: #desplays the food
        print(index)

def delete():

   for index in reversed(listbox.curselection()):
        listbox.delete(index)

listbox.config(height=listbox.size())


def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())


entryBox = Entry(window)
entryBox.pack()
frame = Frame(window)
frame.pack()
addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)
submitbtn= Button(text="submit button",
                 command=submit,)
submitbtn.pack()
deletebtn=Button(text="delete",command=delete)
deletebtn.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"hamburger")
listbox.insert(3,"sandwich")
listbox.insert(4,"chawerma plate")
listbox.insert(5,"rechta")
listbox.insert(6,"hommus")

listbox.pack()
window.mainloop()
