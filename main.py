import tkinter as tk
from tkinter import messagebox
from gui.widgets_demo import MyApp
from gui.registration_form import RegistrationApp
from gui.interest_calculator import InterestApp as InterestCalculator
from gui.interest_app import InterestApp as InterestAppAlt

# Function to launch the selected application
def launch_app(choice):
    if choice == "Widgets Demo":
        app = MyApp()
    elif choice == "Registration Form":
        app = RegistrationApp("Registration Form")
    elif choice == "Interest Calculator":
        app = InterestCalculator("Future Value Calculator")
    elif choice == "Alternative Interest App":
        app = InterestAppAlt("Alternative Interest Calculator")
    else:
        messagebox.showerror("Error", "Invalid selection!")
        return
    app.mainloop()

# Create the main window
root = tk.Tk()
root.title("Tkinter Project Launcher")
root.geometry("400x300")

# Label
tk.Label(root, text="Select an application to run:", font=("Arial", 12)).pack(pady=10)

# App selection dropdown
options = ["Widgets Demo", "Registration Form", "Interest Calculator", "Alternative Interest App"]
selected_option = tk.StringVar()
selected_option.set(options[0])
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)

# Run button
tk.Button(root, text="Launch", command=lambda: launch_app(selected_option.get())).pack(pady=10)

# Exit button
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()