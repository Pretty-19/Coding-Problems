import os
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def header():
    print("""
 _____  _  ____     _____  ____  ____     ______  ___  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \     
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\
  """)


def print_board():
    print("    |    |   ")
    print("  " + board[1] + " | " + board[2] + "  | " + board[3] + " ")
    print("    |    |   ")
    print("----|----|----")

    print("    |    |   ")
    print("  " + board[4] + " | " + board[5] + "  | " + board[6] + " ")
    print("    |    |   ")
    print("----|----|----")

    print("    |    |   ")
    print("  " + board[7] + " | " + board[8] + "  | " + board[9] + " ")
    print("    |    |   ")




os.system("clear")
header()
print_board()
print("\n")

while True:
    print("Please enter number of the box to fill for X: ")
    choice = int(input())
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("space is not empty")
        time.sleep(1)

    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
            (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
            (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
            (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
            (board[3] == "X" and board[5] == "X" and board[7] == "X") or \
            (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
            (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
            (board[3] == "X" and board[6] == "X" and board[9] == "X"):
        print("Winning move")
        print_board()
        print("X wins the game")
        break
    print_board()

    print("Please enter number of the box to fill for O: ")
    choice = int(input())
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("space is not empty")
        time.sleep(1)

    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
            (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
            (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
            (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
            (board[3] == "O" and board[5] == "O" and board[7] == "O") or \
            (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
            (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
            (board[3] == "O" and board[6] == "O" and board[9] == "O"):
        print("Winning move")
        print_board()
        print("O wins the game")
        break

    print_board()

