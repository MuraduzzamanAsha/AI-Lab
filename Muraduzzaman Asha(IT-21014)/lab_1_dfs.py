from collections import deque

GOAL_STATE = ((1,2,3),(4,5,6),(7,8,0))

def find_blank(puzzle):
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
    return -1, -1

def get_possible_moves(puzzle):
    moves = []
    x, y = find_blank(puzzle)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            puzzle_list = [list(row) for row in puzzle]
            puzzle_list[x][y], puzzle_list[nx][ny] = puzzle_list[nx][ny], puzzle_list[x][y]
            moves.append(tuple(tuple(row) for row in puzzle_list))
    return moves

def dfs_8_puzzle(start, goal, limit=50):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (state, path) = stack.pop()
        if state == goal:
            return path
        if len(path) > limit:  
            continue
        visited.add(state)
        for move in get_possible_moves(state):
            if move not in visited:
                stack.append((move, path + [move]))
    return None

initial_state = ((1,2,3),(4,0,6),(7,5,8))  
solution_path = dfs_8_puzzle(initial_state, GOAL_STATE, limit=30)

if solution_path:
    print("Solution found in", len(solution_path)-1, "moves!")
    for step in solution_path:
        for row in step:
            print(row)
        print("-"*6)
else:
    print("No solution found within depth limit.")
