import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def add_person_click():
    pass

def apply_succeed_popup():
    messagebox.showinfo(title="Information", message="Apply Succeed!")


window = tk.Tk()

name_label = tk.Label(window, text="Name: ")
name_label.grid(column=0, row=1, sticky="W")
name_input = tk.Entry(window, width=10, borderwidth=1)
name_input.grid(column=1, row=1, sticky="W")

birth_label = tk.Label(window, text="Birth: ")
birth_label.grid(column=0, row=2, sticky="W")
birth_year = ttk.Combobox(window, width=10, state='readonly', values=[str(x) for x in range(1920, 2021)])
birth_year.grid(column=1, row=2, sticky="W")

death_label = tk.Label(window, text="Death: ")
death_label.grid(column=0, row=3, sticky="W")
death_year = ttk.Combobox(window, width=10, state='readonly', values=[str(x) for x in range(1920, 2021)])
death_year.grid(column=1, row=3, sticky="W")

cancel_button = tk.Button(window, text="Cancel", width=5, command=window.destroy)
cancel_button.grid(column=0, row=4)
apply_button = tk.Button(window, text="Apply", width=5,
                         command=lambda: [apply_succeed_popup(), window.destroy()])
apply_button.grid(column=1, row=4)

window.mainloop()
