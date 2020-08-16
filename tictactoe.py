import random


def draw_board(board):
    # функция выводит игровое поле
    # board - список из 10 строк, 0 строка игнорируется
    print()
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print('---+---+---')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print('---+---+---')
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print()


def choice_symbol():
    # функция предлагает выбрать знак
    print('Выберите знак: x или o')
    symbol = '*'
    while symbol not in 'xo':
        symbol = input().lower()
        if symbol == 'x':
            return ['x', 'o']
        elif symbol == 'o':
            return ['o', 'x']
        else:
            print('Выберите знак: X или O!')


def get_number(turn):
    # функция получает цифру от игрока
    print('Ходит игрок №' + str(turn))
    print('Введите цифру (1-9):')
    return int(input())


def cell_check(board, number, symbol_player1, symbol_player2):
    # функция проверяет ячейку на заполненность и даёт возможность выбрать другую ячейку
    while board[number] in (symbol_player1 + symbol_player2):
        print('Ячейка заполнена! Выберите другую ячейку')
        print('Введите цифру (1-9):')
        number = int(input())
    return number


def write_number(board, number, turn, symbol_player1, symbol_player2):
    # функция записывает число в таблицу
    if turn == 1:
        board[number] = symbol_player1
        return 2
    else:
        board[number] = symbol_player2
        return 1


def is_winner(board, gap_count, player, symbol_player1, symbol_player2):
    # функция проверяет кто из игроков выиграл и ничью
    if player == 1:
        player = 2
        combination_symbol = symbol_player2 * 3
    else:
        player = 1
        combination_symbol = symbol_player1 * 3

    if combination_symbol == (board[1] + board[2] + board[3]) or \
       combination_symbol == (board[4] + board[5] + board[6]) or \
       combination_symbol == (board[7] + board[8] + board[9]) or \
       combination_symbol == (board[1] + board[4] + board[7]) or \
       combination_symbol == (board[2] + board[5] + board[8]) or \
       combination_symbol == (board[3] + board[6] + board[9]) or \
       combination_symbol == (board[1] + board[5] + board[9]) or \
       combination_symbol == (board[3] + board[5] + board[7]):
        print('Выиграл игрок №' + str(player) + '!')
        return True

    if gap_count <= 1:
        print('Ничья!')
        return True


def is_play_again():
    print('Хотите сыграть ещё? (Да или Нет)')
    if input().lower().startswith('д'):
        return True


def main():
    print('Крестики-нолики')
    gap_count = 9
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    draw_board(board)
    symbol_player1, symbol_player2 = choice_symbol()
    turn = random.randint(1, 2)

    while True:
        number = cell_check(board, get_number(turn), symbol_player1, symbol_player2)
        turn = write_number(board, number, turn, symbol_player1, symbol_player2)
        gap_count -= 1
        draw_board(board)

        if is_winner(board, gap_count, turn, symbol_player1, symbol_player2):
            if is_play_again():
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                draw_board(board)
                symbol_player1, symbol_player2 = choice_symbol()
                turn = random.randint(1, 2)
            else:
                break


main()
