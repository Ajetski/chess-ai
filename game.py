import chess

board = chess.Board()

print(board)
print()

#test out board.legal_moves
for move in board.legal_moves:
    print(move)
    board.push(move)
    print(board)
    board.pop()
    print()
