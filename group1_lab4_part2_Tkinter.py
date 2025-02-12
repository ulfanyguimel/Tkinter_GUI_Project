import tkinter as tk
from tkinter import ttk, messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centennial College - ICET Student Survey Form")
        self.geometry("600x500")  # Adjusted for spacing and alignment
        self.resizable(False, False)
        self.configure(bg="#ffffff")  # White background for a clean look

        # Apply Theme
        style = ttk.Style()
        style.theme_use("clam")  # Modern look
        style.configure("TLabel", font=("Poppins", 12), background="#ffffff")  
        style.configure("TButton", font=("Poppins", 11, "bold"), padding=6)
        style.configure("TFrame", background="#ffffff")
        style.map("TButton", background=[("active", "#e0e0e0")])  # Subtle hover effect

        self.widgets()
        self.reset_form()

    def widgets(self):
        # Title Label
        title_label = ttk.Label(self, text="ICET Student Survey", font=("Poppins", 18, "bold"))
        title_label.pack(pady=15)

        # Main Frame (Structured Look)
        frame = ttk.Frame(self, padding=20, relief="ridge", borderwidth=2)
        frame.pack(fill="none", expand=False, padx=20, pady=10)

        # Labels & Entry Fields
        ttk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = ttk.Entry(frame, width=40)
        self.name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        ttk.Label(frame, text="Residency:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.residency_var = tk.StringVar()
        ttk.Radiobutton(frame, text="Domestic", variable=self.residency_var, value="dom").grid(row=1, column=1, sticky="w")
        ttk.Radiobutton(frame, text="International", variable=self.residency_var, value="intl").grid(row=1, column=2, sticky="w")

        ttk.Label(frame, text="Program:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.program_var = tk.StringVar()
        self.program_combobox = ttk.Combobox(frame, textvariable=self.program_var, state="readonly",
                                             values=["Health","AI", "Programming", "Data Warehousing", "Software Development Project", 
                                                     "Employment Skills", "Web Development", "Networking", "Database", 
                                                     "Business Analysis", "Mobile Development", "Game Development", "Cybersecurity"])
        self.program_combobox.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        # Courses Section
        ttk.Label(frame, text="Courses:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.course_vars = {
            "Programming I": tk.StringVar(),
            "Web Page Design": tk.StringVar(),
            "Software Engineering": tk.StringVar()
        }

        ttk.Checkbutton(frame, text="Programming I", variable=self.course_vars["Programming I"], onvalue="COMP100", offvalue="").grid(row=3, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Web Page Design", variable=self.course_vars["Web Page Design"], onvalue="COMP213", offvalue="").grid(row=4, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Software Engineering", variable=self.course_vars["Software Engineering"], onvalue="COMP120", offvalue="").grid(row=5, column=1, sticky="w")

        # Button Frame (Aligned and Centered)
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=15)

        ttk.Button(button_frame, text="Reset", command=self.reset_form, width=16).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Submit", command=self.show_message, width=16).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.quit, width=16).grid(row=0, column=2, padx=5)

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Ulfany Furcal")
        self.residency_var.set("dom")
        self.program_var.set("Health")
        for var in self.course_vars.values():
            var.set("")

    def show_message(self):
        name = self.name_entry.get()
        residency = self.residency_var.get()
        program = self.program_var.get()
        courses = [var.get() for key, var in self.course_vars.items() if var.get()]
        
        messagebox.showinfo("Information", f"Name: {name}\nProgram: {program}\nResidency: {residency}\nCourses: {', '.join(courses)}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()