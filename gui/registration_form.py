from tkinter import *
from tkinter.ttk import *
import os

class RegistrationApp(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("500x400")

        # Check if the icon exists before setting it
        icon_path = os.path.join(os.path.dirname(__file__), "Internet.ico")
        if os.path.exists(icon_path):  
            self.iconbitmap(icon_path)

        sizer = Canvas(self, width=900, height=400)
        sizer.pack()

        container = Frame(self)
        container.place(
            relx=0.05,  ## Distance from left of parent
            rely=0.05,  # Distance from top of parent
            relwidth=0.9,  # Width relative to parent
            relheight=0.9  # Height relative to parent
        )

        self.create_styles()
        self.create_ui(container)

    def create_styles(self):
        style = Style()
        style.configure('TFrame', background='sky blue', padding=(2, 2, 6, 6))
        style.configure('TLabel', background='#ff80c1', padding=(2, 2, 4, 4))
        style.configure('TButton', background='gray', foreground='goldenrod', padding=(2, 2, 4, 4), ipadding=(5, 5, 5, 5))

    def create_ui(self, parent):
        # 1st frame
        frame = Frame(parent)
        frame.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.2)
        Label(frame, text='Registration Form', style='TLabel').pack(expand=True)

        # 2nd frame
        frame = Frame(parent)
        frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)
        # First column labels
        Label(frame, text='Name').place(relx=0, rely=0, relwidth=0.25, relheight=0.3)
        Label(frame, text='Program').place(relx=0, rely=0.33, relwidth=0.25, relheight=0.3)
        Label(frame, text='Course').place(relx=0, rely=0.66, relwidth=0.25, relheight=0.3)

        # Second column inputs
        Entry(frame).place(relx=0.25, rely=0, relwidth=0.5, relheight=0.3)
        Entry(frame).place(relx=0.25, rely=0.33, relwidth=0.5, relheight=0.3)
        Entry(frame).place(relx=0.25, rely=0.66, relwidth=0.5, relheight=0.3)
        
        # Third column labels
        Label(frame, text='Info').place(relx=0.75, rely=0, relwidth=0.25, relheight=0.3)
        Label(frame, text='Info').place(relx=0.75, rely=0.33, relwidth=0.25, relheight=0.3)
        Label(frame, text='Info').place(relx=0.75, rely=0.66, relwidth=0.25, relheight=0.3)
        
        # 3rd frame (Buttons)
        frame = Frame(parent)
        frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.2)
        Button(frame, text='Submit').place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)
        Button(frame, text='Exit', command=self.quit).place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.8)

if __name__ == "__main__":
    app = RegistrationApp('My Awesome GUI')
    app.mainloop()
