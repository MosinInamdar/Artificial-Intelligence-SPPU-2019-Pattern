# Implement a solution for Contraint statisfaction problem using branching and bound and backtracking for graph coloring problem

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to check if the current color assignment is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m coloring problem
    def graphColourUtil(self, m, colour, v, color_map):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c):
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1, color_map):
                    return True
                colour[v] = 0

    def graphColouring(self, color_labels):
        m = len(color_labels)
        color_map = {i + 1: color_labels[i] for i in range(m)}
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0, color_map) is None:
            return False

        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(color_map[c], end=' ')
        return True

# Driver Code
if __name__ == '__main__':
    node = int(input("Enter the number of nodes: "))
    g = Graph(node)
    print("Enter 1 if node is connected to other node else 0")
    g.graph = []
    for i in range(node):
        nodeArray = []
        print(f"Node {i+1}: ")
        for j in range(node):
            nodeValue = int(input(f"Node connected to {j + 1}: "))
            nodeArray.append(nodeValue)
        g.graph.append(nodeArray)
    
    colors = input("Enter the color labels (e.g., R G B): ").split()
    # Function call
    g.graphColouring(colors)
