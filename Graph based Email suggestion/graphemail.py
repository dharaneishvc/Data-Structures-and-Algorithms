# Adjacency List representation of Graph

class AdjNode:
  def __init__(self, value):
    self.vertex = value
    self.next = None

class Graph:
  def __init__(self, num):
    self.V = num
    self.graph = [None] * self.V

  # Add edges
  def add_edge(self, s, d):
    #Source to Destination
    node = AdjNode(d)
    node.next = self.graph[s]
    self.graph[s] = node
    #Destination to Source (in case of bi-directed)
    node = AdjNode(s)
    node.next = self.graph[d]
    self.graph[d] = node

    # Print the graph
  def print_agraph(self):
    for i in range(self.V):
      print("Vertex " + str(i) + ":", end="")
      temp = self.graph[i]
      while temp:
        print(" -> {}".format(temp.vertex), end="")
        temp = temp.next
      print(" \n")

if __name__ == "__main__":
  #TESTING WITHOUT FILE
  '''
  V = 5
  # Create graph and edges
  graph = Graph(V)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(0, 3)
  graph.add_edge(1, 2)
  '''

  filelink = open("Email-EuAll.txt","r")
  V = len(filelink.readlines())
  graph = Graph(V)
  file_line = filelink.readline()
  # use the readline() method to read further.
  # If the file is not empty keep reading one line at a time, till the file is empty
  while file_line:
    #str.split() method is used split the string into a list of strings.
    #map() function is used to convert each string into an integer.
    #list() class is used to convert the map object to a list.
    numlist = list(map(int, file_line))
    graph.add_edge(numlist[0],numlist[1])
    print(file_line)
    # use realine() to read next line
    file_line = filelink.readline()
  filelink.close()
  
  graph.print_agraph()