from tkinter import *# imports all modules and submodules from tkinter
from tkinter import messagebox

from jupyter_client.session import Message

#tkinter is pre-installed, so don't need to install

'''
text message box
dialogue box
dialogue box with text message box as output 
'''
#1. Text message box
ozWindow = Tk()
ozWindow.geometry("500x500")

oztext = Text(ozWindow, height=12, width=40, fg = 'red', selectbackground = 'blue')
#fg is the color used for text
# selectbackground is a parameter used for color of the text when it's selected;
# just adding fucntionality
oztext.pack()

#2. Dialogue box
ozdialogue = messagebox.showinfo('Dialogue', 'Dialogue box')



#3. Dialogue box with a text message as output
ozdialogue = messagebox.askyesno('Order', 'Would you like to order?')
if ozdialogue:
    answer = "Awesome!"
else:
    answer = "Oh no, come again!"
response = Message(ozWindow, text=answer)
response.pack()

ozWindow.mainloop()
# ************************* Practice from videos:
#1. Initialize gui window
ozmain = Tk() # root is a base window, initializes a blank window
ozmain.geometry("500x500") #calling geometry method with dimensions for the window to modify it's size.

#2 Creating a Label
# use any of the 7 defined widgets available in Tkinter
ozLabel = Label(ozmain, text="Text for the label\n Oleg is learning again! \n this is fun") # variable where label is stored; calling Label and specifiying
#that it's to be used in the 'ozmain' window, setting text for the label.
ozLabel.pack() #pack funciton places the Lebel element onto the window

#3 text box to show the menu
menu_output = Text(ozmain, height=15, width=50) # height and width specify dimensions
menu_output.pack() #pack is used to add to the window
#defining a menu dictionary that will be returned.
Menu = {"1. Full Stack Pasta" : 33.00,
        "2. Bit Burger": 31.00,
        "3. Pizza Byte": 30.50, "4. Hello Humus": 19.00, "5. RAM Cola": 6.00, "6. Java Juice": 8.50, "7. Syntax Cake": 14.00, "8. Anaconda Eclair": 16.00}
# defining a function here to return something:
def ourmenu():
    for item, price in Menu.items():  # my first for loop that just iterates over my dictionary pairs and prints them one by one. no magic here
        menu_output.insert(END,f"{item} : {price}")

    #3. Creating a Button
ozButton = Button(ozmain, text="Menu", command = ourmenu) # same as with the label,
# specifying window where the button will be placed.
#command is an attribute for the button that executes an action when button is clicked.
ozButton.pack(side=LEFT, fill='x', expand=True) # side, fill, and expand attributes
# used for the placement of the item. also padding

#placing objects side by side
ozButton2 = Button(ozmain, text="Order", command = '')
ozButton2.pack(side=LEFT, fill='x', expand=True)

ozmain.mainloop()#holds the view in place so the user can see it, and it's closed when user closes it
