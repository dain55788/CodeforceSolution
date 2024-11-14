def get_max_row(): 
    for i in range(n): 
        for j in range(n): 
            if board[i][j] > max_row[i]:
                max_row[i] = board[i][j]

def get_max_col(): 
    for i in range(n): 
        for j in range(n): 
            if board[j][i] > max_col[i]:
                max_col[i] = board[j][i]

def get_max_main_diag(): 
    for i in range(n):
        for j in range(n): 
            idx = i - j 
            if idx < 0: 
                idx += 2 * n - 1 
            if board[i][j] > max_main_diag[idx]: 
                max_main_diag[idx] = board[i][j]

def get_max_sub_diag(): 
    for i in range(n): 
        for j in range(n): 
            if board[i][j] > max_sub_diag[i + j]:
                max_sub_diag[i + j] = board[i][j]

def isQueen(x, y, n): 
    idx = (x - y)
    return (
            board[x][y] >= max_row[x] and 
            board[x][y] >= max_col[y] and 
            board[x][y] >= max_main_diag[idx] and 
            board[x][y] >= max_sub_diag[x + y]
    )

n = int(input())

board = []

for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

max_row = [0] * n 
max_col = [0] * n 
max_main_diag = [0] * (2 * n - 1) 
max_sub_diag = [0] * (2 * n - 1) 

get_max_row()
get_max_col()
get_max_main_diag()
get_max_sub_diag()

ans = 0

for i in range(n): 
    for j in range(n): 
        ans += isQueen(i, j, n) 

print(ans)