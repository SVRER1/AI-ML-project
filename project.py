from collections import deque

def bfs(grid, start, goal):
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node == goal:
            return "Goal Found"
        
        if node not in visited:
            visited.add(node)
            x, y = node
            
            moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for move in moves:
                if move not in visited:
                    queue.append(move)

grid = [[0]*5 for _ in range(5)]
print(bfs(grid, (0,0), (4,4)))