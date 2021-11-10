import random

def init_board():
    board = [
            [ '.','.','.' ],
            [ '.','.','.' ],
            [ '.','.','.' ]
            ]
    return board

    


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
        print(coord)

#get_move()
#start_player()


def main():
    winner = False
    actual = start_player()
    while not winner:
        if actual == "X":
            actual = "O"
        else:
            actual = "X"
        print(actual)

#board print
#ask next coordinate
#check coord is emopty
#add to board
#check board is full or winner

                
        
        
    

main()
