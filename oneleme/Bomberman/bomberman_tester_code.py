import queue

n, m, x_start, y_start, x_end, y_end = list(map(int, input().split()))
maze = []
for _ in range(n):
    maze.append(list(input()))

q = queue.Queue()
q.put([x_start, y_start])

memo = [[(float("inf"), float("inf")) for i in range(n)] for j in range(n)]
memo[x_start][y_start] = [0, 0]
ans = -1

LEFT = [-1, 0]
RIGHT = [1, 0]
UP = [0, 1]
DOWN = [0, -1]

def process_direction(maze, memo, q, curr_x, curr_y, dir):
    if 0 <= curr_x + dir[0] < len(maze) and 0 <= curr_y + dir[1] < len(maze[0]):
        x = curr_x + dir[0]
        y = curr_y + dir[1]
        prev = memo[curr_x][curr_y]
        if maze[x][y] == "." and (memo[curr_x][curr_y][1] + 1 < memo[x][y][1] or memo[curr_x][curr_y][0] < memo[x][y][0]):
            memo[x][y] = [prev[0], prev[1] + 1]
            q.put([x, y])
        elif maze[x][y] == "x" and (memo[curr_x][curr_y][1] + 1 < memo[x][y][1] or memo[curr_x][curr_y][0] + 1 < memo[x][y][0]):
            memo[x][y] = [prev[0] + 1, prev[1] + 1]
            q.put([x, y])


while not q.empty():
    curr_x, curr_y = q.get()
    if curr_x == x_end and curr_y == y_end and memo[curr_x][curr_y][0] <= m:
         ans = memo[curr_x][curr_y][1]
         break
    elif memo[curr_x][curr_y][0] <= m:
        process_direction(maze, memo, q, curr_x, curr_y, LEFT)
        process_direction(maze, memo, q, curr_x, curr_y, RIGHT)
        process_direction(maze, memo, q, curr_x, curr_y, UP)
        process_direction(maze, memo, q, curr_x, curr_y, DOWN)

print(memo[x_end][y_end][1]) if ans != -1 else print("Impossible")