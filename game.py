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


if __name__ == "__main__":
    board = [[None] * 8] * 8
    board[0] = [WhitePiece.ROOK, WhitePiece.KNIGHT, WhitePiece.BISHOP, WhitePiece.QUEEN, WhitePiece.KING, WhitePiece.BISHOP, WhitePiece.KNIGHT, WhitePiece.ROOK]
    board[1] = [WhitePiece.PAWN] * 8
    board[6] = [BlackPiece.PAWN] * 8
    board[7] = [BlackPiece.ROOK, BlackPiece.KNIGHT, BlackPiece.BISHOP, BlackPiece.QUEEN, BlackPiece.KING, BlackPiece.BISHOP, BlackPiece.KNIGHT, BlackPiece.ROOK]
    for i in range(8).__reversed__():
        print([piece for piece in displayGenerator(board[i])])
    