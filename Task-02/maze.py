import random
from collections import deque

# Maze dimensions (must be odd numbers for proper walls/paths)
ROWS, COLS = 11, 11

# Generate maze using DFS
def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]  # 1 = wall, 0 = path

    def carve_path(r, c):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows and 0 < nc < cols and maze[nr][nc] == 1:
                maze[nr][nc] = 0
                maze[r + dr // 2][c + dc // 2] = 0
                carve_path(nr, nc)

    # Start from (1,1)
    maze[1][1] = 0
    carve_path(1, 1)
    return maze

# Solve maze using BFS
def solve_maze(maze, start=(1, 1), end=None):
    rows, cols = len(maze), len(maze[0])
    if not end:
        end = (rows - 2, cols - 2)

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    # Reconstruct path
    path = []
    node = end
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    return path

# Print maze with path
def print_maze(maze, path=None):
    path = set(path or [])
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            if (r, c) in path:
                row_str += "* "
            else:
                row_str += ("# " if maze[r][c] == 1 else "  ")
        print(row_str)

# Main program
maze = generate_maze(ROWS, COLS)
path = solve_maze(maze)

print("Generated Maze:")
print_maze(maze)
print("\nMaze with Solution Path:")
print_maze(maze, path)
