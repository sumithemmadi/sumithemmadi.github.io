def isQueenSafe(row, col, board):
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1
    return True


def doit(c, board):
    if c == n:
        ans.append(board[:])
        return
    for i in range(n):
        if isQueenSafe(i, c, board):
            board[i] = board[i][:c]+'Q'+board[i][c+1:]
            doit(c+1, board)
            board[i] = board[i][:c]+'.'+board[i][c+1:]


n = int(input("Enter the value of N for NXN Queens : "))

board = []
ans = []

board = ['.'*n for _ in range(n)]
doit(0, board)

j = 1

for board in ans:
    print(f'Solution - {j}')
    j += 1
    for i in range(n):
        print(board[i])
    print('\n')
