# Data Structures and Algorithms

## Introduction
- Overview and Philosophy of Data Structures
- Need for Data Structures
- Costs and Benefits
- Abstract Data Types (ADTs)
- Data Structures – Principles and Patterns.

## Complexity Analysis
- Basic complexity analysis
- Best, Worst, and Average Cases
- Asymptotic Analysis (Big-Oh notation)
- Amortized Analysis
- Asymptotic Notations Completeness
- Analyzing Programs
- Space Bounds
- Time and Space Complexity
- Recurrence Relations
  - Methods to solve them including Recursion tree, Substitution, and the Master Method
- Sorting Lower Bounds
- Master Theorem Exceptions

## Arrays & Strings
- 1D Array, 2D Array, Matrix, LU Decomposition
- Kadane’s Algorithm (Maximum Subarray)
- Dutch National Flag algorithm.
- Strings
  - Immutability concepts
  - palindrome checks
  - anagrams

## Linked List
- Singly Linked List
- Doubly Linked List
- Circular Linked List (Singular/Doubly)
- Linked List ADT
- Basic Operations
  - Insertion (beginning/end/given position)
  - Deletion (beginning/end/given position)
  - Display/Traversal (both directions)
  - Search
- Common Problems
  - Reversing
  - detecting cycles
  - merging
  - finding the middle element

## Stack
- Stack ADT properties (LIFO)
- Operations: push(), pop(), peek(), isFull(), isEmpty()
- Array-based Stack Implementation
- Linked Stacks based Implementation
- Min Stack / Max Stack
- Implementing Recursion using Stacks
- Applications
  - Function execution
  - Nested functions
  - Tower of Hanoi
  - Infix/Postfix/Prefix expression conversion and evaluation
  - Matching Valid Parentheses
  - Next Greater Element

## Queue
- Queue ADT properties (FIFO)
- Simple Queue
- Circular Queue
- Double Ended Queue (Deque)
- Priority queue – (push_front(x), push_back(x), pop_front(), pop_back(), peek_front(), peek_back(), size(), isEmpty()). Implementing Priority Queue using List.
- Operations: enqueue(), dequeue(), peek(), isFull(), isEmpty(). Front() & rear() for circular queue
- Array based queue implementation (queue/circular queue, deque)
- Linked Lists based queue implementation queue/circular queue, deque)
- Queue applications

## Trees and Heaps
- Tree Definition and Properties
- Tree ADT
- Basic tree traversals.
- General Trees (N-ary trees) and Forests.
- Binary tree
  - Full, complete, perfect, and balanced binary trees.
  - Linked Structure based Tree Implementation and Array-based Tree implementation.
  - Calculating height, diameter, and Lowest Common Ancestor (LCA)
- Binary Search Trees
  - Definition, properties
  - conversion of a Forest to a binary tree.
  - Implementation of BST using arrays and dynamic allocation (Insertion and deletion operations).
- Heaps
  - Binary Heap
  - Heap property, properties and functions
  - Heapsort.
  - Advanced: Binomial Heap & Fibonacci Heap
  - Top 'K' elements, merging K sorted lists, finding the median in a data stream
- Balanced Trees
  - Definition of Balanced Trees.
  - Self-Balancing Binary Search Trees
  - AVL Trees: Balance factor, rotating subtrees (Right, Left, Left-Right, Right-Left rotations).
  - Red-Black trees
  - B Trees & B+ Trees (Indexing in databases, K-way tree insertion and deletion). Disk-Based Trees

## Maps
- Map ADT, List-based Implementation.

## Dictionary
- Dictionary ADT, Skip Lists (Implementation and Complexity).

## Hash maps
- Hashing ADT
- Simple mapping
- Hash functions
- Hash tables.
- Collision Handling methods
  - Separate Chaining
  - Open Addressing
  - Linear/Quadratic Probing
  - Double Hashing
  - Rehashing.

## Graphs
- Introduction, Properties
- Representation of graphs
  - Adjacency matrix
  - Adjacency list
  - Edge List
- Graph traversal methods
  - Depth First Search – DFS
  - Breadth First Search – BFS
- Bipartite Graphs / Graph Coloring
- Applications of BFS
  - Distance
  - Connectivity
  - Finding connected components
  - identifying cycles in undirected graphs
  - Finding the shortest path in unweighted graphs
  - BFS-based Topological Sorting using in-degrees Kahn’s Algorithm
- Applications of DFS
  - Topological sort
  - identifying cycles in directed graphs
  - Biconnected Components
  - Strong Connectivity.
  - Finding paths
  - solving mazes/grid problems.
- Connectivity of a graph
- Directed Acyclic Graph (DAG)
- Topological Sorting
- Strongly Connected Components
  - Find SCCs using Kosaraju's Algorithm
  - Find SCCs using Tarjan's Algorithm
- Minimum Spanning Trees
  - MST
  - Kruskal's Algorithm. (greedy)
  - Prim's Algorithm. (greedy)
- Shortest Path Algorithms
  - Dijkstra’s Algorithm using Min-Heap. (greedy)
  - Bellman-Ford Algorithm. (DP)
  - Floyd-Warshall Algorithm. (DP)
- Applications
  - Computer network topology
  - Finding paths in a network.
- Advanced Network Flow & Cut Problems
  - Flow Networks
  - Augmenting Paths: Ford-Fulkerson & Dinic's Algorithms
  - Network Flow Problems
  - Max-Flow Min-Cut Theorem
  - Biconnected Components
  - Edmonds Blossom Algorithm
- Disjoint Set Union (DSU) / Union-Find
  - Path Compression & Union by Rank

