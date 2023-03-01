def printList(adj, V):
    for i in range(V):
        print(i, end='')

        for j in adj[i]:
            print(' --> ' + str(j), end='')

        print()

    print()


# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):
    # Initialize a matrix
    matrix = [[0 for j in range(V)]
              for i in range(V)]

    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1

    return matrix


# Function to display adjacency matrix
def printMatrix(adj, V):
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end=' ')

        print()

    print()


# Driver code
if __name__ == '__main__':
    V=25
    graph1 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E','F'],
    'D': [],
    'E': [],
    'F': ['I'],
    'G': ['E','H'],
    'H': ['J'],
    'I': ['L','M','N'],
    'J': ['M','K','O'],
    'K': ['Q','R'],
    'L': ['S','T'],
    'M': [],
    'N': ['T'],
    'O': ['P'],
    'P': [],
    'Q': ['U'],
    'R': ['V'],
    'S': [],
    'T': ['U','V'],
    'U': ['W','X'],
    'V': ['X','Y'],
    'W': [],
    'X': [],
    'Y': []

    }





    # Display adjacency list
    print("Adjacency List: ")
    printList(graph1, V)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(graph1, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)

