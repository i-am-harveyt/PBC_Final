from tkinter import filedialog
import tkinter.messagebox
import pygraphviz


def export_graph(graph: pygraphviz.AGraph):
    file_type = [
        ("JPG file", ".jpg"),
        ("PNG file", ".png")
    ]
    filename = filedialog.asksaveasfilename(filetypes=file_type)

    graph.layout("dot")
    if filename.strip(".jpg").strip(".png"):
        graph.draw(filename)
        tkinter.messagebox.showinfo(message="Export Succeed")
