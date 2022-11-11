#Auto Mail Match suggestion

While the user type to-address or search for mail users, this product predicts and displays the perfect match for input based on the previous sent data of all mail users. It displays in the order the mail is very close to a user or not.
Dataset description:
https://snap.stanford.edu/data/email-EuAll.html
This dataset contains anonymized information about all incoming and outgoing email of a large European research institution for a period from October 2003 to May 2005 (18 months). For each sent or received email message the dataset contains the time, the sender and the recipient of the email. Overall, it contains 3,038,531 emails between 287,755 different email addresses. Note that the dataset contains only complete email graph for only 1,258 email addresses that come from the research institution. Furthermore, there are 34,203 email addresses that both sent and received email within the span of our dataset. All other email addresses are either non-existing, mistyped or spam.
Given a set of email messages, each node corresponds to an email address and a directed edge between nodes i and j, if i sent at least one message to j.

#Choosing Graph Representation
Adjacency list is the perfect representation of graph for this method. An adjacency list is efficient in terms of storage because we only need to store the values for the edges. Our dataset is a sparse graph with millions of vertices and edges, this can mean a lot of saved space.  Meanwhile VxV space requirement of the adjacency matrix makes it a memory hog. Our dataset Email Graphs don't have too many connections, and this causes wastage of space. Hence adjacency lists are the better choice for most tasks.
It also helps to find all the vertices adjacent to a vertex easily.
