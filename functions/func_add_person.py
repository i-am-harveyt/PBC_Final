import tkinter.messagebox
import tkinter.messagebox
from datetime import datetime
import pygraphviz


def add_person(graph: pygraphviz.AGraph, person_list, name, sex, birth, death):
    if name not in person_list:
        person_list.append(name)
        if birth != "None":
            graph.add_node(
                name,
                label="X" if death != "None" else datetime.today().year - int(birth),
                xlabel=name + f", {death} died" if death != "None" else name,
                shape="square" if sex == "Male" else "circle", fontname="Microsoft YaHei",
                height=0.2,
                width=0.2
            )
        else:
            graph.add_node(
                name,
                label="X" if death != "None" else " ",
                xlabel=name + f", {death} died" if death != "None" else name,
                shape="square" if sex == "Male" else "circle", fontname="Microsoft YaHei",
                height=0.2,
                width=0.2
            )
    else:
        tkinter.messagebox.showinfo(message="Name Existed")

    return graph, person_list
