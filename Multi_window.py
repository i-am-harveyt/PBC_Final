import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pygraphviz
from datetime import datetime
from PIL import Image, ImageTk
import functions
# from tkinter import messagebox


class Frame(object):
    def __init__(self):
        self.edited = False
        self.graph = pygraphviz.AGraph(dpi=200)
        self.graph.node_attr["fixedsize"] = True
        self.graph.node_attr["fontsize"] = "8"
        self.graph.layout("dot")
        self.graph.draw("Preview.png")
        self.graph_file = None
        self.graph_preview = None
        self.person_list = []

    def update_graph(self):
        self.graph.layout("dot")
        self.graph.draw("Preview.png")
        self.graph_file = ImageTk.PhotoImage(Image.open("Preview.png"))
        self.graph_preview.configure(image=self.graph_file)
        self.graph_preview.image = self.graph_file

    def main_frame(self, window):
        window.title("Main Page")
        self.graph_file = ImageTk.PhotoImage(Image.open("Preview.png"))
        self.graph_preview = tk.Label(image=self.graph_file)
        self.graph_preview.image = self.graph_file
        self.graph_preview.grid(row=0, column=0, columnspan=5)

        add_person_button = tk.Button(
            window, text="Add Person",
            command=lambda: [
                self.front_end_add_person()
            ])
        add_person_button.grid(row=1, column=0)

        delete_person_button = tk.Button(
            window, text="Delete Person",
            command=lambda: [
                self.front_end_delete_person()
            ])
        delete_person_button.grid(row=1, column=1)

        add_relation_button = tk.Button(
            window, text="Add Relation",
            command=lambda: [
                self.front_end_add_relation()
            ])
        add_relation_button.grid(row=1, column=2)

        delete_relation_button = tk.Button(
            window, text="Delete Relation",
            command=lambda: [
                self.front_end_delete_relation()
            ])
        delete_relation_button.grid(row=1, column=3)

        export_graph_button = tk.Button(
            window, text="Export Graph",
            command=self.export_graph
        )
        export_graph_button.grid(row=1, column=4)

    def front_end_add_person(self):
        def add_click():
            add_name = name_input.get()
            add_sex = sex_select.get()
            add_birth = birth_year.get()
            add_death = death_year.get()

            self.graph, self.person_list = functions.add_person(
                self.graph, self.person_list, add_name, add_sex, add_birth, add_death
            )

        new_window = tk.Toplevel(root)
        new_window.title("Add Person")

        name_label = tk.Label(new_window, text="Name: ")
        name_label.grid(column=0, row=1, sticky="W")
        name_input = tk.Entry(new_window, width=10, borderwidth=1)
        name_input.grid(column=1, row=1, sticky="W")

        sex_label = tk.Label(new_window, text="Sex: ")
        sex_label.grid(column=0, row=2, sticky="W")
        sex_select = ttk.Combobox(
            new_window, width=10,
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
        all_values_len = len(all_values)

        birth_label = tk.Label(new_window, text="Birth: ")
        birth_label.grid(column=0, row=3, sticky="W")
        birth_year = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=all_values
        )
        birth_year.current(all_values_len - 1)
        birth_year.grid(column=1, row=3, sticky="W")

        death_label = tk.Label(new_window, text="Death: ")
        death_label.grid(column=0, row=4, sticky="W")
        death_year = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=all_values
        )
        death_year.current(all_values_len - 1)
        death_year.grid(column=1, row=4, sticky="W")

        cancel_button = tk.Button(
            new_window, text="Cancel",
            width=5, command=new_window.destroy
        )
        cancel_button.grid(column=0, row=5)

        apply_button = tk.Button(
            new_window, text="Apply",
            width=5, command=lambda: [
                add_click(),
                self.update_graph(),
                new_window.destroy()
            ])
        apply_button.grid(column=1, row=5)

    def front_end_delete_person(self):
        def delete_click():
            pattern = name_select.get()
            self.graph, self.person_list = functions.delete_person(
                self.graph, self.person_list, pattern
            )

        new_window = tk.Toplevel(root)
        new_window.title("Delete Person")

        name_label = tk.Label(new_window, text="Name: ")
        name_label.grid(column=0, row=1, sticky="W")

        name_select = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=self.person_list
        )
        name_select.grid(column=1, row=1, sticky="W")

        cancel_button = tk.Button(
            new_window, text="Cancel",
            width=5,
            command=new_window.destroy
        )
        cancel_button.grid(column=0, row=2)

        apply_button = tk.Button(
            new_window, text="Apply", width=5,
            command=lambda: [
                delete_click(),
                self.update_graph(),
                new_window.destroy()
            ]
        )
        apply_button.grid(column=1, row=2)

    def front_end_add_relation(self):
        new_window = tk.Toplevel(root)
        new_window.title("Add Relation")

        name1_label = tk.Label(new_window, text="Name1: ")
        name1_label.grid(column=0, row=1, sticky="W")
        name1_select = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=self.graph.nodes()
        )
        name1_select.grid(column=1, row=1, sticky="W")

        name2_label = tk.Label(new_window, text="Name2: ")
        name2_label.grid(column=0, row=2, sticky="W")
        name2_select = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=self.graph.nodes()
        )
        name2_select.grid(column=1, row=2, sticky="W")

        relation_label = tk.Label(new_window, text="Relation Type: ")
        relation_label.grid(column=0, row=3, sticky="W")
        relation_select = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=["1. Couples", "2. Child", "3. Others"]
        )
        relation_select.grid(column=1, row=3, sticky="W")

        cancel_button = tk.Button(
            new_window, text="Cancel",
            width=5,
            command=new_window.destroy
        )
        cancel_button.grid(column=0, row=5)

        apply_button = tk.Button(
            new_window, text="Apply", width=5,
            command=lambda: [
                self.update_graph(),
                new_window.destroy()
            ])

        apply_button.grid(column=1, row=5)

    def front_end_delete_relation(self):
        new_window = tk.Toplevel(root)
        new_window.title("Delete Relation")

        name1_label = tk.Label(new_window, text="Name1: ")
        name1_label.grid(column=0, row=1, sticky="W")
        name1_select = ttk.Combobox(
            new_window, width=10, state='readonly',
            values=self.graph.nodes())
        name1_select.grid(column=1, row=1, sticky="W")

        name2_label = tk.Label(new_window, text="Name1: ")
        name2_label.grid(column=0, row=2, sticky="W")
        name2_select = ttk.Combobox(
            new_window, width=10,
            state='readonly',
            values=self.graph.nodes()
        )
        name2_select.grid(column=1, row=2, sticky="W")

        cancel_button = tk.Button(
            new_window, text="Cancel",
            width=5, command=new_window.destroy
        )
        cancel_button.grid(column=0, row=3)

        apply_button = tk.Button(
            new_window, text="Apply", width=5,
            command=lambda: [
                self.update_graph(),
                new_window.destroy()
            ])
        apply_button.grid(column=1, row=3)

    def export_graph(self):
        file_type = [
            ("JPG file", ".jpg"),
            ("PNG file", ".png")
        ]
        filename = filedialog.asksaveasfilename(filetypes=file_type)

        self.graph.layout("dot")
        self.graph.draw(filename)


if __name__ == "__main__":
    root = tk.Tk()
    app = Frame()
    app.main_frame(root)
    root.mainloop()
