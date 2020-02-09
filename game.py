from enum import Enum

class WhitePiece(Enum):
    PAWN = "P"
    BISHOP = "B"
    KNIGHT = "N"
    ROOK = "R"
    QUEEN = "Q"
    KING = "K"

class BlackPiece(Enum):
    PAWN = "p"
    BISHOP = "b"
    KNIGHT = "n"
    ROOK = "r"
    QUEEN = "q"
    KING = "k"

def displayGenerator(row):
    for piece in row:
        if piece == None:
            yield ' '
        else:
            yield piece.value

def intGenerator(row):
    for piece in row:
        if piece == None:
            yield 0
        elif piece.value == "P":
            yield 1
        elif piece.value == "B":
            yield 2
        elif piece.value == "N":
            yield 3
        elif piece.value == "R":
            yield 4
        elif piece.value == "Q":
            yield 5
        elif piece.value == "K":
            yield 6
        elif piece.value == "p":
            yield -1
        elif piece.value == "b":
            yield -2
        elif piece.value == "n":
            yield -3
        elif piece.value == "r":
            yield -4
        elif piece.value == "q":
            yield -5
        elif piece.value == "k":
            yield -6

def floatGenerator(row):
    for piece in intGenerator(row):
        yield piece / 6

# to be implemented
def validMoves(rowIdx, colIdx):
    pass
    if board[rowIdx][colIdx] == BlackPiece.PAWN:
        pass

if __name__ == "__main__":
    board = [[None] * 8] * 8
    board[0] = [WhitePiece.ROOK, WhitePiece.KNIGHT, WhitePiece.BISHOP, WhitePiece.QUEEN, WhitePiece.KING, WhitePiece.BISHOP, WhitePiece.KNIGHT, WhitePiece.ROOK]
    board[1] = [WhitePiece.PAWN] * 8
    board[6] = [BlackPiece.PAWN] * 8
    board[7] = [BlackPiece.ROOK, BlackPiece.KNIGHT, BlackPiece.BISHOP, BlackPiece.QUEEN, BlackPiece.KING, BlackPiece.BISHOP, BlackPiece.KNIGHT, BlackPiece.ROOK]
    for i in range(8).__reversed__():
        print([piece for piece in displayGenerator(board[i])])
    