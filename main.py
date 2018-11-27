from graph import Graph

g = Graph()
g.populate()
g.join_clusters(p=True)
g.mst()
