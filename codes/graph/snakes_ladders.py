from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[n * n]

"""
This problem can be solved using Breadth First Search (BFS) algorithm to find the shortest path from square 1 to square n^2. 

First, we need to convert the given board into a linear 1D array, where each index represents a square on the board. We can use a helper function to convert the 2D board into a 1D array.

Then, we create a queue to store the squares that we need to visit, and a visited array to keep track of the squares that have been visited.

We start by adding square 1 to the queue and marking it as visited. Then we enter a while loop, where we process each square in the queue. For each square, we check if it is the destination square n^2. If it is, we return the distance we have traveled.

Otherwise, we generate the possible next squares that we can move to. If the next square does not have a snake or ladder, we add it to the queue and mark it as visited with the distance increased by 1.

If the next square has a snake or ladder, we find the destination of the snake or ladder and add it to the queue if it has not been visited before, with the distance increased by 1.

If we have visited all the squares and have not found the destination square n^2, we return -1.

Here is the code implementation for the above approach:

```python
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = self.convertTo1D(board, n)
        visited = [False] * (n * n + 1)
        
        q = deque([(1, 0)]) # (square, distance)
        visited[1] = True
        
        while q:
            curr, dist = q.popleft()
            
            if curr == n * n:
                return dist
            
            for i in range(curr + 1, min(curr + 6, n * n) + 1):
                if not visited[i]:
                    visited[i] = True
                    
                    if cells[i] == -1:
                        q.append((i, dist + 1))
                    else:
                        q.append((cells[i], dist + 1))
        
        return -1
    
    def convertTo1D(self, board: List[List[int]], n: int) -> List[int]:
        cells = [0] * (n * n + 1)
        label = 1
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                for j in range(n):
                    cells[label] = board[i][j]
                    label += 1
            else:
                for j in range(n - 1, -1, -1):
                    cells[label] = board[i][j]
                    label += 1
        return cells
```

The time complexity of this solution is O(n^2), where n is the size of the board. We need to convert the board into a 1D array in O(n^2) time, and perform a BFS on the board in the worst case, visiting all the squares. The space complexity is O(n^2) for storing the visited array and the queue.
"""