#!/usr/bin/env python3

def is_valid_col(num, c, board):
    return num not in [board[i][c] for i in range(9)]

def is_valid_row(num, r, board):
    return num not in board[r]

def is_valid_quad(num, r, c, board):
    for row in range((r//3)*3, (r//3)*3+3):
        for col in range((c//3)*3, (c//3)*3+3):
            if num == board[row][col]:
                return False
    return True
    
def is_valid(num, r, c, board):
    if is_valid_col(num,c,board) and is_valid_row(num,r,board) and is_valid_quad(num,r,c,board):
        return True

def solve(board, zeroes):
    if not zeroes:
        return True
    r, c = zeroes.pop()
    for num in range(1, 10):
        if is_valid(num, r, c, board):
            board[r][c] = num
            if solve(board, zeroes):
                return True
    board[r][c] = 0
    zeroes.append((r,c))
    return False

def solveSudoku(board):
    zeroes = [(r,c) for r in range(9) for c in range(9) if board[r][c] == 0]
    solve(board, zeroes)
    return board
