from tkinter import filedialog


def export_graph(graph):
    file_type = [
        ("JPG file", ".jpg"),
        ("PNG file", ".png")
    ]
    filename = filedialog.asksaveasfilename(filetypes=file_type)

    graph.layout("dot")
    graph.draw(filename)
