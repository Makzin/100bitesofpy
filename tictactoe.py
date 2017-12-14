import os
import pdb
import random
import time

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_LINES = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] + [[1, 4, 7], [2, 5, 8], [3, 6, 9]] + [[1, 5, 9], [3, 5, 7]]
FIRST_TURN = ['Player', 'Computer', 'Choose']

def prompt(input):
    print("==> %s" %input)

def display_board(board, playerScore, computerScore, current_player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You're %s. Computer is %s" % (PLAYER_MARKER, COMPUTER_MARKER))
    print("Player score is %s, Computer score is %s" %(playerScore, computerScore))
    print("5 points required to win!")
    print("      |       |")
    print("  %s   |   %s   |   %s   " %(board[1], board[2], board[3]))
    print("      |       |")
    print("------+-------+-------")
    print("      |       |")
    print("  %s   |   %s   |   %s   " % (board[4], board[4], board[6]))
    print("      |       |")
    print("------+-------+-------")
    print("      |       |")
    print("  %s   |   %s   |   %s   " % (board[7], board[8], board[9]))
    print("")
    print("")
    print("")
    print(" ------------------------- ")
    print("    %s's turn!    " %current_player)
    print(" ------------------------- ")


def initialize_board():
    new_board = {}
    for num in range(1,10):
        new_board[num] = INITIAL_MARKER
    return new_board


def empty_squares(board):
    emptySquares = list(filter(lambda num: board[num] == INITIAL_MARKER, board))
    return emptySquares


def joinor(list, delimiter=', ', word='or'):
    list[-1] = ('%s %s' % (word, list[-1]))
    delimList = delimiter.join(list)
    options = {
        0: '',
        1: list[0],
        2: (' %s ' %word).join(list)
        }
    return options.get(len(list), delimList)

def detect_next_best_square(line, board, marker):
    boardValues = list(board[num] for num in line)
    if boardValues.count(marker) == 2:
        nextSquare = list(filter(lambda k, v:
                                 k in line and v == INITIAL_MARKER, line))
        return next(iter(nextSquare))


def player_places_piece(board):
    while True:
        prompt('Choose a square %s' %(joinor(empty_squares(board))))
        square = int(input())
        if square in empty_squares(board):
            break
        prompt('Sorry, invalid choice')
    board[square] = PLAYER_MARKER

def computer_places_piece(board):
    global square
    if board[5] == INITIAL_MARKER:
        square = 5
    else:
        for line in WINNING_LINES:
            square = detect_next_best_square(line, board, COMPUTER_MARKER)
            if square:
                break
            square = detect_next_best_square(line, board, PLAYER_MARKER)
            if square:
                break
            square = random.sample(empty_squares(board), 1)[0]
    board[square] = COMPUTER_MARKER


def place_piece(board, currentPlayer):
    if currentPlayer == 'Computer':
        computer_places_piece(board)
    else:
        player_places_piece(board)
#
# def alternate_player(currentPlayer):
#
# def checkIfBoardFull(board):
#
# def someoneWon(board):
#
# def detect_winner(board):
#
# def new_game(board):

def mainGame():
    while True:
        currentPlayer = random.sample(FIRST_TURN, 1)[0]
        computerScore = 0
        playerScore = 0
        if (currentPlayer == 'Choose'):
            while True:
                prompt('Please choose who should go first (Player/ Computer).')
                answer = input()
                if (answer.lower().startswith('p')):
                    currentPlayer = 'Player'
                    break
                elif (answer.lower().startswith('c')):
                    currentPlayer = 'Computer'
                    break
                else:
                    prompt("I'm sorry, that's not a valid choice. Please try again")
        while True:
            board = initialize_board()
            while True:
                display_board(board,playerScore, computerScore, currentPlayer)
                if (currentPlayer == 'Computer'):
                    time.sleep(1)
                place_piece(board, currentPlayer)



mainGame()