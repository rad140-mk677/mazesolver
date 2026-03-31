A-Maze-Solver A Maze Solver: Pathfinding Visualizer* Welcome to the A Maze Solver*, a Python project that turns pathfinding logic into a clean, visual experience. This tool uses the A* (A-Star) algorithm to navigate a grid-based maze, dodging obstacles to find the most efficient route from start to finish.

How It Works

The solver doesn't just guess; it calculates. It uses a Heuristic function to evaluate the best next move: • g(n): The actual cost from the start to the current tile. • h(n): The estimated distance to the goal (Manhattan distance). By prioritizing the lowest total cost (f(n) = g(n) + h(n)), the algorithm "thinks" ahead, exploring the most promising paths first.

Key Features

* Efficient Search: Powered by Python’s heap for fast priority queue management. • Visual Storytelling: Uses Matplotlib to create a high-contrast map. • Smart Logic: Checks four directions (Up, Down, Left, Right) while respecting boundaries and walls.

Map Legend

* Red / Green: The Start and the Goal. • Blue: Impassable Walls. • Yellow: Areas the algorithm explored. • White Outline: The final, optimal path found.

Getting Started

Ensure you have NumPy and matplotlib installed. Run the script to see the pathfinder in action. Feel free to modify the maze array to create your own custom challenges!# mazesolver
