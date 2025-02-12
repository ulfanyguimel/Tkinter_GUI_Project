import tkinter as tk
from tkinter import ttk, messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centennial College - ICET Student Survey Form")
        self.geometry("400x300")
        self.resizable(True, True)
        
        self.widgets()
        self.reset_form()  #Set default values on initializiation

    def widgets(self):
        title_label = ttk.Label(self, text="ICET Student Survey", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
 
        frame = ttk.Frame(self, padding=10, relief="ridge")
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Labels
        ttk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Residency:").grid(row=1, column=0, sticky="w")
        self.residency_var = tk.StringVar()
        ttk.Radiobutton(frame, text="Domestic", variable=self.residency_var, value="dom").grid(row=1, column=1, sticky="w")
        ttk.Radiobutton(frame, text="International", variable=self.residency_var, value="intl").grid(row=1, column=2, sticky="w")
        
        ttk.Label(frame, text="Program:").grid(row=2, column=0, sticky="w")
        self.program_var = tk.StringVar()
        self.program_combobox = ttk.Combobox(frame, textvariable=self.program_var, values=["AI", "Programming", "Data Warehousing", "Software Development Project", "Employment Skills", "Web Development", "Networking", "Database", "Business Analysis", "Mobile Development", "Game Development", "Cybersecurity"])
        self.program_combobox.grid(row=2, column=1)

        ttk.Label(frame, text="Courses:").grid(row=3, column=0, sticky="w")
        self.course_vars = {
            "Programming I": tk.StringVar(),
            "Web Page Design": tk.StringVar(),
            "Software Engineering": tk.StringVar()
        }
        
        ttk.Checkbutton(frame, text="Programming I", variable=self.course_vars["Programming I"], onvalue="COMP100", offvalue="").grid(row=3, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Web Page Design", variable=self.course_vars["Web Page Design"], onvalue="COMP213", offvalue="").grid(row=4, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Software Engineering", variable=self.course_vars["Software Engineering"], onvalue="COMP120", offvalue="").grid(row=5, column=1, sticky="w")
        
        # Buttons
        ttk.Button(frame, text="Reset", command=self.reset_form).grid(row=6, column=0, pady=5)
        ttk.Button(frame, text="OK", command=self.show_message).grid(row=6, column=1, pady=5)
        ttk.Button(frame, text="Exit", command=self.quit).grid(row=6, column=2, pady=5)
    
    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Ulfany Furcal")
        self.residency_var.set("dom")
        self.program_var.set("AI")
        for var in self.course_vars.values():
            var.set("")
    
    def show_message(self):
        name = self.name_entry.get()
        residency = self.residency_var.get()
        program = self.program_var.get()
        courses = [var.get() for key, var in self.course_vars.items() if var.get()]
        
        messagebox.showinfo("Form Submission", f" {name}\n {program}\n {residency}\n {', '.join(courses)}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
