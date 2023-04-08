from socket import *
from tictactoe import *


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('접속이 확인되었습니다.')


while True:
    Game_Board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Me = 'X'
    You = 'O'
    time = 9
    turn = 0
    while True:
        if turn == 0:
            pick = player_choose(Game_Board)
            Game_Board[pick] = Me
            time -= 1
            show_board(Game_Board)
            clientSock.send(str(pick).encode('utf-8'))
            if board_check(Game_Board) == Me:  # 사용자가 승리한 경우
                print("승리!!!")
                break
            elif time == 0:  # 무승부인 경우
                print("무승부!!!")
                break
            else:
                turn = 1  # 컴퓨터의 차례

        else:
            print('상대방이 입력 중입니다.')
            data = clientSock.recv(1024)
            Game_Board[int(data.decode('utf-8'))] = You
            turn = 0
            time -= 1
            if board_check(Game_Board) == You:  # 컴퓨터가 승리한 경우
                show_board(Game_Board)
                print("패배!!!")
                break
            else:
                turn = 0  # 사용자의 차례

    break

print("Bye~!")