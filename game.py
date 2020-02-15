import chess
import numpy as np
from tensorflow import keras
import time
from collections import deque

def arrayify(board):
    myBoard = np.empty([8, 8], dtype=np.float64)

    #myBoard = [[0 for i in range(8)] for j in range(8)]
    row = 0
    col = 0

    for c in str(board):
        if c != ' ' and c != '\n':
            value = None
            if c == '.':
                value = 0
            elif c == 'P' or c == 'p':
                value = 1
            elif c == 'B' or c == 'b':
                value = 2
            elif c == 'R' or c == 'r':
                value = 3
            elif c == 'N' or c == 'n':
                value = 4
            elif c == 'Q' or c == 'q':
                value = 5
            elif c == 'K' or c == 'k':
                value = 6
            if c >= 'a' and c <= 'z':
                value *= -1
            value /= 6
            myBoard[row][col] = value
            col += 1
            if col == 8:
                row += 1
                col = 0
    return myBoard


def model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(8, 8)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(8, activation='relu'),
        keras.layers.Dense(4, activation='relu'),
        keras.layers.Dense(4, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam',
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

    return model

def play_game(model1, model2):
    board = chess.Board()
    stack1 = deque()
    stack2 = deque()
    num_moves = 0
    while not board.is_game_over():
        best_move_precentage = 0
        save_move = None
        best_move = None
        for move in board.legal_moves:
            if board.turn:
                board.push(move)
                current_move = model1.predict(np.array([arrayify(board)]))[0][2]
                if current_move > best_move_precentage:
                    best_move_precentage = current_move
                    save_move = arrayify(board)
                    best_move = move
                board.pop()
            else:
                board.push(move)
                current_move = model2.predict(np.array([arrayify(board)]))[0][2]
                if current_move > best_move_precentage:
                    best_move_precentage = current_move
                    save_move = arrayify(board)
                    best_move = move
                board.pop()
        if board.turn:
            stack1.append(save_move)
        else:
            stack2.append(save_move)
        board.push(best_move)
        num_moves += 1
    print("\nfinal state: ")
    print(board)
    print(board.turn)
    print(num_moves)
    array1 = np.empty((len(stack1), 8, 8), dtype=float)
    array2 = np.empty((len(stack2), 8, 8), dtype=float)
    if board.is_checkmate():
        if board.turn:
            pass
            #train model 1 and 2 that stack1 are wins
            #train model 1 and 2that stack2 are losses
        else:
            pass
            #train model 1 and 2 that stack1 are losses
            #train model 1 and 2 that stack2 are wins
    else:
        pass
        # train model 1 and 2 that stack 1 and 2 are stalemates
    keras.models.save_model(model1, 'model1.hd5')
    keras.models.save_model(model2, 'model2.hd5')
    print("saved models")

if __name__ == "__main__":
    board = chess.Board()

    # input to model:
    # (8,8) 2d array of board data
    # (n,) 1d array of categories
    # 0 = loss, 1 = tie, 2 = win
    model1 = None
    model2 = None
    try:
        model1 = keras.models.load_model('model1.hd5')
        model2 = keras.models.load_model('model2.hd5')
        print("models loaded")
    except:
        print("error, creating new models")
        model1 = model()
        model1.fit(np.array([arrayify(board)]), np.array([1]))

        model2 = model()
        model2.fit(np.array([arrayify(board)]), np.array([1]))

    board = play_game(model1, model2)

    #while True:
        #play_game(model1, model2)
        # train model on data returned
        #time.sleep(2)



