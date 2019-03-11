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


# Create the dictionary with graph elements
graph = {"a" : ["b", "c"],
         "b" : ["a", "d"],
         "c" : ["a", "d"],
         "d" : ["e"],
         "e" : ["d"]
         }

#Print graph
print(graph)
