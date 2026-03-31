import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

maze = np.array([
    [0,0,0,1,0,0,0,1,0,0],
    [1,1,0,1,0,1,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,1],
    [0,1,1,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,1,1,0],
    [1,1,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,1,0,1,1,0],
    [0,1,1,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,1],
    [0,0,0,0,0,1,0,0,0,0]
])

start = (0, 0)
goal = (9, 9)

rows, cols = maze.shape

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node):
    x, y = node
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    result = []
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
            result.append((nx, ny))
    return result

def astar():
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}
    visited = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited

        for nb in neighbors(current):
            temp_g = g_score[current] + 1

            if nb not in g_score or temp_g < g_score[nb]:
                g_score[nb] = temp_g
                f = temp_g + h(nb, goal)

                heapq.heappush(open_list, (f, nb))
                came_from[nb] = current

                visited[nb] = (temp_g, h(nb, goal))

    return None, visited

path, visited = astar()

#  Color Grid (black background)
color_grid = np.zeros((rows, cols, 3))

# walls = blue
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 1:
            color_grid[i][j] = [0, 0, 1]

# explored = yellow
for (i, j) in visited:
    color_grid[i][j] = [1, 1, 0]

# start & goal
color_grid[start] = [1, 0, 0]   # 
color_grid[goal] = [0, 1, 0]    # 

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(color_grid)

# Grid lines (clean look)
for i in range(rows):
    for j in range(cols):
        ax.add_patch(
            plt.Rectangle((j-0.5, i-0.5), 1, 1,
                          fill=False, edgecolor='gray', linewidth=0.5)
        )

# Path outline
if path:
    for (i, j) in path:
        ax.add_patch(
            plt.Rectangle((j-0.5, i-0.5), 1, 1,
                          fill=False, edgecolor='white', linewidth=2)
        )

# Legend (OUTSIDE)
legend_elements = [
    Patch(facecolor='blue', label='Wall'),
    Patch(facecolor='yellow', label='Explored'),
    Patch(facecolor='black', label='Unvisited'),
    Patch(facecolor='red', label='Start'),
    Patch(facecolor='green', label='Goal')
]

ax.legend(
    handles=legend_elements,
    loc='center left',
    bbox_to_anchor=(1, 0.5)
)

ax.set_title("A* Maze Solver (Clean UI)")
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
