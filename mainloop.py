import tkinter as tk
from tkinter import messagebox
from gui.registration_form import RegistrationApp
from gui.widgets_demo import MyApp
from gui.interest_app import InterestApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Project Launcher")
        self.geometry("500x400")

        # Dropdown menu for selecting an application
        self.options = ["Registration Form", "Widgets Demo", "Interest Calculator"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])  # Default selection
        tk.Label(self, text="Select an application to run:", font=("Arial", 12)).pack(pady=10)
        tk.OptionMenu(self, self.selected_option, *self.options).pack(pady=10)

        # Launch button
        tk.Button(self, text="Launch", command=self.launch_app).pack(pady=10)

        # Exit button
        tk.Button(self, text="Exit", command=self.quit).pack(pady=10)

        # Frame to embed the selected GUI
        self.app_frame = tk.Frame(self)
        self.app_frame.pack(fill="both", expand=True)

    def launch_app(self):
        """Switches between different GUI applications within the same window."""
        for widget in self.app_frame.winfo_children():
            widget.destroy()  # Remove previous UI

        selected = self.selected_option.get()
        if selected == "Registration Form":
            app = RegistrationApp("Registration Form")
        elif selected == "Widgets Demo":
            app = MyApp()
        elif selected == "Interest Calculator":
            app = InterestApp("Future Value Calculator")
        else:
            messagebox.showerror("Error", "Invalid selection!")
            return

        # Embed the selected app inside the main frame
        app.master = self.app_frame
        app.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()