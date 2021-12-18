import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def delete_person_click():
    pass


def delete_person_succeed():
    messagebox.showinfo(title="Information", message="Delete Succeed!")


window = tk.Tk()

name_label = tk.Label(window, text="Name: ")
name_label.grid(column=0, row=1, sticky="W")

name_select = ttk.Combobox(window, width=10, state='readonly', values=[])
name_select.grid(column=1, row=1, sticky="W")

cancel_button = tk.Button(window, text="Cancel", width=5, command=window.destroy)
cancel_button.grid(column=0, row=2)
apply_button = tk.Button(window, text="Apply", width=5,
                         command=lambda: [delete_person_click(), window.destroy()])
apply_button.grid(column=1, row=2)


window.mainloop()
