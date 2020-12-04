"""file to save the urls of the chess pieces and the image dictionary for the urls. We can organize this better in the future, and maybe store each piece's url in each pieces class."""

white_pawn = "https://i.ibb.co/K5NWnKw/chess-game-03-512.png"
black_pawn = "https://i.ibb.co/X4bPjyy/2-512.png"
black_rook = "https://i.ibb.co/mJ8wN23/777783-200.png" "https://i.ibb.co/ncsXVq1/queen-logo-chess-pawn-chess-piece-bishop-checkmate-rook-game-png-clipart.jpg"
white_rook = "https://i.ibb.co/v3SVSMy/checkmate-chess-figure-game-rook-icon-1320086877598773860.png"
white_knight = "https://i.ibb.co/ncm89tr/chess-chess-game-chess-knight-chess-piece-game-icon-knight-png-chess-512-512.png"
black_night ="https://i.ibb.co/d2r0NfP/chess-knight-icon-13.png"
white_bishop = "https://i.ibb.co/xGCLxsT/chess-game-04-512.png"
black_bishop = "https://i.ibb.co/gVw0Cgv/Bishop-512.png"
black_queen = "https://i.ibb.co/MnpGrFb/black-crown-icon-png-free-download-black-crown-png-500-500.png"
white_queen  ="https://i.ibb.co/g6K6DB6/crown.png"
white_king = "https://i.ibb.co/qp7ySHh/checkmate-chess-figure-game-king-icon-1320086877008120531.png"
black_king = "https://i.ibb.co/2qfPW5x/chess-king-icon-6.png"

#associate a space on the board with an image url to represent the piece
board = {'A7' : black_pawn, 'B7' : black_pawn, 'C7' : black_pawn, 'D7' : black_pawn, 'E7' : black_pawn, 'F7' : black_pawn, 'G7' : black_pawn, 'H7' : black_pawn, 'A2': white_pawn, 'B2': white_pawn, 'C2': white_pawn, 'D2': white_pawn, 'E2': white_pawn, 'F2': white_pawn, 'G2': white_pawn, 'H2': white_pawn, 'A8':black_rook, 'H8': black_rook, 'A1': white_rook, 'H1': white_rook, 'B8':black_night, 'G8': black_night, 'B1': white_knight, 'G1': white_knight, 'C8':black_bishop, 'F8':black_bishop, 'C1': white_bishop, 'F1': white_bishop, 'D8':black_queen, 'D1':white_queen, 'E1': white_king, 'E8': black_king }

#fill in the blank spaces on the board
for file in ["A", "B", "C", "D", "E", "F","G", "H"]:
    for rank in [1,2,3,4,5,6,7,8]:
        file_rank = file + str(rank)
        if(file_rank not in board):
            board[file_rank] = ""
