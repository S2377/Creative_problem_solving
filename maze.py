

def path_exists(maze, i, j, visited):
    """
    Check if there exists a path in the maze from position (i,j) to the target
    
    Args:
        maze (List[List[int]]): 2D array representing the maze (0 is path, 1 is wall)
        i (int): current row position
        j (int): current column position
        visited (List[List[bool]]): 2D array tracking visited cells
    
    Returns:
        bool: True if path exists, False otherwise
    """
    # Base case: Check if out of bounds
    if not (0 <= i < len(maze) and 0 <= j < len(maze[0])):
        return False
    
    # Base case: Check if wall or already visited
    if maze[i][j] == 1 or visited[i][j]:
        return False
        
    # Mark current cell as visited
    visited[i][j] = True
    
    # Base case: Check if reached target (bottom-right corner)
    if i == len(maze)-1 and j == len(maze[0])-1:
        return True
    
    # Get all possible neighboring cells
    neighbors = [
        (i+1, j),  # down
        (i-1, j),  # up
        (i, j+1),  # right
        (i, j-1)   # left
    ]
    
    # Check each neighbor
    for next_i, next_j in neighbors:
        if path_exists(maze, next_i, next_j, visited):
            return True
    
    return False

def solve_maze(maze):
    """
    Wrapper function to initialize visited array and call path_exists
    
    Args:
        maze (List[List[int]]): 2D array representing the maze
    
    Returns:
        bool: True if path exists from start to end, False otherwise
    """
      
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    return path_exists(maze, 0, 0, visited)

# Example usage
def print_maze(maze):
    """Helper function to print the maze"""
    for row in maze:
        print(" ".join(map(str, row)))

# Test the maze solver
if __name__ == "__main__":
    # Example maze (0 represents path, 1 represents wall)
    maze = [
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 0]
    ]
    
    print("Maze layout:")
    print_maze(maze)
    
    result = solve_maze(maze)
    print("\nPath exists from start to end:", result)