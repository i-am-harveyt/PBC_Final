import pygraphviz
from datetime import datetime


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


def delete_person(graph: pygraphviz.AGraph, person_list, pattern):
    person_list.remove(pattern)
    for element in graph.nodes():
        if pattern == element \
                or pattern + "_son" in element \
                or pattern + "_married" in element:
            graph.remove_node(element)

    return graph, person_list