## Tries
- Definition & Introduction to Trie Trees
- Suffix links of TRIE trees.
- Insert, delete, and search operations.
- XOR Trie
- String Matching Algorithms
  - KMP (Knuth-Morris-Pratt)
  - Rabin-Karp (Rolling Hash)
  - Z-Algorithm
- Applications: Cryptography, URL decoding, Autocomplete systems/Word prediction using TRIE trees/Suffix Trees
- Advanced
  - Treaps, Bit maps, Bloom Filter

## Searching
- Linear Search
- Binary Search
- Jump Search & Exponential Search
- Interpolation Search & Fibonacci Search

## Sorting
- Basic: Insertion Sort, Selection Sort & Bubble Sort
- Quick Sort & Merge Sort (Divide & Conquer)
- Heap Sort
- Non-Comparison / Linear Time Sorts: Counting Sort, Radix Sort & Bucket Sort
- Shell sort

## Recursion
- Tower of Hanoi Using Recursion
- Fibonacci Series Using Recursion

## Divide and Conquer
- Introduction
- Binary Search
- Merge Sort
- Quick Sort
- Strassen's Matrix Multiplication
- Karatsuba Fast Long integer Multiplication Algorithm
- Maximum sub-array sum problem
- Max-Min Problem
- Closest pair of points
- Advanced
  - Fast Fourier Transform
  - Convex Hull

## Greedy Algorithm
- Introduction to the greedy method
- Fractional Knapsack problem
- Task Scheduling Problem with Deadline
- Travelling Salesman Problem
- Huffman Coding – Data compression
- Jump Game / Coin Change (Greedy Variants) Problem
- Graph
  - Prim's Minimal Spanning Tree Algorithm
  - Kruskal's Minimal Spanning Tree Algorithm
  - Dijkstra's Shortest path Algorithm
  - Graph − Map Coloring
  - Graph − Vertex Cover
- Optimal Merge Pattern Algorithm

## Dynamic Programming
- Introduction
- Memoization (Top-Down) vs. Tabulation (Bottom-Up).
- 1D
  - computing Fibonacci numbers
  - Coin Change Problem
  - Climbing Stairs
  - Maximum Subarray (Kadane's Algorithm)
  - House robber
- 2D
  - Unique Paths
  - Minimum path sum
- Strings & Sequences
  - Longest Palindromic Substring
  - Longest Common Subsequence Algorithm
  - Edit Distance (Levenshtein Distance)
  - Regular Expression Matching
- 0-1 Knapsack problem
- Unbounded Knapsack
- Matrix chain multiplication problem.
- Travelling Salesman Problem (Dynamic Approach)
- Interval & Partition DP
- Palindrome Partitioning
- Burst Balloons.
- DP on Trees & DP with Bitmasking
- Traveling Salesperson
- Subtree queries.
- Graph
  - Single Source Shortest Path (SSSP): Bellman-Ford algorithm.
  - All Pairs Shortest Path (APSP): Floyd-Warshall's algorithm
- Digit DP

## Branch and Bound
- Branch and Bound strategies applied to the 0-1 Knapsack problem, Traveling Salesperson Problem

## Backtracking
- Introduction
- N-Queen problem.
- Permutations / Combinations / Subsets
- Word search

## Complexity Classes
- Introduction to NP class
- Definitions of P, NP, NP-complete, NP-hard problems
- Examples of P and NP class problems

## Algorithm design Patterns
- Two Pointers: Opposite-end and same-direction pointers (Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water).
- Fast & Slow Pointers: Floyd’s Cycle-Finding Algorithm (Linked List cycle detection, Middle of Linked List, Find Duplicate Number).
- Sliding Window: Fixed & variable length windows for substring and subarray problems (Longest Substring Without Repeating Characters, Minimum Window Substring).
- Monotonic Stack / Queue: Maintains elements in monotonic order (Next Greater Element, Daily Temperatures, Largest Rectangle in Histogram, Sliding Window Maximum).
- Binary Search on Answer Space: Using a predicate function over a monotonic search space (Koko Eating Bananas, Capacity to Ship Packages, Aggressive Cows).
- Bit Manipulation & Bitmasking: Bitwise XOR tricks, bitmask subsets, counting set bits (Single Number, Subsets generation, Power of Two)
- Array & String Patterns
  - Intervals / Sweep Line: Merge Intervals, Meeting Rooms (I & II), Insert/Remove Intervals. (A massive omission in your current list).
  - Prefix Sum & Difference Arrays: Subarray Sum Equals K (Prefix Sum + Hash Map), 2D Prefix Sums.
  - Top K Elements: K-way merge using a Min/Max Heap (e.g., Kth Largest Element, Merge K Sorted Lists).
- Tree & Graph Archetypes
  - Tree BFS / Level Order Traversal: Zigzag level order, Right side view, Vertical order traversal.
  - Tree Path Problems: Binary Tree Maximum Path Sum, Diameter of Binary Tree.
  - Multi-Source BFS: Essential for grid problems (e.g., Rotting Oranges, 01 Matrix).
- Fast Exponentiation & Modular Arithmetic

## Data Structure Design
- LRU Cache
- LFU Cache: (Hash Map + Frequency Buckets of Doubly Linked Lists).
- Median from Data Stream: Maintaining running medians using two Heaps (Max-Heap + Min-Heap).
- RandomizedSet: Supporting insert, remove, and getRandom all in $O(1)$ time (Hash Map + Dynamic Array).

## Advanced
- Approximation Algorithms
- Randomized Algorithms
- Bit Manipulation: AND, OR, XOR operations, shifting, finding single numbers, masking.
- Mathematics: Sieve of Eratosthenes (Prime numbers), Euclidean Algorithm (GCD), Modular Arithmetic
