import tkinter.messagebox
import pygraphviz


def add_relation(
        graph: pygraphviz.AGraph, relationship_dict,
        name1, name2, name3, relation_type):
    if relation_type[0] == "1":
        if name1 != name2 and name1 and name2:
            name1_married = name1 + "_married"
            name2_married = name2 + "_married"
            if name1_married not in graph.nodes() and \
                    name2_married not in graph.nodes() and \
                    (name1 + "_unmarried", name2 + "_unmarried") not in relationship_dict and \
                    (name2 + "_unmarried", name1 + "_unmarried") not in relationship_dict:
                subgraph = graph.add_subgraph(rank="same")
                subgraph.add_node(name1_married, shape="point")
                subgraph.add_node(name2_married, shape="point")
                subgraph.add_edge(name1_married, name2_married, rank="same")
                graph.add_edge(name1, name1_married)
                graph.add_edge(name2, name2_married)
                relationship_dict[
                    (name1_married, name2_married)] = [name1_married, name2_married]
            else:
                tkinter.messagebox.showerror(message="Relationship existed or the person is in another relationship!")
        else:
            tkinter.messagebox.showerror(message="Wrong Input")

    elif relation_type[0] == "2" and name3 != "":
        if name1 == name3 or name2 == name3:
            tkinter.messagebox.showerror(message="The person cannot be his/her parent!")

        elif name1 != "" and name1 == name2:
            tkinter.messagebox.showerror(message="Two parents cannot be the same person!")

        elif (name1 != "" and name2 != "") and \
                (name1 + "_married", name2 + "_married") in relationship_dict:
            left_node = relationship_dict[
                (name1 + "_married", name2 + "_married")][0]
            right_node = relationship_dict[
                (name1 + "_married", name2 + "_married")][1]
            name3_child = name3 + "_child"
            if name3_child not in graph.nodes():
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
            else:
                tkinter.messagebox.showerror(message="Relationship existed!")

        elif name1 != "" and name2 != "" and \
                (name1 + "_unmarried", name2 + "_unmarried") in relationship_dict:
            left_node = relationship_dict[
                (name1 + "_unmarried", name2 + "_unmarried")][0]
            right_node = relationship_dict[
                (name1 + "_unmarried", name2 + "_unmarried")][1]
            name3_child = name3 + "_child"
            if name3_child not in graph.nodes():
                graph.remove_edge(left_node, right_node)
                subgraph = graph.add_subgraph(rank="same")
                subgraph.add_node(left_node, shape="point")
                subgraph.add_node(right_node, shape="point")
                subgraph.add_node(name3_child, shape="point")
                graph.add_edge(left_node, name3_child, style="dashed")
                graph.add_edge(name3_child, right_node, style="dashed")
                graph.add_edge(name3_child, name3)
                relationship_dict[
                    (name1 + "_unmarried", name2 + "_unmarried")
                ] = [name3_child, right_node]
            else:
                tkinter.messagebox.showerror(message="Relationship existed!")

        elif name1 != "" and name2 != "":
            tkinter.messagebox.showerror(message="Please add the relation of parents before adding child!")

        elif name1 != "":
            if not graph.has_edge(name1, name3) and not graph.has_edge(name3, name1):
                graph.add_subgraph(name3)
                graph.add_edge(name1, name3)
            else:
                tkinter.messagebox.showerror(message="Relationship existed!")

        elif name2 != "":
            if not graph.has_edge(name2, name3) and not graph.has_edge(name3, name2):
                graph.add_subgraph(name3)
                graph.add_edge(name2, name3)
            else:
                tkinter.messagebox.showerror(
                    message="Relationship existed, or one of them is married!"
                )

    elif relation_type[0] == "3":
        if name1 != name2 and name1 and name2:
            name1_unmarried = name1 + "_unmarried"
            name2_unmarried = name2 + "_unmarried"
            if (name1_unmarried, name2_unmarried) not in relationship_dict and \
                    (name2_unmarried, name1_unmarried) not in relationship_dict and \
                    (name1 + "_married", name2 + "_married") not in relationship_dict and \
                    (name2 + "_married", name1 + "_married") not in relationship_dict:
                subgraph = graph.add_subgraph(rank="same")
                if name1_unmarried not in graph.nodes():
                    subgraph.add_node(name1_unmarried, shape="point")
                if name2_unmarried not in graph.nodes():
                    subgraph.add_node(name2_unmarried, shape="point")
                if len(graph.neighbors(name1_unmarried)) == 0:
                    graph.add_edge(name1, name1_unmarried)
                if len(graph.neighbors(name2_unmarried)) == 0:
                    graph.add_edge(name2, name2_unmarried)
                subgraph.add_edge(name1_unmarried, name2_unmarried, style="dashed", rank="same")
                relationship_dict[
                    (name1_unmarried, name2_unmarried)] = [name1_unmarried, name2_unmarried]
            else:
                tkinter.messagebox.showerror(message="Relationship existed or the person is in another relationship!")
        else:
            tkinter.messagebox.showerror(message="They are same person!")

    return graph, relationship_dict
