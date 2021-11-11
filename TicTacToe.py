import random

def init_board():
    board = [
            [ '.','.','.' ],
            [ '.','.','.' ],
            [ '.','.','.' ]
            ]
    return board


def print_board(board):
    print(f"  1   2   3\nA {' | '.join(board[0])}\n ---+---+---\nB {' | '.join(board[1])}\n ---+---+---\nC {' | '.join(board[2])}")


def start_player():
    player1 = "X"
    player2 = "O"
    startplayer = random.randint(1,2)

    if startplayer == 1:
        print(f"Player One: {player1} will start the game.")  

        return "X"  
    
    if startplayer == 2:
        print(f"Player One: {player2} will start the game.") 

        return "O"
       
    
def get_move():
    coord = ()
    while len(coord) == 0:
        turn = input("Please give a valid coordinate! ").upper()
        if turn == "A1":
            coord = [0,0]
        elif turn == "A2":            
            coord = [0,1]
        elif turn == "A3":
            coord = [0,2]
        elif turn == "B1":
            coord = [1,0]
        elif turn == "B2":
            coord = [1,1]
        elif turn == "B3":
            coord = [1,2]
        elif turn == "C1":
            coord = [2,0]
        elif turn == "C2":
            coord = [2,1]
        elif turn == "C3":
            coord = [2,2]
        else:
            print("This is not a valid coordinate! Please give a valid coordinate! ")
    return coord


def won(board):
    solution = [

        [board[0][0], board[0][1], board[0][2]],  #row
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        
        [board[0][0], board[1][0], board[2][0]],  #col
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],

        [board[0][0], board[1][1], board[2][2]],  #keresztbe
        [board[2][0], board[1][1], board[0][2]],
        
         ]

    if ["X", "X", "X"] in solution or ["O", "O", "O"] in solution:
        return True

    else:
        return False    


def is_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    return True


def new_game():
    #while 
    nxt =input("Do you want to play again? (Y/N): ").upper()
    if nxt in ["Y"]:
        main()
    elif nxt in ["N"]:
        print("Good bye, brother!")     
        quit()
    else:
        print("Enter a correct input! ")


def win_case(actual):
    print(f"Player {actual} won the game!")   


def main():
    print("""
    
  _______            __                   __           
 /_  __(_)____      / /_____ ______      / /_____  ___ 
  / / / / ___/_____/ __/ __ `/ ___/_____/ __/ __ \/ _ \\
 / / / / /__/_____/ /_/ /_/ / /__/_____/ /_/ /_/ /  __/
/_/ /_/\___/      \__/\__,_/\___/      \__/\____/\___/ 
    
    """)
    print("""Welcome!
    
    """)
    print("""If you want to leave... never mind you can't. 
    You have to play with this (˘ε˘)
    
    """)
    board = init_board()
    actual = start_player()
    while not is_full(board):
        if clear_board(board):
            print_board(board)
            move = get_move()
            if board [move [0]][move[1]] == ".":
                board [move [0]][move[1]] = actual
                print_board(board)
            else:
                continue
            if actual == "X":
                print("Next player: O ")
                actual = "O"
            else:
                print("Next player: X ")
                actual = "X"
        else:
            move = get_move()
            if board [move [0]][move[1]] == ".":
                board [move [0]][move[1]] = actual
                print_board(board)
                if won(board):
                    win_case(actual)
                    new_game()
                    break
                else:
                    if actual == "X":
                        print("Next player: O ")
                        actual = "O"
                    else:
                        print("Next player: X ")
                        actual = "X"
            else:
                continue
def clear_board(board):
    fields = [

        board[0][0], board[0][1], board[0][2],  #row
        board[1][0], board[1][1], board[1][2],
        board[2][0], board[2][1], board[2][2],

        board[0][0], board[1][0], board[2][0],  #col
        board[0][1], board[1][1], board[2][1],
        board[0][2], board[1][2], board[2][2],

        board[0][0], board[1][1], board[2][2],  #keresztbe
        board[2][0], board[1][1], board[0][2],

         ]
    if "X" not in fields and "O" not in fields:
        return True
    else:
        return False

        
 
        
                
        
if __name__ == '__main__':
    main()
