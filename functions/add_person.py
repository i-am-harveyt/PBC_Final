import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
import pygraphviz


# TODO add focus to the Entry
def add_person(graph: pygraphviz.AGraph, person_list, name, sex, birth, death):
    if name not in person_list:
        person_list.append(name)
        if birth != "None":
            graph.add_node(
                name,
                label="X" if death != "None" else datetime.today().year - int(birth),
                xlabel=name + f"{death} died" if death != "None" else name,
                shape="square" if sex == "Male" else "circle",
                height=0.3,
                width=0.3
            )
        else:
            graph.add_node(
                name,
                label="X" if death != "None" else " ",
                xlabel=name + f"{death} died" if death != "None" else name,
                shape="square" if sex == "Male" else "circle",
                height=0.3,
                width=0.3
            )

    return graph, person_list


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

    def click_apply(self):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window):
        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Add Person")

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
            width=10, borderwidth=1
        )
        # name_input = tk.Entry(self.new_window, width=10, borderwidth=1)
        name_input.grid(column=1, row=1, sticky="W")

        self.add_sex = tk.StringVar()
        sex_label = tk.Label(self.new_window, text="Sex: ")
        sex_label.grid(column=0, row=2, sticky="W")
        sex_select = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_sex,
            state="readonly",
            values=["Male", "Female"]
        )
        sex_select.current(0)
        sex_select.grid(column=1, row=2, sticky="W")

        all_values = [
            str(x) for x in range(
                int(datetime.today().year) + 1 - 100,
                int(datetime.today().year) + 1
            )
        ]
        all_values.append("None")
        all_values_len = 101

        self.add_birth = tk.StringVar()
        birth_label = tk.Label(self.new_window, text="Birth: ")
        birth_label.grid(column=0, row=3, sticky="W")
        birth_year = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_birth,
            state='readonly',
            values=all_values
        )
        birth_year.current(all_values_len - 1)
        birth_year.grid(column=1, row=3, sticky="W")

        self.add_death = tk.StringVar()
        death_label = tk.Label(self.new_window, text="Death: ")
        death_label.grid(column=0, row=4, sticky="W")
        death_year = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_death,
            state='readonly',
            values=all_values
        )
        death_year.current(all_values_len - 1)
        death_year.grid(column=1, row=4, sticky="W")

        cancel_button = tk.Button(
            self.new_window, text="Cancel",
            width=5, command=self.new_window.destroy
        )
        cancel_button.grid(column=0, row=5)

        apply_button = tk.Button(
            self.new_window, text="Apply",
            width=5,
            command=self.click_apply
        )
        apply_button.grid(column=1, row=5)
