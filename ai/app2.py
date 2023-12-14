from collections import deque

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()

def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start = None
    end = None

    # Find the start and end points
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start, 0)])  # Queue to store current position and cost
    visited = set()

    while queue:
        (current, cost) = queue.popleft()
        visited.add(current)

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited and maze[next_row][next_col] != 'X':
                if maze[next_row][next_col] == 'E':
                    return cost + 1  # We reached the end, return the cost
                queue.append(((next_row, next_col), cost + 1))

    return -1  # No path found

def dfs(maze):
    rows, cols = len(maze), len(maze[0])
    start = None
    end = None

    # Find the start and end points
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(start, 0)]  # Stack to store current position and cost
    visited = set()

    while stack:
        (current, cost) = stack.pop()
        visited.add(current)

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited and maze[next_row][next_col] != 'X':
                if maze[next_row][next_col] == 'E':
                    return cost + 1  # We reached the end, return the cost
                stack.append(((next_row, next_col), cost + 1))

    return -1  # No path found

if _name_ == "_main_":
    maze = [
        ['S', '.', '.', 'X', '.', 'X', '.', 'E'],
        ['.', 'X', '.', 'X', '.', 'X', '.', '.'],
        ['.', 'X', '.', '.', '.', '.', 'X', '.'],
        ['.', '.', '.', 'X', '.', '.', '.', '.'],
        ['.', 'X', '.', '.', '.', 'X', '.', '.']
    ]

    print("Maze:")
    print_maze(maze)

    bfs_cost = bfs(maze)
    if bfs_cost != -1:
        print(f"BFS Path Cost: {bfs_cost}")
    else:
        print("No path found for BFS")

    dfs_cost = dfs(maze)
    if dfs_cost != -1:
        print(f"DFS Path Cost: {dfs_cost}")
    else:
        print("No path found for DFS")



def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move
