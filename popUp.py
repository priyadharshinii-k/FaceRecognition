import tkinter as tk
from tkinter import messagebox

def msgSucces():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transaction Status", "Amount has been sent successfully")
    root.mainloop()

def fail():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information", "Show your face in front of the camera")
    root.mainloop()

def msgFail():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transaction Status", "Face not recognized")
    root.mainloop()

def MultipleFace():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Transaction Status", "Multiple Faces Detected")
    root.mainloop()
