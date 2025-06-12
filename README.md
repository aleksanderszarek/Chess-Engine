# Chess Engine

## Installation:

1. Install Python (https://www.python.org/downloads/) with PATH.
2. Restart your computer.
3. On your terminal, run `pip install chess`.
4. Run main.py by double-clicking the file.

## Usage:

1. Run main.py by double-clicking the file.
2. Game moves will appear at the top of the page.
3. Below them, game eval will appear. The higher the eval is, the better the position is for you according to the computer.
4. Below that, the game state will appear. It is represented by a matrix consisting of characters. Each character represents one position on the board. '.' represents empty position, Big letters represent white pieces, small - black pieces:

- P/p - pawn
- B/b - bishop
- N/n - knight
- R/r - rook
- Q/q - queen
- K/k - king

5. You will need to type your move in an algebraic notation (eg. e4, Kxg3, exf8=Q, O-O)
6. After typing your move, the computer will re-evaluate the position and try selecting the best move on the board. New board will appear.
7. The game will end with a win for one side (checkmate) or a draw (three-fold repetition, stalemate or 50-moves rule). Appropriate message will appear on the screen.
