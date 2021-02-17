Problem Statement
-------------------

The travelling salesman problem asks the following question:
 "Given a list of cities and the distances between each pair of cities,
  what is the shortest possible route that visits each city exactly once and returns to the origin city?"


Problem Explanation
---------------------
Let's say we have a graph given for above problem. To trasvel from one city(node in graph) to another city
there may be multiple path. So, when we start travelling from city "A" and want to travel all the cities and come back to "A" again.
We may have multiple route for this. Some of the routes may include the longest path and some of may even not go via that longest path.
Due to this we will have different routes and total_distance_covered to come back to our start city. 
We need to find the route which includes least distance to achieve the required conditions of the problem.

How we will do this?
----------------------
We will create an adjacent matrix of the graph and take this matrix as input to the program and output will be 
the path with least distance which visited all the cities.

How to find the least distance?
----------------------------------

1. We will update the adjacent matrix by finding least distance from one node to another brute force
2. Then we can go for dynamic progrmming to solve this issue.


