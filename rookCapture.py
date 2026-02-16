def white_rook_can_capture(rook, board):
    can_capture = []
    for square in board.keys():
        piece = board[square]
        if piece[0] == 'b' and (square[0] == rook[0] or square[1] == rook[1]):
            can_capture.append(square)
    return can_capture
print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))