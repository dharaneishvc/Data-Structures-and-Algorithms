# *Auto Mail Match suggestion and “Who knows Who”*

While the user type to-address or search for mail users, this feature predicts and displays the perfect match for input based on the previous sent data of all mail users. It displays in the order the mail is very close to a user or not.
When User types destination address fully, this feature displays the connection between both users if exist and the path they are connection similar to mutual friends and followers in social media platforms.

## Dataset description:
https://snap.stanford.edu/data/email-EuAll.html
This dataset contains anonymized information about all incoming and outgoing email of a large European research institution for a period from October 2003 to May 2005 (18 months). For each sent or received email message the dataset contains the time, the sender and the recipient of the email. Overall, it contains 3,038,531 emails between 287,755 different email addresses. Note that the dataset contains only complete email graph for only 1,258 email addresses that come from the research institution. Furthermore, there are 34,203 email addresses that both sent and received email within the span of our dataset. All other email addresses are either non-existing, mistyped or spam.
Given a set of email messages, each node corresponds to an email address and a directed edge between nodes i and j, if i sent at least one message to j.

## Choosing Graph Representation
Adjacency list is the perfect representation of graph for this method. An adjacency list is efficient in terms of storage because we only need to store the values for the edges. Our dataset is a sparse graph with millions of vertices and edges, this can mean a lot of saved space.  Meanwhile VxV space requirement of the adjacency matrix makes it a memory hog. Our dataset Email Graphs don't have too many connections, and this causes wastage of space. Hence adjacency lists are the better choice for most tasks.
It also helps to find all the vertices adjacent to a vertex easily. For Breadth First and Depth First search techniques, Adjacency list is perfect way as it can be traversed easily.

## Algorithm
1.	Input: Read from files and store in the form of Adjacency list as it is the best representation.
2.	Print Graph: Traverse each vertex and print the vertexes which has direct edge link with it.
3.	Mail Suggestion: Do Breadth-First Traversal between with the input as source and print the node elements in order
4.	Check Connection: Calculate the minimum distance between two nodes by doing Breadth-First Traversal from the source vertex and by adding up in distances in each step. At the time of BFS maintain an array of distance[n] and initialize it to zero for all vertices and initialize Found to No for connection checking. Now, suppose during BFS, vertex x is popped from queue and we are pushing all adjacent non-visited vertices(y) back into queue at the same time we should update distance[y] = distance[x] + 1; Also, during the BFS if the second vertex is found in traversal, set found to Yes.
5.	Who Knows Who: Print all path from given source to destination. Do Depth First Traversal of a given directed graph starting from the source. Keep storing the visited vertices in an array. If the destination vertex is reached, print the contents of the array. Also mark current vertices in the array[] as visited also so that the traversal doesn’t go in a cycle.
6.	It works for Both Undirected and Directed Graphs. For Directed Graphs we can also add both from and to as edges so that we get better result.

## Complexity Analysis
* If E is the number of edges and V is number of nodes in a graph, then the time complexity of building such a list is O(E). The space complexity is O(V + E). But, in the worst case of a complete graph, which contains V/2 edges, the time and space complexities reduce to O(n^2)
*	Time Complexity for Mail suggestion and Connection checking is same as that of Breadth-First Traversal ie O(V+E). And auxiliary space required is O(V) as V vertices can be present in the queue or array in the worst case.
*	Time Complexity for Who knows Who is O(V^V), The time complexity is exponential. From each vertex there are V vertices that can be visited from current vertex. Auxiliary space required is O(V^V), To store the paths V^V space is needed.
