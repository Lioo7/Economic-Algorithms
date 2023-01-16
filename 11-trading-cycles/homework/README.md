# Top Trading Cycle
This project is an implementation of the algorithm that finds a cycle in the trading houses graph when all the players have strong preferences.

## The Algorithm
Top trading cycle (TTC) is an algorithm for trading indivisible items without using money. 
<br>
It was developed by David Gale and published by Herbert Scarf and Lloyd Shapley.

## Input
The input to the algorithm is a list of lists of integers, where each inner list represents the preferences of a player. The value at index i of an inner list represents the ith preference of the player.

## Output
The output of the algorithm is a list of integers representing the nodes in the largest cycle in the trading houses graph.

## Steps
The algorithm works by first finding a trading cycle using the trading cycle algorithm, then removing the nodes that are part of the cycle and repeating the process until no more cycles can be found.

1. Find a trading cycle using the trading cycle algorithm.
2. Each person gets the house he points to.
3. Remove the nodes that are part of the cycle.
4. Each person left in the graph's edge is updated to point to the house they want the most from those left.
5. Repeat steps 1-4 until no more cycles can be found.

## Visualization
You can visualize the top trading cycle in the graph using the methods that are provided in the code.
<br>
You can enable the visualization by setting the 'save_graphs' parameter to True.

## Example
### Input
preferences = [[1, 2, 0], [2, 0, 1], [0, 1, 2]]
<br>
In this example, the player #0 has a preference for houses 1, 2, and 0 in that order. Similarly, player #1 has a preference for houses 2, 0, and 1, and player #3 has a preference for houses 0, 1, and 2.
<br>
- Players are represented by positive nodes, while houses are represented by negative nodes.
<br>
- If a house has an edge to a player, that means the player is the tenant.
<br>
- If a player edges a house, that player wants to live there.
<img src="https://i.ibb.co/84cq0Pb/input-graph.png" width="100%" />

### Output
[0,1,2,0]
<br>
The output above means that after the trading, player #0 lives in house #1, player #1 lives in house #2 and player #2 lives in house #0.
<img src="https://i.ibb.co/TrNwfV6/output-graph.png" width="100%" />

It's also important to note that the top trading cycle algorithm may not always find the largest cycle, it depends on the order of the nodes in the original graph.

The algorithm's implementation includes several tests that can be run using the doctest library and also it includes a visualization of the input and output graph using NetworkX library (using only for the visualization).