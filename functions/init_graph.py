import pygraphviz


def init_graph():
    graph = pygraphviz.AGraph(
        dpi=200, strict=False,
        splines=False, overlap="scale",
        encoding="UTF-8"
    )
    graph.node_attr["fixedsize"] = True
    graph.node_attr["fontsize"] = "8"
    graph.layout("dot")
    graph.draw("Preview.png")
    return graph
