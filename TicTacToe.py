import random

def init_board():
    game_board = [
            [ '.','.','.' ],
            [ '.','.','.' ],
            [ '.','.','.' ]
            ]
    return game_board




def start_player(player1, player2):
    player1 == "X"
    player2 == "O"
    startplayer = random.randint(1,2)

    if startplayer == 1:
        print(f"Player One: {player1} will start the game.")    
    else:
        startplayer == 2

    if startplayer == 2:
        print(f"Player One: {player2} will start the game.")    
    else:
        startplayer == 1