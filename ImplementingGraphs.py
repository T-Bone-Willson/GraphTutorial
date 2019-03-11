#print("Hello World")

#This is a Directed Graph
#Create Dictionary with elements within that represent "Nodes/Vertices"
graph = {'A': ['B', 'C'], #"['B', 'C']" represents edge connection from Node A
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
