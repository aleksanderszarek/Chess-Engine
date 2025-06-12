import chess
import random
import os
import secrets
class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.moves = []
        self.movecount = 1
        self.openings = [
            # 1. e4 Openings
            ["1. e4", "e5", "2. Nf3", "Nc6", "3. Bb5", "a6", "4. Ba4", "Nf6", "5. O-O", "Be7"],  # Ruy-Lopez (Closed)
            ["1. e4", "e5", "2. Nf3", "Nc6", "3. Bc4", "Bc5", "4. c3", "Nf6", "5. d4", "exd4"],  # Italian Game
            ["1. e4", "e5", "2. Nf3", "d6", "3. d4", "exd4", "4. Nxd4", "Nf6", "5. Nc3", "Be7"],  # Philidor Defense
            ["1. e4", "e5", "2. Nf3", "f5", "3. exf5", "e4", "4. Qe2", "d5", "5. d3", "Nf6"],     # Latvian Gambit
            ["1. e4", "c5", "2. Nf3", "d6", "3. d4", "cxd4", "4. Nxd4", "Nf6", "5. Nc3", "a6"],   # Sicilian Najdorf
            ["1. e4", "c5", "2. Nf3", "e6", "3. d4", "cxd4", "4. Nxd4", "a6", "5. Nc3", "Qc7"],   # Sicilian Kan
            ["1. e4", "e6", "2. d4", "d5", "3. Nc3", "Nf6", "4. e5", "Nfd7", "5. f4", "c5"],      # French Defense (Steinitz)
            ["1. e4", "c6", "2. d4", "d5", "3. Nc3", "dxe4", "4. Nxe4", "Nf6", "5. Nxf6+", "gxf6"],  # Caro-Kann Defense
            ["1. e4", "d6", "2. d4", "Nf6", "3. Nc3", "g6", "4. Nf3", "Bg7", "5. Be2", "O-O"],    # Pirc Defense
            ["1. e4", "g6", "2. d4", "Bg7", "3. Nc3", "d6", "4. f4", "Nf6", "5. Nf3", "O-O"],     # Modern Defense

            # 1. d4 Openings
            ["1. d4", "d5", "2. c4", "e6", "3. Nc3", "Nf6", "4. Bg5", "Be7", "5. e3", "O-O"],     # Queen's Gambit Declined
            ["1. d4", "Nf6", "2. c4", "e6", "3. Nf3", "b6", "4. g3", "Bb7", "5. Bg2", "Be7"],     # Queen's Indian Defense
            ["1. d4", "Nf6", "2. c4", "g6", "3. Nc3", "Bg7", "4. e4", "d6", "5. Nf3", "O-O"],     # King's Indian Defense
            ["1. d4", "Nf6", "2. c4", "e6", "3. Nc3", "Bb4", "4. e3", "O-O", "5. Nf3", "d5"],     # Nimzo-Indian Defense
            ["1. d4", "f5", "2. g3", "Nf6", "3. Bg2", "e6", "4. Nf3", "Be7", "5. O-O", "O-O"],    # Dutch Defense
            ["1. d4", "c5", "2. d5", "e5", "3. e4", "d6", "4. Nc3", "Be7", "5. Bd3", "Nf6"],      # Benoni Defense
            ["1. d4", "d6", "2. c4", "e5", "3. Nf3", "e4", "4. Nfd2", "f5", "5. Nc3", "Nf6"],     # Old Indian Defense
            ["1. d4", "d5", "2. Bf4", "Nf6", "3. e3", "e6", "4. Nf3", "Bd6", "5. Bg3", "O-O"],    # London System
            ["1. d4", "d5", "2. Nf3", "Nf6", "3. e3", "e6", "4. Bd3", "Be7", "5. O-O", "O-O"],    # Colle System
            ["1. d4", "Nf6", "2. c4", "c5", "3. d5", "e6", "4. Nc3", "exd5", "5. cxd5", "d6"],    # Benko Gambit

            # Other Openings
            ["1. c4", "e5", "2. Nc3", "Nf6", "3. g3", "d5", "4. cxd5", "Nxd5", "5. Bg2", "Nb6"],  # English Opening
            ["1. Nf3", "d5", "2. g3", "c5", "3. Bg2", "Nc6", "4. O-O", "e5", "5. d3", "Nf6"],     # Reti Opening
            ["1. f4", "d5", "2. Nf3", "Nf6", "3. g3", "g6", "4. Bg2", "Bg7", "5. O-O", "O-O"],    # Bird's Opening
            ["1. b3", "e5", "2. Bb2", "Nc6", "3. e3", "d5", "4. Bb5", "Bd6", "5. f4", "Qe7"],     # Larsen's Opening
            ["1. g3", "d5", "2. Bg2", "Nf6", "3. c4", "c6", "4. Nf3", "e6", "5. O-O", "Be7"],     # King's Fianchetto Opening
            ["1. b4", "e5", "2. a3", "d5", "3. Bb2", "Nd7", "4. e3", "Ngf6", "5. c4", "c6"],      # Polish Opening
            ["1. Nc3", "d5", "2. e4", "dxe4", "3. Nxe4", "Nf6", "4. Nxf6+", "gxf6", "5. d4", "c6"],  # Dunst Opening
            ["1. d3", "e5", "2. Nf3", "Nc6", "3. g3", "d5", "4. Bg2", "Nf6", "5. O-O", "Be7"],    # Mieses Opening
            ["1. h3", "e5", "2. a4", "d5", "3. e3", "Nf6", "4. b3", "Be7", "5. Bb2", "Nc6"],      # Clemenz Opening
            ["1. h4", "d5", "2. a4", "e5", "3. g3", "Nf6", "4. Bg2", "Be7", "5. d3", "O-O"],      # Anti-Borg Opening
        ]

        self.consideropenings = True
    def display(self):
        print(self.board)

    def move(self, move_str):
        try:
            if move_str is None or move_str.strip() == "":
                print("Invalid move format!")
                return False
            move = self.board.parse_san(move_str)
            if self.board.is_legal(move):
                self.board.push(move)
                return True
            else:
                print("Illegal move!")
                return False
        except ValueError:
            return False

    def play(self):
        while not self.board.is_checkmate() and not self.board.is_stalemate():
            self.display()

            if self.board.turn == chess.WHITE:
                move = input("Enter your move (e.g., e4): ")
                self.moves.append(f"{self.movecount}. {move}")
                self.movecount+=1
            else:
                move = self.get_computer_move()            
            if move is not None and self.move(move):
                if self.board.is_checkmate():
                    print("Checkmate!")
                    break
                elif self.board.is_stalemate():
                    print("Draw by stalemate!")
                    break
                elif self.board.can_claim_threefold_repetition():
                    print("Draw by threefold repetition!")
                elif self.board.can_claim_fifty_moves():
                    print("Draw by fifty moves rule!")
    def get_computer_move(self):
        legal_moves = list(self.board.legal_moves)
        playable_openings = []
        guard = 0
        if self.consideropenings:
            for opening in self.openings:
                guard = 0
                for i, move in enumerate(self.moves):
                    if move != opening[i]:
                        guard = 1
                        break
                if guard == 0:
                    playable_openings.append(opening)
            if playable_openings:
                opening = random.choice(playable_openings)
                move = opening[len(self.moves)]
                self.moves.append(move)
                return move
        if legal_moves:
            _evals = []
            moves = []
            for _move in legal_moves:
                _testboard = chess.Board(self.board.fen())
                _testboard.san(_move)
                _testboard.push(_move)
                evals = []
                lm = list(_testboard.legal_moves)
                for move in lm:
                    testboard = chess.Board(_testboard.fen())
                    testboard.san(move)
                    testboard.push(move)
                    whiteeval = 0
                    blackeval = 0
                    if testboard.is_into_check(move):
                        blackeval+=1.5
                    if testboard.is_checkmate():
                        blackeval+=999
                    for square in chess.SQUARES:
                        piece = testboard.piece_at(square)
                        if str(piece).upper() == str(piece):
                            ## White
                            try:
                                value = piece.piece_type
                            except:
                                value = 0
                            attacks = len(testboard.attacks(square))
                            pinned = testboard.is_pinned(chess.WHITE, square)
                            capture_value = 0
                            if testboard.piece_at(move.to_square) and testboard.piece_at(move.to_square).color == chess.WHITE:
                                capture_value = (testboard.piece_at(move.to_square)).piece_type
                            val =  value * 0.83 + attacks * 0.3 + capture_value
                            if pinned:
                                val *= 0.35
                            if testboard.turn == chess.WHITE:
                                val += attacks * 0.01
                            if piece:
                                whiteeval += val
                        else:
                            ## Black
                            try:
                                value = piece.piece_type
                            except:
                                value = 0
                            attacks = len(testboard.attacks(square))
                            pinned = testboard.is_pinned(chess.BLACK, square)
                            capture_value = 0
                            if testboard.piece_at(move.to_square) and testboard.piece_at(move.to_square).color == chess.WHITE:
                                capture_value = (testboard.piece_at(move.to_square)).piece_type
                            val =  value * 0.83 + attacks * 0.3 + capture_value
                            if pinned:
                                val *= 0.35
                            if testboard.turn == chess.BLACK:
                                val += attacks * 0.01
                            if piece:
                                blackeval += val
                            
                    evals.append(round(whiteeval-blackeval,3))
                _evals.append(sorted(evals,reverse=True)[0])
                moves.append(_move)
            print(_evals,moves)
            sevals = sorted(_evals)
            os.system('cls')
            self.moves.append(self.board.san(moves[_evals.index(sevals[0])]))
            for x in self.moves:
                print(x,end=" ")
            print(f"\nEval: {sevals[0]}")
            return self.board.push(moves[_evals.index(sevals[0])])

        else:
            print("No legal moves for computer! Stalemate!")
            return None 

if __name__ == "__main__":
    game = ChessGame()
    game.play()
