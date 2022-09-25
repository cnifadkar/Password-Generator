from tkinter import *
from random import randint

#initializing tkinter 
root = Tk()
root.title('Strong Password Generator')

myPassword = chr(randint(33, 126))

def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(myEntry.get())
    myPassword = ''
    for x in range(pw_length):
        myPassword += chr(randint(33, 126))
    pw_entry.insert(0, myPassword)    
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("Password Copied")
    pop.geometry("250x150")

    pop_label = Label(pop, text= "The password has been copied", fg = "black", font = ("Helvetica", 12))
    pop_label.pack(pady=10)

    my_frame = Frame(pop)
    my_frame.pack(pady=5)

    ok = Button(my_frame, text = "ok", command = lambda: choice("ok"))
    ok.grid(row = 0, column = 1)
def choice(option):
    pop.destroy()
    if (option == "ok"):
        my_label.config(text = "You copied the password")
def clearmy_label():
    my_label.config(text = "")
    
lf = LabelFrame(root, text="How many characters do you want your password to be?")
lf.pack(pady=30)

myEntry = Entry(lf, font=("Helvetica", 24))
myEntry.pack(pady=20, padx=20)

pw_entry = Entry(root, text = '', font = ("Helvetica", 24))
pw_entry.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)

myButton = Button(myFrame, text = "Generate Strong Password", command=lambda:[clearmy_label(), new_rand()])
myButton.grid(row=0, column = 0, padx = 10)

clip_button = Button(myFrame, text="Copy to Clipboard",command =lambda:[clipper(), clicker()])
clip_button.grid(row=0, column = 1, padx = 10)

my_label = Label(root, text= "")
my_label.pack(pady=20)


root.mainloop()
                 
                                          
