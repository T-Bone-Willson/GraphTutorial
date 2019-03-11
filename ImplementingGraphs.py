#print("Hello World")

#This is a Directed Graph
#Create Dictionary with elements within that represent "Nodes/Vertices"
#graph = {'A': ['B', 'C'], #"['B', 'C']" represents edge connection from Node A
#         'B': ['C', 'D'], # "[]" connectable nodes are contained in a list
#         'C': ['D'],
#         'D': ['C'],
#         'E': ['F'],
#         'F': ['C']}

#def find_path(graph, start, end, path=[]):
#    path = path + [start]
#    if start == end:
#        return path
#    if not graph.has_key(start):
#        return None
#    for node in graph[start]:
#        if node not in path:
#            newpath = find_path(graph, node, end, path)
#            if newpath: return newpath
#    return None

# Creates class called graph. Takes in two arguements
class graph:
    def __init__(self, graph_dictionary = None):
        if graph_dictionary is None:
            graph_dictionary = [] # sets graph_dictionary to an empty list
        self.graph_dictionary = graph_dictionary

# Get the keys of the dictionary
    def getNodes(self):
        return list(self.graph_dictionary.keys()) # "Keys()" method returns a list of
                                                  # all avaliable keys in a dictionary

# Find list of edges
    def getEdges(self):
        edge_name = []
        for node in self.graph_dictionary:
            for next_node in self.graph_dictionary[node]:
                if {next_node, node} not in edge_name:
                    edge_name.append({node, next_node})
        return edge_name

# Create the dictionary with graph elements
graph_elements = {"a" : ["b", "c"],
         "b" : ["a", "d"],
         "c" : ["a", "d"],
         "d" : ["e"],
         "e" : ["d"]
         }
# "g" is assigned the graph element values from the class graph
g = graph(graph_elements)

#Print graph
print(g.getEdges())
