import tkinter as tk
import tkinter.ttk as ttk


class DeletePerson(object):
    def get_del_value(self):
        self.new_window.wait_window()
        if self.apply:
            ret = self.del_name.get()
            return ret
        return None

    def click_apply(self, event=None):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window, person_list):
        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Delete Person")
        self.new_window.geometry("250x50")
        self.new_window.resizable(0, 0)

        toplevel_offsetx, toplevel_offsety = window.winfo_x(), window.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.new_window.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        name_label = tk.Label(self.new_window, text="Name: ")
        name_label.grid(column=0, row=1, sticky="W")

        self.del_name = tk.StringVar()
        name_select = ttk.Combobox(
            self.new_window, width=15,
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

        self.new_window.bind("<Return>", self.click_apply)

        apply_button = tk.Button(
            self.new_window, text="Apply", width=5,
            command=self.click_apply
        )
        apply_button.grid(column=1, row=2)
