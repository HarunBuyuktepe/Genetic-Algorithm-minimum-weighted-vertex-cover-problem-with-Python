# Genetic-Algorithm-minimum-weighted-vertex-cover-problem-with-Python

In this project, I realized “Minimum Weighted Vertex Cover Problem” with using different graphs. Each graphs has nodes and their weight. Here, we should do maximum cover with minimum weight. At the beginning of the program, we brought the user input and we run the run() method with our parameters.(Graph name, #Generation, #Population,Crossover Prob. And Mutation Prob.)

First, I read given file and formatted usable fitness with readFile() method. And I keep our nodes in Hash map data type to reach maximum efficiency in time.

And next, I created initial population with random uniform. After every generation, I checked for proper that means checking reach all nodes in the graph.

If not suitable, I use repair() function to randomly make solution proper.

Then, I applied crossover and mutation respect to given parameters.

After, mutation I check again the feasibility of all solution string with using repair2() method.

repair2() is different from repair(). In this method, I try to make 1’s 0 with randomly.

End of the this repair2(), I select best solution and iterate with result of mutation.
And finally, I printed the best of the best list.
