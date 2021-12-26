import pygraphviz


def init_graph():
    graph = pygraphviz.AGraph(
        dpi=200, strict=False, splines=False, overlap="scale"
    )
    graph.node_attr["fixedsize"] = True
    graph.node_attr["fontsize"] = "9"
    graph.layout("dot")
    graph.draw("Preview.png")
    return graph
