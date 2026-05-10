import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform

class OrderingKiosk:
    def __init__(self, root):
        self.root = root
        self.root.title("NicaAdventures: Sign-Up Kiosk")
        self.root.geometry("500x650")
        
        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        
        self.root.configure(bg="#2c3e50") 
        
        self.adventures = {
            "Volcano Boarding (Cerro Negro)": "Hike an active volcano and sled down ash at 50 mph!",
            "Surfing (San Juan del Sur)": "Catch world-class Pacific waves.",
            "Night Volcano Tour (Masaya)": "Look directly into a bubbling lake of real lava.",
            "Canyon Scrambling (Somoto)": "Swim and jump through a million-year-old canyon."
        }

        self.setup_ui()
        # Start the looping background music as soon as the app initializes
        self.play_background_music()

    def setup_ui(self):
        """Builds all the widgets for the application."""
        
        title = tk.Label(self.root, text="Nicaragua Adventures", font=("Arial", 20, "bold"), bg="#2c3e50", fg="#f1c40f")
        title.pack(pady=15)

        # --- Adjusted Image Size ---
        try:
            self.img = tk.PhotoImage(file="adventure.png") 
            # Increased subsample values (e.g., 4, 4 means 1/4th the original width and height)
            # Adjust these numbers if it's still too big or too small.
            self.img = self.img.subsample(4, 4) 
            img_label = tk.Label(self.root, image=self.img, bg="#2c3e50")
            img_label.pack(pady=5)
        except Exception:
            tk.Label(self.root, text="[Image 'adventure.png' not found]", bg="#2c3e50", fg="white").pack()

        name_frame = tk.Frame(self.root, bg="#2c3e50")
        name_frame.pack(pady=10)
        tk.Label(name_frame, text="Explorer Name:", font=("Arial", 12), bg="#2c3e50", fg="white").pack(side=tk.LEFT)
        self.name_entry = ttk.Entry(name_frame, width=25)
        self.name_entry.pack(side=tk.LEFT, padx=10)

        tk.Label(self.root, text="Select Your Adventure:", font=("Arial", 12), bg="#2c3e50", fg="white").pack(pady=(15, 0))
        self.activity_var = tk.StringVar()
        self.activity_combo = ttk.Combobox(self.root, textvariable=self.activity_var, state="readonly", width=35)
        self.activity_combo['values'] = list(self.adventures.keys()) 
        self.activity_combo.pack(pady=5)

        self.addon_var = tk.BooleanVar()
        self.addon_check = tk.Checkbutton(
            self.root, 
            text="Add VIP Round-Trip Transportation ($20)", 
            variable=self.addon_var,
            bg="#2c3e50", fg="white", selectcolor="#34495e", font=("Arial", 11)
        )
        self.addon_check.pack(pady=15)

        self.submit_btn = tk.Button(
            self.root, text="Book Adventure!", 
            font=("Arial", 14, "bold"), bg="#e67e22", fg="white", 
            command=self.submit_order 
        )
        self.submit_btn.pack(pady=10)

        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 12, "italic"), 
            bg="#2c3e50", fg="#2ecc71", wraplength=400, justify="center"
        )
        self.result_label.pack(pady=20)

    def play_background_music(self):
        """Plays a looping background track (Windows only)."""
        if platform.system() == "Windows":
            try:
                import winsound
                # SND_ASYNC allows the music to play without freezing the UI.
                # SND_LOOP makes it repeat continuously.
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            except Exception as e:
                print(f"Audio error: {e}")

    def submit_order(self):
        """Handles the logic when the submit button is clicked."""
        name = self.name_entry.get().strip()
        selected_activity = self.activity_var.get()

        if not name:
            messagebox.showerror("Missing Information", "Please enter your Explorer Name!")
            return
        
        if not selected_activity:
            messagebox.showerror("Missing Information", "Please select an adventure from the drop-down menu!")
            return

        info = self.adventures[selected_activity]
        transport = "Yes" if self.addon_var.get() else "No (Self-drive)"

        receipt = (
            f"🎉 Booking Confirmed, {name}! 🎉\n\n"
            f"Adventure: {selected_activity}\n"
            f"Details: {info}\n"
            f"VIP Transport: {transport}"
        )
        
        self.result_label.config(text=receipt)
        
        # Optional: You can trigger a different sound here, but it will interrupt the background loop
        # on Windows using winsound. 

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderingKiosk(root)
    root.mainloop()