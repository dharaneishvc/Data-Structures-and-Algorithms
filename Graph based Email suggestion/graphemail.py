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

  def BFS(self, s):
    # Mark all the vertices as not visited
    visited = [False] * (self.V)

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

      # Dequeue a vertex from queue and print it
      s = queue.pop(0)
      print (s, end = ",")

      # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
      nd = self.graph[s]
      while nd:
        if visited[nd.vertex] == False:
          queue.append(nd.vertex)
          visited[nd.vertex] = True
        nd = nd.next

  def minEdgeBFS(self, s, d):
    # Mark all the vertices as not visited
    visited = [False] * (self.V)

    #Pathexist Boolean Value
    pathexist = False

    # Initialize distances as 0
    distance = [0] * (self.V)

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

      # Dequeue a vertex from queue and print it
      s = queue.pop(0)
      if s == d:
        pathexist = True

      # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
      nd = self.graph[s]
      while nd:
        if visited[nd.vertex] == False:
          queue.append(nd.vertex)
          visited[nd.vertex] = True
          distance[nd.vertex] = distance[s] + 1
        nd = nd.next
        
    return [pathexist, distance[d]]

  def printAllPathsUtil(self, u, d, visited, path):

      # Mark the current node as visited and store in path
      visited[u]= True
      path.append(u)

      # If current vertex is same as destination, then print current path[]
      if u == d:
          print (path)
      else:
          # If current vertex is not destination Recur for all the vertices adjacent to this vertex
          nd = self.graph[u]
          while nd:
            if visited[nd.vertex]== False:
              self.printAllPathsUtil(nd.vertex, d, visited, path)
            nd = nd.next
                    
      # Remove current vertex from path[] and mark it as unvisited
      path.pop()
      visited[u]= False

  def printAllPaths(self, s, d):
 
    # Mark all the vertices as not visited
    visited =[False]*(self.V)

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    self.printAllPathsUtil(s, d, visited, path)

if __name__ == "__main__":
  #TESTING WITHOUT FILE
  
  V = 5
  # Create graph and edges
  graph = Graph(V)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(0, 3)
  graph.add_edge(1, 2)
  graph.add_edge(2, 0)
  graph.add_edge(2, 3)
  graph.add_edge(3, 3)
  graph.add_edge(4, 3)

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

'''

  op = 0
  while op != 5:
    print('\n', '─' * 50)
    op = int(input("1. Print Graph \n2. Find Suggestions \n3. Distance between two Nodes(if exists) \n4. All Path between Nodes \n5. Exit \nEnter(1-5): "))
    if(op == 1):
      print("Graph Adjacency List:")
      graph.print_agraph()
    elif(op == 2):
      inn = int(input("Enter your Mail (Node Number):"))
      while (inn >= V or inn < 0):
        inn = int(input("Error! Again Enter your Mail (Node Number (0-V)):"))
      print("The order of Suggestion is: ", end=" ")
      graph.BFS(inn)
    elif(op == 3):
      ins = int(input("Enter Source Mail (Node Number):"))
      while (ins >= V or ins < 0):
        ins = int(input("Error! Again Enter Source (Node Number (0-V)):"))
      ind = int(input("Enter Destination Mail (Node Number):"))
      while (ind >= V or ind < 0):
        ind = int(input("Error! Again Enter Destination (Node Number (0-V)):"))
      a = graph.minEdgeBFS(ins,ind)
      if a[0]:
        print("Path Exists Between 2 points")
        print("The distance between 2 nodes is: ", a[1])
      else:
        print("Path doesn't exist Between 2 points")
    elif(op == 4):
      ins = int(input("Enter Source Mail (Node Number):"))
      while (ins >= V or ins < 0):
        ins = int(input("Error! Again Enter Source (Node Number (0-V)):"))
      ind = int(input("Enter Destination Mail (Node Number):"))
      while (ind >= V or ind < 0):
        ind = int(input("Error! Again Enter Destination (Node Number (0-V)):"))
      print("Set of all paths between 2 nodes are: ")
      graph.printAllPaths(ins, ind)
    else:
      print("Exit")
      break
