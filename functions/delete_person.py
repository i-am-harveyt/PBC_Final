import tkinter as tk
import tkinter.ttk as ttk
import pygraphviz
# from delete_relation import delete_relation


# TODO If delete a person that is married, the _married node of the spouse will not be removed
def delete_person(graph: pygraphviz.AGraph, person_list: list, name):
    for node in graph.nodes():
        if name in node:
            graph.remove_node(node)
    person_list.remove(name)
    return graph, person_list


class DeletePerson(object):
    def get_del_value(self):
        self.new_window.wait_window()
        if self.apply:
            ret = self.del_name.get()
            return ret
        return None

    def click_apply(self):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window, person_list):
        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Delete Person")

        toplevel_offsetx, toplevel_offsety = window.winfo_x(), window.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.new_window.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        name_label = tk.Label(self.new_window, text="Name: ")
        name_label.grid(column=0, row=1, sticky="W")

        self.del_name = tk.StringVar()
        name_select = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.del_name,
            state='readonly',
            values=person_list
        )
        name_select.grid(column=1, row=1, sticky="W")

        cancel_button = tk.Button(
            self.new_window, text="Cancel",
            width=5,
            command=self.new_window.destroy
        )
        cancel_button.grid(column=0, row=2)

        apply_button = tk.Button(
            self.new_window, text="Apply", width=5,
            command=self.click_apply
        )
        apply_button.grid(column=1, row=2)
