import pygraphviz
from Person import Person


def init_graph():
    graph = pygraphviz.AGraph(dpi=300)
    return graph


def set_graph_caption(graph):
    name = input("The label of graph: ")
    graph.graph_attr['label'] = name
    return graph


def new_node(graph):
    ret_lst = []
    person_name = input("Name: ")
    person_birth = int(input("Birth year(yyyy): "))
    person_death = input("Death year(yyyy, if not leave blank): ")
    graph.add_node(person_name)
    new_person = Person(person_name, person_birth, person_death)
    ret_lst.append(new_person)
    have_spouse = input("Is this person married?(y/n): ")
    if have_spouse == 'y':
        spouse_name = input("Name of Spouse: ")
        spouse_birth = int(input("Birth year(yyyy): "))
        spouse_death = input("Death year(yyyy, if not leave blank): ")
        graph.add_node(spouse_name)
        person_and_spouse = person_name+'&'+spouse_name
        new_person_spouse = Person(spouse_name, spouse_birth, spouse_death)
        ret_lst.append(new_person_spouse)
        graph.add_node(person_and_spouse)
        graph.edge(person_name, person_and_spouse)
        graph.edge(person_and_spouse, spouse_name)

    return graph, ret_lst


def edit_node_attr():
    pass


def delete_node():
    pass


def set_relation():
    pass


def edit_relation():
    pass


def delete_relation():
    pass
