import random
import math


class Player:
    def __init__(self, letter) -> None:
        # letter X or O
        self.letter = letter


    # We want all players to get their next move 
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square



class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8)")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again")

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get best square position from minimax function
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 
            'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else  -1 * (
                state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            {'position': None, 'score': 0}        

        if player == max_player:
            best = {'position': None, 'score': -math.inf} 
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # Make a move, try the spot
            state.make_move(possible_move, player)

            # Recurse using the minimax to try the different spot
            sim_score = self.minimax(state, other_player)

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # Update the dictionary if necessary   
            # We are trying to Maximize the max_player and minimize the other player
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

            
             
    
