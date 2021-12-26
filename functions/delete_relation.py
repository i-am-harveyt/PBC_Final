import tkinter as tk
import tkinter.ttk as ttk
import pygraphviz


def delete_relation(
        graph: pygraphviz.AGraph, person_list, relationship_dict, name1, name2, name3, relation_type):
    print(f"person list: {person_list}")
    print(f"relationship list: {relationship_dict}")
    print(name1, name2, name3, relation_type)
    print(f"nodes: {graph.nodes()}")
    print(f"edges: {graph.edges()}")
    if relation_type[0] == "1":
        while relationship_dict[(name1+"_married", name2+"_married")] != [name1+"_married", name2+"_married"]:
            graph, person_list, relationship_dict = delete_relation(
                graph, person_list, relationship_dict, name1, name2,
                relationship_dict[(name1+"_married", name2+"_married")][0][:-6], "2"
            )
        graph.remove_node(name1+"_married")
        graph.remove_node(name2+"_married")
        del relationship_dict[(name1+"_married", name2+"_married")]

    elif relation_type[0] == "2":
        neighbors = graph.neighbors(name3+"_child")
        print(f"neighbors: {neighbors}")
        neighbors.remove(name3)
        graph.add_edge(neighbors[1], neighbors[0])
        graph.remove_node(name3+"_child")
        if name3+"_child" in relationship_dict[(name1+"_married", name2+"_married")]:
            relationship_dict[(name1+"_married", name2+"_married")] = [neighbors[1], neighbors[0]]

    return graph, person_list, relationship_dict


class DeleteRelation(object):
    def get_delete_value(self):
        self.new_window.wait_window()
        ret = (
            self.add_name1.get(),
            self.add_name2.get(),
            self.add_name3.get(),
            self.add_relation.get()
               )
        return ret

    def click_apply(self):
        self.apply = True
        self.new_window.destroy()

    def __init__(self, window, person_list):
        def switch_name3_status(event):
            if self.add_relation.get()[0] == "1":
                name1_label.config(text="Husband: ")
                name2_label.config(text="Wife: ")
                name3_label.config(text="Not usable")
                name3_select.config(state=tk.DISABLED)
            elif self.add_relation.get()[0] == "2":
                name1_label.config(text="Father: ")
                name2_label.config(text="Mother: ")
                name3_label.config(text="Child: ")
                name3_select.config(state="readonly")
            else:
                name1_label.config(text="Name1: ")
                name2_label.config(text="Name2: ")
                name3_label.config(text="Not usable")
                name3_select.config(state=tk.DISABLED)

        self.apply = False
        self.new_window = tk.Toplevel(window)
        self.new_window.title("Delete Relation")

        toplevel_offsetx, toplevel_offsety = window.winfo_x(), window.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.new_window.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        self.add_relation = tk.StringVar()
        relation_label = tk.Label(self.new_window, text="Relation Type: ")
        relation_label.grid(column=0, row=1, sticky="W")
        relation_select = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_relation,
            state='readonly',
            values=["1. Couples", "2. Child", "3. Others"]
        )
        relation_select.current(0)
        relation_select.bind("<<ComboboxSelected>>", switch_name3_status)
        relation_select.grid(column=1, row=1, sticky="W")

        self.add_name1 = tk.StringVar()
        name1_label = tk.Label(self.new_window, text="Husband: ")
        name1_label.grid(column=0, row=2, sticky="W")
        name1_select = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_name1,
            state='readonly',
            values=person_list
        )
        name1_select.grid(column=1, row=2, sticky="W")

        self.add_name2 = tk.StringVar()
        name2_label = tk.Label(self.new_window, text="Wife: ")
        name2_label.grid(column=0, row=3, sticky="W")
        name2_select = ttk.Combobox(
            self.new_window, width=10,
            textvariable=self.add_name2,
            state='readonly',
            values=person_list
        )
        name2_select.grid(column=1, row=3, sticky="W")

        self.add_name3 = tk.StringVar()
        name3_label = tk.Label(self.new_window, text="Not usable: ")
        name3_label.grid(column=0, row=4, sticky="W")
        name3_select = ttk.Combobox(
            self.new_window, width=10,
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

        apply_button = tk.Button(
            self.new_window, text="Apply", width=5,
            command=self.click_apply
        )

        apply_button.grid(column=1, row=5)
