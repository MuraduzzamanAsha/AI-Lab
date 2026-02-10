import heapq

# Board type: tuple of tuples (hashable)
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

goal_pos = {}

def goal_map():
    for i in range(3):
        for j in range(3):
            goal_pos[GOAL[i][j]] = (i, j)

def calculate_manhattan(board):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                gi, gj = goal_pos[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_8_puzzle(start):
    # Priority Queue: (f, g, board)
    pq = []

    visited = {}          # board -> min g
    parent = {}           # board -> previous board

    start_h = calculate_manhattan(start)
    start_g = 0
    start_f = start_g + start_h

    heapq.heappush(pq, (start_f, start_g, start))
    visited[start] = start_g

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        f, current_g, current_board = heapq.heappop(pq)

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
                print("------")
            return

        x, y = find_blank(current_board)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                # Convert to list to swap
                new_board = [list(row) for row in current_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                new_board = tuple(tuple(row) for row in new_board)

                new_g = current_g + 1

                if new_board not in visited or new_g < visited[new_board]:
                    visited[new_board] = new_g
                    new_h = calculate_manhattan(new_board)
                    new_f = new_g + new_h

                    heapq.heappush(pq, (new_f, new_g, new_board))
                    parent[new_board] = current_board

    print("Unsolvable puzzle.")

if __name__ == "__main__":
    start_board = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    goal_map()
    print("Starting 8-Puzzle Solver...\n")
    solve_8_puzzle(start_board)
