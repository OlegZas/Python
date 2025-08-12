from tkinter import *# importing all modules, but not submodules, from tkinter
from tkinter import messagebox # message box submodule has to be imported explicitly
#tkinter is pre-installed, so don't need to install


'''
text message box
dialogue box
dialogue box with text message box as output 
'''
#1. Text message box
ozWindow = Tk() # This is a root window; Tk is a class that creates main window; stored in the variable ozWidnow
ozWindow.geometry("500x500") ##calling geometry method with dimensions for the window to modify it's size.

oztext = Text(ozWindow, height=30, width=60, fg = 'red', selectbackground = 'blue')
#Text is a built-in widget in the tkinter; i am using it to create a text box;
#ozWindow just references the window where to pack my text box;
# height and width are dimensions for the textbox (parameters that take attributes - values).
#fg is the color parameter used for text
# selectbackground is a parameter used for color of the text when it's selected;
# just adding functionality
oztext.pack()#pack method is used to add widgets to the containers(windows)



#2. Dialogue box
ozdialogue = messagebox.showinfo('Exercise 8: Magic', 'Carlos Rodriguez is reading this.') #  imported messagebox submodule to use messagebox object
# showinfo method is builtin to the messagebox submodule. it shows a dialogue box with information that i will provide


#3. Dialogue box with a text message as output
ozdialogue = messagebox.askyesno('Order', 'Would you like to order?') # same as above, but here i am using askyesno method to return
# an output - in this case, text message
if ozdialogue: # conditional if/else statment to return different outputs based on user's choice
    answer = "Great!" #storing in an answer variable
else:
    answer = "Oh no, come again!"
response = Message(ozWindow, text=answer) # response is a vaiable where i will store the widget Message that will be
# opened in ozWidow and will show an answer based on Carlos' choice
response.pack() # same as above, adding widget to the window continaer

ozWindow.mainloop() #method that runs the applicaiton and lets users interact with it.
# and keep it open while user uses it (hence the loop).
