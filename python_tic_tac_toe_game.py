win = 0

def print_board():
    print (empty_board[:3])
    print (empty_board[3:6])
    print (empty_board[6:])
    
def player_one():
    move = int(raw_input("\nPlayer One, choose where you want your token to go: \n"))
    empty_board[move-1] = tokens['player_1']
    print_board()
    
def player_two():
    move2 = int(raw_input("\nPlayer Two, choose where you want your token to go: \n"))
    empty_board[move2-1] = tokens['player_2']
    print_board()
    
def check_one():
    if empty_board[0] == empty_board[1] == empty_board[2] == 'X' or empty_board[3] == empty_board[4] == empty_board[5] == 'X' or empty_board[6] == empty_board[7] == empty_board[8] == 'X' or empty_board[0] == empty_board[3] == empty_board[6] == 'X' or empty_board[1] == empty_board[4] == empty_board[7] == 'X' or empty_board[2] == empty_board[5] == empty_board[8] == 'X':
        win = 1
        print ("!!!Game Over!!!!!!")
        print ("Player 1 Won")
    else:
        pass
    
def check_two():
    if empty_board[0] == empty_board[1] == empty_board[2] == 'X' or empty_board[3] == empty_board[4] == empty_board[5] == 'X' or empty_board[7] == empty_board[8] == empty_board[9] == 'X' or empty_board[0] == empty_board[3] == empty_board[6] == 'X' or empty_board[1] == empty_board[4] == empty_board[7] == 'X' or empty_board[2] == empty_board[5] == empty_board[8] == 'X':
        win = 1
        print ("!!!Game Over!!!!!!")
        print ("Player 2 Won")
    else:
        pass
    
def play():
    while win !=1:
        player_one()
        check_one()
    
        if win !=0:
            break
        else:
            player_two()
            check_two()
  
    
    
     
empty_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

sample_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tokens = {'player_1': 'X', 'player_2': 'O'}

print ("\nLet's Play TicTacToe!\nHere are the rules:\n....................\n")

print (sample_board[:3])
print (sample_board[3:6])
print (sample_board[6:])
print (" ")

choose_token = raw_input(" Player One, Choose your token ( X / O ): ")
tokens['player_1'] = choose_token

print ("Player One, your token is " + tokens['player_1'])
print ("Player Two, your token is " + tokens['player_2'])

print ("\nLet's start!\n")
print_board()
# check
player_one()

player_two()

player_one()

player_two()

print (tokens['player_1'])
print (tokens['player_2'])
