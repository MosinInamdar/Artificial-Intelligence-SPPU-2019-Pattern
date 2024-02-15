def dfs(visited, graph, node):
#checks if node is present in visited or not
    if node not in visited:
    #if not present then print it and add in visited
        print(node, "-> ",end="")
        print()
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            
def main():
    temp = ""
    visited = set()
    n=int(input("Enter the number of nodes: "))
    graph = dict()
    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        nodevalue = input("Enter Node Name: ")
        if i==1:
            temp = nodevalue
        graph[nodevalue]=[]
        for j in range(1,edges+1):
            node = input("Enter edge {} for node {} : ".format(j,i))
            graph[nodevalue].append(node)

    dfs(visited, graph, temp)

main()