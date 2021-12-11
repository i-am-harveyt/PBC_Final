import json
import pygraphviz


def graph_init():
    graph = pygraphviz.AGraph(
        encoding="UTF-8",
        directed=True,
        dpi=300
    )
    graph.edge_attr.update(
        len='2.0'
    )
    return graph


def set_graph_attribute(graph):
    """Set the attribute of the graph. For example, caption."""
    graph_name = input("Caption of the graph: ")
    graph.graph_attr["label"] = graph_name
    return graph


def read_existing_data():
    """Read existing data by get the path of existing data"""
    print("---Read Existing Data---\n")
    data_path = input("Path of existing data: ")
    with open(data_path + ".json", 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def draw_graph_from_existing_data(people_dict):
    graph = graph_init()
    graph = set_graph_attribute(graph)
    for key, node_list in zip(people_dict.key(), people_dict.value()["relations"]):
        if not graph.has_node(key):
            graph.add_node(key)
        for node, relation in node_list.items():
            if not graph.has_node(node):
                graph.has_node(node)
            if (not graph.has_edge(key, node)) and (not graph.has_node(node, key)):
                graph.add_edge(key, node, label=relation, dir="both")
    return graph


def new_person(graph, people_dict):
    """Init a new node, new a node and a dict_data"""
    print("---New Person---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name = input("\nName: ")
    graph.add_node(name)
    people_dict[name] = dict({'attribute': {}, 'relations': {}})
    return graph, people_dict


def check_person_attribute(people_dict):
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name = input("\nName: ")
    for key, value in people_dict[name]["attribute"].items():
        print(f"{key}: {value}")


def set_person_attribute(people_dict):
    """Set the attribute of the person, address to the dict"""
    print("---Set Person Attribute---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name = input("\nName: ")
    attr_name = input("The attribute you want to edit: ")
    attr_content = input("Content of the attribute: ")
    people_dict[name]['attribute'][attr_name] = attr_content
    return people_dict


def delete_person(graph, people_dict):
    """Remove an existing node, delete the dict"""
    print("---Delete Person---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name = input("\nName: ")
    graph.delete_node(name)
    del people_dict[name]
    return graph, people_dict


def set_relation(graph, people_dict):
    """Set the relation between two guys, create the edge between
       nodes, and update the data in dict(both two)."""
    print("---Set Relation---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name1 = input("\nName of the first person: ")
    name2 = input("Name of the second person: ")
    relation_type_num = input(
        "\nThe type of the relation: \n" +
        "1. Same rank\n"
        "2. Not same rank\n" +
        "What's the type(number)? "
    )
    relation_label = input("The label of relation: ")
    if relation_type_num == "1":
        graph.add_edge(name1, name2, label=relation_label, dir='none', rank='same', constraint=False)
    elif relation_type_num == "2":
        graph.add_edge(name1, name2, label=relation_label, dir='none', constraint=True)

    people_dict[name1]['relations'][name2] = relation_label
    people_dict[name2]['relations'][name1] = relation_label

    return graph, people_dict


def edit_relation(graph, people_dict):
    """Edit the relation between two people"""
    print("---Edit Relation---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name1 = input("\nName of the first person: ")
    name2 = input("Name of the second person: ")
    new_relation = input("New relation: ")
    if graph.has_edge(name1, name2):
        graph.remove_edge(name1, name2)
        graph.add_edge(name1, name2, label=new_relation, dir='both')
    elif graph.has_edge(name2, name1):
        graph.remove_edge(name2, name1)
        graph.add_edge(name2, name1, label=new_relation, dir='both')
    people_dict[name1]['relations'][name2] = new_relation
    people_dict[name2]['relations'][name1] = new_relation
    return graph, people_dict


def check_relation(graph, people_dict):
    """Check if there is an edge between two nodes"""
    print("---Check Relation---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name1 = input("\nName of the first person: ")
    name2 = input("Name of the second person: ")
    if graph.has_edge(name1, name2):
        return f"{name1}, {name2}: {people_dict[name1]['relations'][name2]}"
    elif graph.has_edge(name2, name1):
        return f"{name2}, {name1}: {people_dict[name2]['relations'][name1]}"
    return "Not Existed"


def delete_relation(graph, people_dict):
    """Remove the edge between two nodes"""
    print("---Delete Relation---\n")
    count = 1
    for person in people_dict:
        print(f"{count}. {person}")
        count += 1
    name1 = input("\nName of the first person: ")
    name2 = input("Name of the second person: ")
    if graph.has_edge(name1, name2):
        graph.remove_edge(name1, name2)
    elif graph.has_edge(name2, name1):
        graph.remove_edge(name2, name1)
    del people_dict[name1]['relations'][name2]
    del people_dict[name2]['relations'][name1]
    return graph, people_dict


def export_data(people_dict):
    """Exporting data as a json file"""
    print("---Export Data---\n")
    export_filename = input("Export filename: ")
    with open(export_filename + ".json", 'w', encoding="utf-8") as file:
        json.dump(people_dict, file, sort_keys=True, indent=4)


def export_graph(graph):
    """Output the graph, as <filename>.<datatype>"""
    print("---Get output---\n")
    graph.layout("dot")
    output_name = input("Output name: ")
    output_datatype = input("Output datatype: ")
    graph.draw(output_name + "." + output_datatype)
