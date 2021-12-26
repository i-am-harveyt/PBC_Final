import tkinter as tk
from PIL import Image, ImageTk
from functions.add_person import AddPerson, add_person
from functions.delete_person import DeletePerson, delete_person
from functions.add_relation import AddRelation, add_relation
from functions.delete_relation import DeleteRelation, delete_relation
from functions.export_graph import export_graph
from functions.init_graph import init_graph


# TODO write a "clear all", if have enough time and strength
# TODO add the messageBox to all the function, if there is alert
class Controller(object):
    def update_graph(self):

        if self.debug:
            print(f"nodes: {self.graph.nodes()}")
            print(f"edges: {self.graph.edges()}")
            print(f"dict: {self.relationship_dict}")
            print("---------")

        self.graph.layout("dot")
        self.graph.draw("Preview.png")
        self.graph_file = ImageTk.PhotoImage(Image.open("Preview.png"))
        self.graph_preview.configure(image=self.graph_file)
        self.graph_preview.image = self.graph_file

    def click_add_person(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = AddPerson(window).get_add_value()
            self.function_in_use = False

            if result:
                if result[0]:
                    self.graph, self.person_list = add_person(
                        self.graph, self.person_list,
                        result[0], result[1], result[2], result[3]
                    )
                    self.update_graph()

    def click_delete_person(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = DeletePerson(window, self.person_list).get_del_value()
            self.function_in_use = False

            if result in self.person_list:
                self.graph, self.person_list = delete_person(self.graph, self.person_list, result)
                self.update_graph()

    def click_add_relation(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = AddRelation(window, self.person_list).get_add_value()
            self.function_in_use = False

            if result:
                if result[0] or result[1]:
                    self.graph, self.relationship_dict = add_relation(
                        self.graph, self.relationship_dict,
                        result[0], result[1],
                        result[2], result[3]
                    )
                    self.update_graph()

    def click_delete_relation(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = DeleteRelation(window, self.person_list).get_delete_value()
            self.function_in_use = False

            if result:
                if result[0] or result[1]:
                    self.graph, self.person_list, self.relationship_dict = delete_relation(
                        self.graph, self.person_list, self.relationship_dict,
                        result[0], result[1], result[2], result[3]
                    )
                    self.update_graph()

    def click_export_graph(self):
        export_graph(self.graph)

    def __init__(self, window):
        self.debug = False
        self.function_in_use = False
        self.relationship_dict = {}

        window.title("Main Page")
        self.graph = init_graph()
        self.graph.edge_attr.update(len="2.0")
        self.graph_file = ImageTk.PhotoImage(Image.open("Preview.png"))
        self.graph_preview = tk.Label(image=self.graph_file)
        self.graph_preview.image = self.graph_file
        self.graph_preview.grid(row=0, column=0, columnspan=5)

        self.person_list = []

        add_person_button = tk.Button(
            window, text="Add Person",
            command=lambda: [
                self.click_add_person(window)
            ])
        add_person_button.grid(row=1, column=0)

        delete_person_button = tk.Button(
            window, text="Delete Person",
            command=lambda: [
                self.click_delete_person(window)
            ])
        delete_person_button.grid(row=1, column=1)

        add_relation_button = tk.Button(
            window, text="Add Relation",
            command=lambda: [
                self.click_add_relation(window)
            ])
        add_relation_button.grid(row=1, column=2)

        delete_relation_button = tk.Button(
            window, text="Delete Relation",
            command=lambda: [
                self.click_delete_relation(window)
            ])
        delete_relation_button.grid(row=1, column=3)

        export_graph_button = tk.Button(
            window, text="Export Graph",
            command=self.click_export_graph
        )
        export_graph_button.grid(row=1, column=4)
