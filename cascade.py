# 5.Write a program to cascade mul ple designed pages (at least three) with resizing tool, take some tools to input and output data.
import tkinter as tk
from tkinter import messagebox

# Page 1: Collects name and course information
class Page1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page Design 1")
        self.geometry("2560x1440")

        # Define colors
        self.c1 = "#A0A0DC"  # Light purple
        self.c2 = "#A0690A"  # Brown
        self.c3 = "#14A00A"  # Green

        # Create main panel (frame)
        panel = tk.Frame(self)
        panel.pack(fill="both", expand=True)

        # Panel 1: Enter your name
        p1 = tk.Frame(panel, bg=self.c1)
        p1.pack(fill="x")
        label1 = tk.Label(p1, text="Enter Your Name", font=("Verdana", 16), fg="green", bg=self.c1)
        label1.pack(padx=10, pady=10)
        self.tf1 = tk.Entry(p1, font=("Times New Roman", 14))
        self.tf1.pack(padx=10, pady=5)

        # Panel 2: Choose your course
        p2 = tk.Frame(panel, bg=self.c2)
        p2.pack(fill="x")
        label2 = tk.Label(p2, text="Choose Your Course", font=("Verdana", 16), fg="blue", bg=self.c2)
        label2.pack(padx=10, pady=10)
        self.cb1 = tk.StringVar()
        self.cb1.set("Select")  # Default value
        course_options = ["Select", "M. Tech", "MCA", "M.Sc"]
        course_menu = tk.OptionMenu(p2, self.cb1, *course_options)
        course_menu.config(width=15)
        course_menu.pack(padx=10, pady=5)

        # Panel 3: Button to go to Page 2
        p3 = tk.Frame(panel)
        p3.pack(fill="both", expand=True)
        self.button = tk.Button(p3, text="Next", bg="pink", relief="raised", command=self.on_button_click)
        self.button.pack(padx=10, pady=10)

    def on_button_click(self):
        # Get name and course
        name = self.tf1.get()
        course = self.cb1.get()

        # Validation
        if len(name) == 0:
            messagebox.showerror("Notification", "Please Write your Name")
            return
        if course == "Select":
            messagebox.showerror("Notification", "Please Select The Course")
            return

        # Proceed to Page 2 and pass the data (name, course)
        self.destroy()  # Close the current window
        Page2(name, course).mainloop()

# Page 2: Collects country and gender information
class Page2(tk.Tk):
    def __init__(self, name, course):
        super().__init__()
        self.title("Page Design 2")
        self.geometry("2560x1440")

        # Store name and course
        self.name = name
        self.course = course

        # Define colors
        self.c1 = "#A0A0DC"  # Light purple
        self.c2 = "#A0690A"  # Brown
        self.c3 = "#14A00A"  # Green

        # Create main panel (frame)
        panel = tk.Frame(self)
        panel.pack(fill="both", expand=True)

        # Panel 1: Display name and course from Page 1
        p1 = tk.Frame(panel, bg=self.c1)
        p1.pack(fill="x")
        label1 = tk.Label(p1, text=f"My Name is {self.name}", font=("Verdana", 16), fg="green", bg=self.c1)
        label1.pack(padx=10, pady=10)

        p2 = tk.Frame(panel, bg=self.c2)
        p2.pack(fill="x")
        label2 = tk.Label(p2, text=f"I am a Student of {self.course}", font=("Verdana", 16), fg="blue", bg=self.c2)
        label2.pack(padx=10, pady=10)

        # Panel 2: Enter country and choose gender
        p21 = tk.Frame(panel, bg=self.c3)
        p21.pack(fill="both", expand=True)
        
        # Enter country
        label21 = tk.Label(p21, text="Enter Country", font=("Verdana", 16), fg="green", bg=self.c3)
        label21.pack(padx=10, pady=10)
        self.tf1 = tk.Entry(p21, font=("Times New Roman", 14))
        self.tf1.pack(padx=10, pady=5)

        # Choose gender
        self.cb1 = tk.StringVar()
        self.cb1.set("Select")  # Default value
        gender_options = ["Select", "Male", "Female"]
        gender_menu = tk.OptionMenu(p21, self.cb1, *gender_options)
        gender_menu.config(width=15)
        gender_menu.pack(padx=10, pady=5)

        # Panel 3: Button to go to Page 3
        self.button = tk.Button(p21, text="Next", bg="pink", relief="raised", command=self.on_button_click)
        self.button.pack(padx=10, pady=10)

    def on_button_click(self):
        # Get country and gender
        country = self.tf1.get()
        gender = self.cb1.get()

        # Validation
        if len(country) == 0:
            messagebox.showerror("Notification", "Please Write your Country")
            return
        if gender == "Select":
            messagebox.showerror("Notification", "Please Select The Gender")
            return

        # Proceed to Page 3 and pass the data (country, gender)
        self.destroy()  # Close the current window
        Page3(country, gender).mainloop()

# Page 3: Display final message with country and gender
class Page3(tk.Tk):
    def __init__(self, country, gender):
        super().__init__()
        self.title("Page 3")
        self.geometry("2560x1440")

        # Define colors
        self.c3 = "#14A00A"  # Green

        # Create main panel (frame)
        panel = tk.Frame(self)
        panel.pack(fill="both", expand=True)

        # Panel 1: Display country
        p1 = tk.Frame(panel, bg=self.c3)
        p1.pack(fill="x")
        label1 = tk.Label(p1, text=f"Country is {country}", font=("Verdana", 16), fg="green", bg=self.c3)
        label1.pack(padx=10, pady=10)

        # Panel 2: Display gender
        p2 = tk.Frame(panel, bg=self.c3)
        p2.pack(fill="x")
        label2 = tk.Label(p2, text=f"Gender is {gender}", font=("Verdana", 16), fg="blue", bg=self.c3)
        label2.pack(padx=10, pady=10)

        # Panel 3: Thank you message
        p3 = tk.Frame(panel, bg=self.c3)
        p3.pack(fill="x")
        label3 = tk.Label(p3, text="Thank You", font=("Verdana", 20), fg="red", bg=self.c3)
        label3.pack(padx=10, pady=20)

if __name__ == "__main__":
    app = Page1()  # Start from Page1
    app.mainloop()
