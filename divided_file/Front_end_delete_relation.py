import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def delete_relation_succeed():
    messagebox.showinfo(title="Information", message="Delete relation Succeed!")


def delete_relation_click():
    pass


window = tk.Tk()

name1_label = tk.Label(window, text="Name1: ")
name1_label.grid(column=0, row=1, sticky="W")
name1_select = ttk.Combobox(window, width=10, state='readonly', values=[])
name1_select.grid(column=1, row=1, sticky="W")

name2_label = tk.Label(window, text="Name1: ")
name2_label.grid(column=0, row=2, sticky="W")
name2_select = ttk.Combobox(window, width=10, state='readonly', values=[])
name2_select.grid(column=1, row=2, sticky="W")

cancel_button = tk.Button(window, text="Cancel", width=5, command=window.destroy)
cancel_button.grid(column=0, row=3)
apply_button = tk.Button(window, text="Apply", width=5,
                         command=lambda: [delete_relation_click(), window.destroy()])
apply_button.grid(column=1, row=3)


window.mainloop()
