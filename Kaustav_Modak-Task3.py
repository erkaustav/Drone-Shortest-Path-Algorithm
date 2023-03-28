# Recursive function to print the path of given vertex `u` from source vertex `v`
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])


# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                print(f'The shortest path from {v} —> {u} is', route)


# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix):
    # base case
    
    if not adjMatrix:
        return

    # total number of vertices in the `adjMatrix`
    n = len(adjMatrix)

    # cost and path matrix stores shortest path
    # (shortest cost/shortest route) information

    # initially, cost would be the same as the weight of an edge
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]

    # initialize cost and path
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1

    # run Floyd–Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # If vertex `k` is on the shortest path from `v` to `u`,
                # then update the value of cost[v][u] and path[v][u]
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]

            # if diagonal elements become negative, the
            # graph contains a negative-weight cycle
            if cost[v][v] < 0:
                print('Negative-weight cycle found')
                return

    # Print the shortest path between all pairs of vertices
    printSolution(path, n)

# define infinity
I = float('inf')

# taking inputs of m and n grid
m = int(input('Enter m grid = '))
n = int(input('enter n grid = '))
dn = int(input('Enter number of drones = '))
  # size of the matrix
  # value to be set
if(m>n):
    xx=m
else:
    xx=n
# create an empty 2D matrix with n rows and n columns
adjMatrix = [[0 for x in range(xx)] for y in range(xx)]

# update values in the matrix while keeping diagonal values at 0
for i in range(xx):
    for j in range(xx):
        if i != j:  # if not a diagonal element
            adjMatrix[i][j] = I

# print the updated matrix
for row in adjMatrix:
    print(row)

# taking inputs of strating location, destination location and times
for a in range(dn):
    print('Input format : x1<space>y<space>x2<space>y2<space>t<enter>')
    l=list(map(int, input().split()))
            
    x1 = l[0]
    y1 = l[1]
    x2 = l[2]
    y2 = l[3]
    t = l[4]
    print(l)
    
    adjMatrix [x1][y2] = t
# Run Floyd–Warshall algorithm
    
floydWarshall(adjMatrix)

