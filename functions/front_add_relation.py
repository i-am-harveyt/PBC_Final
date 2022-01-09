import tkinter as tk
import tkinter.ttk as ttk


class AddRelation(object):
    def get_add_value(self):
        self.new_window.wait_window()
        if self.apply:
            ret = (
                self.add_name1.get(),
                self.add_name2.get(),
                self.add_name3.get(),
                self.add_relation.get()
            )
            return ret
        return None

    def click_apply(self, event=None):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window, person_list):
        def update_name1_value(event):
            pass

        def update_name2_value(event):
            pass

        def update_name3_value(event):
            pass

        def switch_name3_status(event):
            if self.add_relation.get()[0] == "1":
                name1_label.config(text="Left: ")
                name2_label.config(text="Right: ")
                name3_label.config(text="Not usable")
                name3_select.config(state=tk.DISABLED)
            elif self.add_relation.get()[0] == "2":
                name1_label.config(text="Left: ")
                name2_label.config(text="Right: ")
                name3_label.config(text="Child: ")
                name3_select.config(state="readonly")
            else:
                name1_label.config(text="Left: ")
                name2_label.config(text="Right: ")
                name3_label.config(text="Not usable")
                name3_select.config(state=tk.DISABLED)

        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Add Relation")
        self.new_window.geometry("275x125")
        self.new_window.resizable(0, 0)

        toplevel_offsetx, toplevel_offsety = window.winfo_x(), window.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.new_window.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        self.add_relation = tk.StringVar()
        relation_label = tk.Label(self.new_window, text="Relation Type: ")
        relation_label.grid(column=0, row=1, sticky="W")
        relation_select = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_relation,
            state='readonly',
            values=["1. Couple", "2. Child", "3. Unmarried Couple"]
        )
        relation_select.current(0)
        relation_select.bind("<<ComboboxSelected>>", switch_name3_status)
        relation_select.grid(column=1, row=1, sticky="W")

        self.add_name1 = tk.StringVar()
        name1_label = tk.Label(self.new_window, text="Left: ")
        name1_label.grid(column=0, row=2, sticky="W")
        name1_select = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_name1,
            state='readonly',
            values=person_list
        )
        name1_select.grid(column=1, row=2, sticky="W")

        self.add_name2 = tk.StringVar()
        name2_label = tk.Label(self.new_window, text="Right: ")
        name2_label.grid(column=0, row=3, sticky="W")
        name2_select = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_name2,
            state='readonly',
            values=person_list
        )
        name2_select.grid(column=1, row=3, sticky="W")

        self.add_name3 = tk.StringVar()
        name3_label = tk.Label(self.new_window, text="Not usable: ")
        name3_label.grid(column=0, row=4, sticky="W")
        name3_select = ttk.Combobox(
            self.new_window, width=15,
            textvariable=self.add_name3,
            state='readonly',
            values=person_list
        )
        name3_select.config(state=tk.DISABLED)
        name3_select.grid(column=1, row=4, sticky="W")

        cancel_button = tk.Button(
            self.new_window, text="Cancel",
            width=5,
            command=self.new_window.destroy
        )
        cancel_button.grid(column=0, row=5)

        self.new_window.bind("<Return>", self.click_apply)

        apply_button = tk.Button(
            self.new_window, text="Apply", width=5,
            command=self.click_apply
        )

        apply_button.grid(column=1, row=5)
