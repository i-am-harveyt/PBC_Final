import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def add_relation_click():
    pass


def add_relation_succeed():
    messagebox.showinfo(title="Information", message="Add relation Succeed!")


window = tk.Tk()

name1_label = tk.Label(window, text="Name1: ")
name1_label.grid(column=0, row=1, sticky="W")
name1_select = ttk.Combobox(window, width=10, state='readonly', values=[])
name1_select.grid(column=1, row=1, sticky="W")

name2_label = tk.Label(window, text="Name2: ")
name2_label.grid(column=0, row=2, sticky="W")
name2_select = ttk.Combobox(window, width=10, state='readonly', values=[])
name2_select.grid(column=1, row=2, sticky="W")

relation_label = tk.Label(window, text="Relation Type: ")
relation_label.grid(column=0, row=3, sticky="W")
relation_select = ttk.Combobox(window, width=10, state='readonly', values=[
    "1. Couples",
    "2. Child",
    "3. Others"
])
relation_select.grid(column=1, row=3, sticky="W")


def condition_toggle():
    if relation_select.current() == 1:
        born_parent_label = tk.Label(window, text="Father/Mother is: ")
        born_parent_label.grid(column=0, row=4, sticky="W")
        born_parent_selection = ttk.Combobox(window, width=10, state="readonly")
        born_parent_selection.grid(column=1, row=4, sticky="W")


cancel_button = tk.Button(window, text="Cancel", width=5, command=window.destroy)
cancel_button.grid(column=0, row=5)
apply_button = tk.Button(window, text="Apply", width=5,
                         command=lambda: [add_relation_click(), window.destroy()])


apply_button.grid(column=1, row=5)
window.after(100, condition_toggle)
window.mainloop()
