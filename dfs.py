def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" -> ")  # Print the current node and a separator
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def bfs(visited, graph, node):
    queue = [node]
    visited.add(node)  # Mark the start node as visited before the loop

    while queue:
        s = queue.pop(0)
        print(s, end=" -> ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)  # Mark as visited when enqueued
                queue.append(neighbour)

def main():
    visited_dfs = set()
    visited_bfs = set()
    n = int(input("Enter the number of nodes: "))
    graph = dict()

    for i in range(1, n+1):
        nodevalue = input(f"Enter Node Name for node {i}: ")
        edges = int(input(f"Enter number of edges for node {nodevalue}: "))
        graph[nodevalue] = []
        for j in range(1, edges+1):
            node = input(f"Enter edge {j} for node {nodevalue}: ")
            graph[nodevalue].append(node)

    start_node = next(iter(graph))  # Get the first node added to start the traversals
    print("DFS traversal:")
    dfs(visited_dfs, graph, start_node)
    print("\nBFS traversal:")
    bfs(visited_bfs, graph, start_node)

if __name__ == "__main__":
    main()
