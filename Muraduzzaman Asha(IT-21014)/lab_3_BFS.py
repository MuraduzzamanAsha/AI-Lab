from collections import deque

# Goal state (tuple of tuples so it is hashable)
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_8_puzzle(start):
    # Queue for BFS: (moves, board)
    q = deque()
    visited = {}          # board -> moves
    parent = {}           # board -> previous board

    q.append((0, start))
    visited[start] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        current_g, current_board = q.popleft()

        # Goal check
        if current_board == GOAL:
            print(f"Goal Reached in {current_g} moves!\n")

            # Reconstruct path
            path = []
            curr = GOAL
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            path.reverse()

            for step in path:
                for row in step:
                    print(*row)
                print()
            return

        x, y = find_blank(current_board)

        # Generate moves
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                # Convert to list for swapping
                new_board = [list(row) for row in current_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                new_board = tuple(tuple(row) for row in new_board)

                if new_board not in visited:
                    visited[new_board] = current_g + 1
                    parent[new_board] = current_board
                    q.append((current_g + 1, new_board))

    print("Unsolvable puzzle.")

if __name__ == "__main__":
    start_board = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    print("Starting 8-Puzzle Solver...\n")
    solve_8_puzzle(start_board)
