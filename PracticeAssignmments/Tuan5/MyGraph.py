class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # This function is necessary so that Nodes can be used as
        # keys in a dictionary, even though Nodes are mutable
        return self.name.__hash__()


class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)

    def __eq__(self, other):
        return self.src == other.src and self.dest == other.dest


class WeightedEdge(Edge):
    def __init__(self, src, dest, cost):
        Edge.__init__(self, src, dest)
        self.cost = cost

    def get_total_cost(self):
        return self.cost


    def __str__(self):
        return '{}->{} ({})'.format(self.src, self.dest, self.cost)


class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dict of Node -> list of edges

    def __str__(self):
        edge_strs = []
        for k in self.edges.keys():
            for edge in self.edges[k]:
                edge_strs.append(str(Edge(k,edge.dest)))
        edge_strs = sorted(edge_strs)  # sort alphabetically
        return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

    def get_edges_for_node(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
            self.nodes.add(node)

    def add_edge(self, edge):
        """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the  graph."""
        src = edge.get_source()
        dest = edge.get_destination()
        #weightEdge = WeightedEdge(src, dest, edge.get_total_distance(), edge.get_outdoor_distance())
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(edge)
        #self.edges[src].append(weightEdge)

    def get_level(self, node):
        return len(self.edges[node])

    def remove_edge(self, node, edge):
        tmp = self.edges[node]
        tmp.remove(edge)
        self.edges[node] = tmp
    
    def get_nodes(self):
        return self.nodes

    def remove_all_edge(self, node):
        self.edges[node]=[]
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)
    
    def remove_edge(self, edge):
        #rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.remove_edge(self , edge.get_source(), edge)
        #Digraph.remove_edge(rev)