import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_greeting():
    """
    Persnonalized greeting GUI and error handling. 
    """
    name = name_entry.get().strip() #input 
    selected_language = language_var.get()

    # if the name is empty will prevent
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name now!")
        return

    # Dictionary mapping for the drop down opitons
    greetings = {
        "English": f"Hello, {name}! Rock and Roll?",
        "Spanish": f"¡Hola, {name}! calcetin.",
        "French": f"Bonjour, {name}! roasted duck and cotacombs?",
        "German": f"Hallo, {name}! techno night club?",
        "Japanese": f"Konnichiwa, {name} hiroshima."
    }

    greeting_message = greetings.get(selected_language, f"Hello, {name}!")# default just hello oleg

    result_label.config(text=greeting_message)

def clear_form():
    """
    Here will clear the greeting and reset. 
    """
    name_entry.delete(0, tk.END)
    result_label.config(text="")
    name_entry.focus() 


root = tk.Tk()
root.title("Oleg Zasukha")
root.geometry("400x600") 

try: # will add image and exception to handle if it's not in the same folder. 
    hello_img = tk.PhotoImage(file="hello.gif")
    img_label = tk.Label(root, image=hello_img)
    img_label.pack(pady=5)
except Exception as e:
    print(f"Image not found. Make sure 'hello.gif' is in the same folder. Error: {e}")


# 1. Title Label
title_label = tk.Label(root, text="Oleg's greeter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# 2. Name Input Frame
name_frame = tk.Frame(root)
name_frame.pack(pady=5)

name_label = tk.Label(name_frame, text="Enter your name:")
name_label.grid(row=0, column=0, padx=5)

name_entry = ttk.Entry(name_frame, width=22)
name_entry.grid(row=0, column=1, padx=5)

# 3. Language Selection Frame
lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

language_label = tk.Label(lang_frame, text="Select a language:")
language_label.grid(row=0, column=0, padx=5)

languages = [
    "English", 
    "Spanish", 
    "French", 
    "German", 
    "Japanese"
]
language_var = tk.StringVar(value=languages[0])

language_combo = ttk.Combobox(
    lang_frame, 
    textvariable=language_var, 
    values=languages, 
    state="readonly", 
    width=20
)
language_combo.grid(row=0, column=1, padx=5)

# 4. Button Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

greet_button = tk.Button(button_frame, text="Greet Me!", command=generate_greeting)
greet_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_form)
clear_button.grid(row=0, column=1, padx=10)

#result
result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=350)
result_label.pack(pady=10)


if __name__ == "__main__":
    name_entry.focus() 
    root.mainloop()