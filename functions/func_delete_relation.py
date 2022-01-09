import tkinter.messagebox
import pygraphviz


def delete_relation(
        graph: pygraphviz.AGraph, person_list, relationship_dict,
        name1, name2, name3, relation_type):
    if relation_type[0] == "1":
        name1, name2 = name1.split(" ")
        if (name1 + "_married", name2 + "_married") in relationship_dict:
            while relationship_dict[(name1 + "_married", name2 + "_married")] != [name1 + "_married",
                                                                                  name2 + "_married"]:
                graph, person_list, relationship_dict = delete_relation(
                    graph, person_list, relationship_dict, name1, name2,
                    relationship_dict[(name1 + "_married", name2 + "_married")][0][:-6], "2"
                )
            graph.remove_node(name1 + "_married")
            graph.remove_node(name2 + "_married")
            del relationship_dict[(name1 + "_married", name2 + "_married")]

        elif (name1 + "nmarried", name2 + "nmarried") in relationship_dict:
            while relationship_dict[(name1 + "nmarried",
                                     name2 + "nmarried")] != [name1 + "nmarried", name2 + "nmarried"]:

                graph, person_list, relationship_dict = delete_relation(
                    graph, person_list, relationship_dict, name1, name2,
                    relationship_dict[(name1 + "nmarried", name2 + "nmarried")][0][:-6], "2"
                )
            graph.remove_edge(name1 + "nmarried", name2 + "nmarried")
            if len(graph.neighbors(name1 + "nmarried")) == 1:
                graph.remove_node(name1 + "nmarried")
            if len(graph.neighbors(name2 + "nmarried")) == 1:
                graph.remove_node(name2 + "nmarried")
            del relationship_dict[(name1 + "nmarried", name2 + "nmarried")]

    elif relation_type[0] == "2" and name3 != "":
        if name3 + "_child" in graph.nodes():
            neighbors = graph.neighbors(name3 + "_child")
            neighbors.remove(name3)
            if name1 != "" and name1 == name2:
                tkinter.messagebox.showerror(message="Parents cannot be the same person!")

            if name1 == name3 or name2 == name3:
                tkinter.messagebox.showerror(message="The person, of course, not his/her own parent!")

            elif (name1 + "_married", name2 + "_married") in relationship_dict:
                graph.add_edge(neighbors[1], neighbors[0])
                relationship_dict[(name1 + "_married", name2 + "_married")] = [neighbors[1], neighbors[0]]
                graph.remove_node(name3 + "_child")

            elif (name1 + "_unmarried", name2 + "_unmarried") in relationship_dict:
                graph.add_edge(neighbors[1], neighbors[0], style="dashed")
                relationship_dict[(name1 + "_unmarried", name2 + "_unmarried")] = [neighbors[1], neighbors[0]]
                graph.remove_node(name3 + "_child")

            elif (name1 + "nmarried", name2 + "nmarried") in relationship_dict:
                graph.add_edge(neighbors[1], neighbors[0], style="dashed")
                relationship_dict[(name1 + "nmarried", name2 + "nmarried")] = [neighbors[1], neighbors[0]]
                graph.remove_node(name3 + "_child")

            elif graph.has_edge(name1, name3):
                graph.remove_edge(name1, name3)

            elif graph.has_edge(name2, name3):
                graph.remove_edge(name2, name3)

            else:
                tkinter.messagebox.showerror(message="It seems like there's a problem with your input!")

        else:
            tkinter.messagebox.showerror(message="There is not a child relationship!")

    else:
        tkinter.messagebox.showerror("It seems like there's a problem with your input!")

    return graph, person_list, relationship_dict
