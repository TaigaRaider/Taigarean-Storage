from tkinter import *

counter = 0

# push button function
# def consequences():
#     global counter
#     counter += 1
#     counter_message = f"You pushed the button {counter} times"
#     if int(counter) == 1:
#         counter_message = f"You pushed the button once"
#     else:
#         counter_message = counter_message
#     print(counter_message)


# backspace button function
def backspace():
    write.delete((len(write.get())-1),END)


# text delete button function
def delete():
    write.delete(0,END)


# text entry button function
def turn_in():
    work = write.get()
    print(f"user entered {work}")
    write.configure(state="disabled")


# window configuration
source = Tk()
source.geometry("250x200")
source.title("GUI")

# icon change
qr = PhotoImage(file='me.png')        #photo variable
source.iconphoto(True,qr)      #icon set function
source.configure(background='black')    #background colour function, .configure can be used to alter data in the GUI window

# entry boxes
write = Entry(source,
              font = ('Segoe',50),
              fg="blue",
              bg="black",
              show="*")     # computer will only display quoted text rather actual input in the entry box, use case: passwords
write.insert(0,"Write!!!")      # entry box placeholder
write.pack(side="left")     #align entry box to the side

# text entry button
turn_in_button = Button(source,
                 text="Turn in",
                 command= turn_in)
turn_in_button.pack(side="right")

# backspace button
backspace_button = Button(source,
                 text="Backspace",
                 command= backspace
                 )
backspace_button.pack(side="right")

# delete button
delete_button = Button(source,
                 text="Delete",
                 command= delete
                 )
delete_button.pack(side="right")

# buttons
# push = Button(source,
#               text='Push me',
#               command=consequences,     #writing the function name without the parenthesis is known as a callback, and callbacks are used in button command definition
#               font=('Segoe', 30),
#               foreground='white',
#               background='black',
#               activeforeground='white',
#               activebackground='black',
#               state='active',      #set to disabled to prevent the button from being used or set to active to enable button use
#               image=qr,
#               compound='top')
# push.pack()

# labels
# loading = PhotoImage(file='snp.png')

# label = Label(source,text=f"Hi Everyone",
#               font='Segoe',
#               foreground='white',
#               background='black',
#               relief='raised',
#               bd=2,
#               padx=7,
#               pady=4,
#               image=loading,
#               compound='bottom')

# label.pack()  #for centering the label on the x-axis with y-axis = 0
# label.place(x=5,y=5) is used to place the label in a desired location

source.mainloop() #display window on screen - listen for events