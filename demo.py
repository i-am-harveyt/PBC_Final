import pygraphviz

if __name__ == '__main__':
    graph = pygraphviz.AGraph(dpi=300)
    graph.graph_attr['label'] = "DEMO"

    graph.add_node("A")
    graph.add_node("G")
    graph.add_node("T")
    graph.add_node("H")
    graph.add_node("J")

    graph.subgraph("Gen1").add_node("A&G", shape="point")
    graph.subgraph("Gen1").add_edge(
        "A", "A&G",
        dir='none',
        rank='same'
    )
    graph.subgraph("Gen1").add_edge(
        "A&G", "G",
        dir='none',
        rank='same'
    )
    graph.add_subgraph(
        nbunch=["G", "A", "A&G"],
        name="Gen1",
        rank="same"
    )

    graph.subgraph("Siblings").add_node("T&H", shape="point")
    graph.subgraph("Siblings").add_edge(
        "T", "T&H",
        dir='none',
        rank='same'
    )
    graph.subgraph("Siblings").add_edge(
        "T&H", "H",
        dir='none',
        rank='same'
    )
    graph.add_subgraph(
        nbunch=["T", "H", "T&H"],
        name="Siblings",
        rank="same"
    )

    graph.add_edge(
        "A&G", "T&H",
        dir='none'
    )

    graph.layout("dot")
    graph.draw("Demo.jpg")
