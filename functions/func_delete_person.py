import tkinter.messagebox
import pygraphviz


def delete_person(graph: pygraphviz.AGraph, person_list: list, name):
    if name + "_child" in graph.neighbors(name):
        tkinter.messagebox.showerror(message="Please remove the \"Child\" relation first!")

    elif name + "_married" in graph.neighbors(name):
        tkinter.messagebox.showerror(message="Please remove the \"Couple\" relation first!")

    else:
        for node in graph.nodes():
            if name in node:
                graph.remove_node(node)
        person_list.remove(name)

    return graph, person_list
