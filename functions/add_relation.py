import tkinter as tk
import tkinter.ttk as ttk
import pygraphviz


# TODO the problem of married him/herself , and, the child's father/mother is same one
def add_relation(
        graph: pygraphviz.AGraph, relationship_dict,
        name1, name2, name3, relation_type):
    """
    Add the information of the logic of graphviz in README.md,
    the overlapping problem might couldn't be solved.
    """
    if relation_type[0] == "1":
        name1_married = name1 + "_married"
        name2_married = name2 + "_married"
        subgraph = graph.add_subgraph(rank="same")
        subgraph.add_node(name1_married, shape="point")
        subgraph.add_node(name2_married, shape="point")
        subgraph.add_edge(name1_married, name2_married, rank="same")
        graph.add_edge(name1, name1_married)
        graph.add_edge(name2, name2_married)
        relationship_dict[
            (name1_married, name2_married)] = [name1_married, name2_married]

    if relation_type[0] == "2" and name3 != "":
        if (name1 != "" and name2 != "") and \
                (name1 + "_married", name2 + "_married") in relationship_dict:
            left_node = relationship_dict[
                (name1 + "_married", name2 + "_married")][0]
            right_node = relationship_dict[
                (name1 + "_married", name2 + "_married")][1]
            name3_child = name3 + "_child"
            graph.remove_edge(left_node, right_node)
            subgraph = graph.add_subgraph(rank="same")
            subgraph.add_node(left_node, shape="point")
            subgraph.add_node(right_node, shape="point")
            subgraph.add_node(name3_child, shape="point")
            graph.add_edge(left_node, name3_child)
            graph.add_edge(name3_child, right_node)
            graph.add_edge(name3_child, name3)
            relationship_dict[
                (name1 + "_married", name2 + "_married")
            ] = [name3_child, right_node]

        elif name1 != "":
            graph.add_subgraph(name3)
            graph.add_edge(name1, name3)
            print(graph)

        elif name2 != "":
            graph.add_subgraph(name3)
            graph.add_edge(name2, name3)

    return graph, relationship_dict


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
        self.new_window.title("Add Relation")

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
