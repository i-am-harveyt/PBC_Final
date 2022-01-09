import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime


class AddPerson(object):
    def get_add_value(self):
        self.new_window.wait_window()
        if self.apply:
            ret = (self.add_name.get(),
                   self.add_sex.get(),
                   self.add_birth.get(),
                   self.add_death.get())
            return ret
        return None

    def click_apply(self, event=None):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window):
        def switch_death_year_value(event):
            self.all_values_death = self.all_values_death[
                self.all_values.index(self.add_birth.get()):
            ]
            death_year.config(values=self.all_values_death)

        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Add Person")
        self.new_window.geometry("250x125")
        self.new_window.resizable(0, 0)

        toplevel_offsetx, toplevel_offsety = window.winfo_x(), window.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.new_window.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        self.add_name = tk.StringVar()
        name_label = tk.Label(self.new_window, text="Name: ")
        name_label.grid(column=0, row=1, sticky="W")
        name_input = tk.Entry(
            self.new_window,
            textvariable=self.add_name,
            width=15, borderwidth=1
        )
        name_input.focus()
        name_input.grid(column=1, row=1, sticky="W")

        self.add_sex = tk.StringVar()
        sex_label = tk.Label(self.new_window, text="Sex: ")
        sex_label.grid(column=0, row=2, sticky="W")
        sex_select = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_sex,
            state="readonly",
            values=["Male", "Female"]
        )
        sex_select.current(0)
        sex_select.grid(column=1, row=2, sticky="W")

        self.all_values = [
            str(x) for x in range(
                int(datetime.today().year) + 1 - 100,
                int(datetime.today().year) + 1
            )
        ]
        self.all_values.append("None")
        self.all_values_len = 101

        self.add_birth = tk.StringVar()
        birth_label = tk.Label(self.new_window, text="Birth: ")
        birth_label.grid(column=0, row=3, sticky="W")
        self.birth_year = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_birth,
            state='readonly',
            values=self.all_values
        )
        self.birth_year.current(self.all_values_len - 1)
        self.birth_year.bind("<<ComboboxSelected>>", switch_death_year_value)
        self.birth_year.grid(column=1, row=3, sticky="W")

        self.all_values_death = [
            str(x) for x in range(
                int(datetime.today().year) + 1 - 100,
                int(datetime.today().year) + 1
            )
        ]
        self.all_values_death.append("None")
        self.all_values_death_len = 101

        self.add_death = tk.StringVar()
        death_label = tk.Label(self.new_window, text="Death: ")
        death_label.grid(column=0, row=4, sticky="W")
        death_year = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_death,
            state='readonly',
            values=self.all_values_death
        )
        death_year.current(self.all_values_len - 1)
        death_year.grid(column=1, row=4, sticky="W")

        cancel_button = tk.Button(
            self.new_window, text="Cancel",
            width=5, command=self.new_window.destroy
        )
        cancel_button.grid(column=0, row=5)

        self.new_window.bind("<Return>", self.click_apply)

        apply_button = tk.Button(
            self.new_window, text="Apply",
            width=5,
            command=self.click_apply
        )
        apply_button.grid(column=1, row=5)
