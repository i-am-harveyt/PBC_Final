import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from functions.front_add_person import AddPerson
from functions.func_add_person import add_person
from functions.front_delete_person import DeletePerson
from functions.func_delete_person import delete_person
from functions.front_add_relation import AddRelation
from functions.func_add_relation import add_relation
from functions.front_delete_relation import DeleteRelation
from functions.func_delete_relation import delete_relation
from functions.export_graph import export_graph
from functions.init_graph import init_graph


# TODO write a "clear all", if have enough time and strength
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
        self.graph_file_x = self.graph_file.width()
        self.graph_file_y = self.graph_file.height()
        self.canvas.create_image(
            self.HEIGHT/2, self.WIDTH/2,
            image=self.graph_file, anchor="center"
        )
        self.canvas.configure(
            scrollregion=(
                min(0, self.WIDTH/2-self.graph_file_x/2),
                min(0, self.HEIGHT/2-self.graph_file_y/2),
                max(self.WIDTH, self.graph_file_x/2+self.WIDTH/2),
                max(self.HEIGHT, self.graph_file_y/2+self.HEIGHT/2)
            )
        )

    def click_add_person(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = AddPerson(window).get_add_value()
            self.function_in_use = False

            if result:
                if result not in self.person_list:
                    if result[0]:
                        self.graph, self.person_list = add_person(
                            self.graph, self.person_list,
                            result[0], result[1], result[2], result[3]
                        )
                        self.update_graph()
                    else:
                        tkinter.messagebox.showerror(message="Wrong Input!")
                else:
                    tkinter.messagebox.showerror(message="Person existed!")

    def click_delete_person(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = DeletePerson(window, self.person_list).get_del_value()
            self.function_in_use = False

            if result:
                # Is this condition needed? I think it can be discussed later.
                if result in self.person_list:
                    self.graph, self.person_list = delete_person(self.graph, self.person_list, result)
                    self.update_graph()
            elif result == "":
                tkinter.messagebox.showerror(message="Wrong Input!")

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
                else:
                    tkinter.messagebox.showerror(message="Wrong Input!")

    def click_delete_relation(self, window):
        if not self.function_in_use:
            self.function_in_use = True
            result = DeleteRelation(window, self.person_list, self.relationship_dict).get_delete_value()
            self.function_in_use = False

            print(result)

            if result:
                if result[0] or result[1]:
                    self.graph, self.person_list, self.relationship_dict = delete_relation(
                        self.graph, self.person_list, self.relationship_dict,
                        result[0], result[1], result[2], result[3]
                    )
                    self.update_graph()
                else:
                    tkinter.messagebox.showerror(message="Wrong input!")

    def click_export_graph(self):
        self.graph.graph_attr.update(dpi=300)
        export_graph(self.graph)
        self.graph.graph_attr.update(dpi=200)

    def yscroll_canvas(self, event):
        if event.state == 0:
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        if event.state == 1:
            self.canvas.xview_scroll(int(-1 * event.delta), "units")

    def __init__(self, window: tkinter.Tk):
        self.debug = False
        self.function_in_use = False
        self.relationship_dict = {}
        self.person_list = []
        self.WIDTH = 500
        self.HEIGHT = 500

        window.title("Main Page")
        window.geometry("600x550")
        window.resizable(0, 0)

        self.frame = tkinter.Frame(window, width=500, height=500)
        self.frame.grid(row=0, column=0, columnspan=5)

        self.graph = init_graph()
        self.graph.edge_attr.update(len="2.0")
        self.graph_file = ImageTk.PhotoImage(Image.open("Preview.png"))
        self.graph_file_x = self.graph_file.width()
        self.graph_file_y = self.graph_file.height()

        self.canvas = tkinter.Canvas(
            self.frame, bd=0, width=self.WIDTH, height=self.HEIGHT,
            scrollregion=(
                0, 0,
                self.WIDTH, self.HEIGHT
            )
        )

        xscrollbar = tkinter.Scrollbar(
            self.frame, orient=tkinter.HORIZONTAL,
            command=self.canvas.xview
        )
        yscrollbar = tkinter.Scrollbar(
            self.frame, orient=tkinter.VERTICAL,
            command=self.canvas.yview
        )
        xscrollbar.pack(side=tkinter.BOTTOM, fill="x")
        yscrollbar.pack(side=tkinter.RIGHT, fill="y")
        self.canvas.config(
            scrollregion=self.canvas.bbox("all"),
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set
        )
        self.canvas.create_image(
            self.WIDTH/2, self.HEIGHT/2,
            image=self.graph_file, anchor="center"
        )
        self.canvas.bind_all("<MouseWheel>", self.yscroll_canvas)
        self.canvas.pack()

        add_person_button = tk.Button(
            window, text="Add Person",
            command=lambda: [
                self.click_add_person(window)
            ])
        add_person_button.grid(row=2, column=0)

        delete_person_button = tk.Button(
            window, text="Delete Person",
            command=lambda: [
                self.click_delete_person(window)
            ])
        delete_person_button.grid(row=2, column=1)

        add_relation_button = tk.Button(
            window, text="Add Relation",
            command=lambda: [
                self.click_add_relation(window)
            ])
        add_relation_button.grid(row=2, column=2)

        delete_relation_button = tk.Button(
            window, text="Delete Relation",
            command=lambda: [
                self.click_delete_relation(window)
            ])
        delete_relation_button.grid(row=2, column=3)

        export_graph_button = tk.Button(
            window, text="Export Graph",
            command=self.click_export_graph
        )
        export_graph_button.grid(row=2, column=4)
