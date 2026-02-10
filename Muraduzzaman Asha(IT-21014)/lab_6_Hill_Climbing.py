GOAL = ((1,2,3),(4,5,6),(7,8,0))

goal_pos = {GOAL[i][j]:(i,j) for i in range(3) for j in range(3)}

def manhattan(b):
    return sum(
        abs(i-goal_pos[b[i][j]][0]) + abs(j-goal_pos[b[i][j]][1])
        for i in range(3) for j in range(3) if b[i][j]!=0
    )

def find_blank(b):
    for i in range(3):
        for j in range(3):
            if b[i][j]==0: return i,j

def print_board(b):
    for r in b: print(*r)
    print()

def hill_climbing(start):
    cur = start
    h = manhattan(cur)
    moves = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    print(f"Initial (h={h})")
    print_board(cur)

    while h!=0:
        x,y = find_blank(cur)
        best, best_h = None, 10**9

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<3 and 0<=ny<3:
                nb = [list(r) for r in cur]
                nb[x][y], nb[nx][ny] = nb[nx][ny], nb[x][y]
                nb = tuple(tuple(r) for r in nb)
                nh = manhattan(nb)
                if nh < best_h:
                    best, best_h = nb, nh

        if best_h < h:
            cur, h = best, best_h
            moves += 1
            print(f"Move {moves} (h={h})")
            print_board(cur)
        else:
            print("Stuck at Local Maximum → Failure")
            return

    print(f"Goal Reached in {moves} moves!")

start = ((1,2,3),(4,0,6),(7,5,8))
hill_climbing(start)
