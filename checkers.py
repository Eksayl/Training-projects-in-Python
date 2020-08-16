import random


def draw_board():
    # вывод игрового поля

    print()
    print('       a ' + '  b ' + '  c ' + '  d ' + '  e ' + '  f ' + '  g ' + '  h ')
    print('     ---------------------------------')
    print('   8 ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[8][2] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[8][4] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[8][6] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[8][8] + ' ' + '|' + ' 8')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   7 ' + '|' + ' ' + squares[7][1] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[7][3] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[7][5] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[7][7] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' 7')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   6 ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[6][2] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[6][4] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[6][6] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[6][8] + ' ' + '|' + ' 6')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   5 ' + '|' + ' ' + squares[5][1] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[5][3] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[5][5] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[5][7] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' 5')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   4 ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[4][2] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[4][4] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[4][6] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[4][8] + ' ' + '|' + ' 4')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   3 ' + '|' + ' ' + squares[3][1] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[3][3] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[3][5] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[3][7] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' 3')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   2 ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[2][2] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[2][4] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[2][6] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[2][8] + ' ' + '|' + ' 2')
    # print('     |---|---|---|---|---|---|---|---| ')
    print('   1 ' + '|' + ' ' + squares[1][1] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[1][3] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[1][5] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' ' + squares[1][7] + ' ' + '|' + '▒' + '▒' + '▒' + '|' + ' 1')
    print('     ---------------------------------')
    print('       a ' + '  b ' + '  c ' + '  d ' + '  e ' + '  f ' + '  g ' + '  h ')
    print()
    

def input_mark():
    # ввод знака
    print('Игрок №1 выберите знак: =/+')
    mark = '*'
    while mark not in '+=':
        mark = input()
        if mark in '=':
            marks = ['=', '+']
        elif mark in '+':
            marks = ['+', '=']
        else:
            print('Неправильно! Введите знак "=" или "+"!')
    return marks


def input_gamer(turn, first_player, second_player, squares, letters, xy):
    # ввод игрока
    print('Сделайте ход!')
    while True:
        input_turn = input()
        
        if turn == 1:
            mark = first_player
        else:
            mark = second_player
        
        # проверка на обратный ход
        # направления: ↙, ↘
        if mark in '=' and (int(input_turn[1]) - int(input_turn[3]) == 1 and letters[input_turn[0]] - letters[input_turn[2]] == 1 or int(input_turn[1]) - int(input_turn[3]) == 1 and letters[input_turn[0]] - letters[input_turn[2]] == -1):
            print('Назад ходить нельзя!')
            print('Сделайте другой ход')
            continue
            
        # проверка на обратный ход  
        # направления: ↖, ↗
        elif mark in '+' and (int(input_turn[1]) - int(input_turn[3]) == -1 and letters[input_turn[0]] - letters[input_turn[2]] == -1 or int(input_turn[1]) - int(input_turn[3]) == -1 and letters[input_turn[0]] - letters[input_turn[2]] == 1):
            print('Назад ходить нельзя!')
            print('Сделайте другой ход')
            continue

        x = letters[input_turn[0]] - letters[input_turn[2]]
        y = int(input_turn[1]) - int(input_turn[3])
        # условие на направление атаки
        if (x == 2 or x == -2) and (y == 2 or y == -2):
            # условие: клетка пуста?
            if squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]] not in '+±=≠':
                print('Клетка пуста!')
                print('Сделайте другой ход')
                continue
            # условия: атака на своих?
            elif squares[int(input_turn[1])][letters[input_turn[0]]] == squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]]:
                print('Своих рубить нельзя!')
                print('Сделайте другой ход')
                continue
            elif squares[int(input_turn[1])][letters[input_turn[0]]] in '+±' and squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]] in '+±':
                print('Своих рубить нельзя!')
                print('Сделайте другой ход')
                continue
            elif squares[int(input_turn[1])][letters[input_turn[0]]] in '=≠' and squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]] in '=≠':
                print('Своих рубить нельзя!')
                print('Сделайте другой ход')
                continue
            else:
                squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]] = ' '
                break
        # условие: клетка занята?
        elif squares[int(input_turn[1])][letters[input_turn[0]]] in '+±=≠' and squares[int(input_turn[3])][letters[input_turn[2]]] in '+±=≠':
            print('Клетка занята!')
            print('Сделайте другой ход')
            continue
        else:
            squares[int(input_turn[1]) + xy[y]][letters[input_turn[0]] + xy[x]] = ' '
            break
            
    return(str(input_turn))
    
    
def fill_square(turn, input_g, squares, letters, first_player, second_player):
    # выбор знака для заполнения
    if turn == 1:
        mark = first_player
        turn = 2
    else:
        mark = second_player
        turn = 1
    
    # заполнение клетки
    squares[int(input[1])][letters[input[0]]] = ' '
    squares[int(input[3])][letters[input[2]]] = mark
    return turn


squares = [[], ['*', '=', ' ', '=', ' ', '=', ' ', '=', ' '], ['*', ' ', '=', ' ', '=', ' ', '=', ' ', '='],
               ['*', '=', ' ', '=', ' ', '=', ' ', '=', ' '], ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['*', ' ', '+', ' ', '+', ' ', '+', ' ', '+'],
               ['*', '+', ' ', '+', ' ', '+', ' ', '+', ' '], ['*', ' ', '+', ' ', '+', ' ', '+', ' ', '+']]
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
xy = {-2: 1, 2: -1}


def main():
    # тело основного кода

    # случайно выбирает кто будет ходить первым
    turn = random.randint(1, 2)
    draw_board()
    first_player, second_player = input_mark()
    
    while True:
        draw_board()
        
        if turn == 1:
            print('Ход игрока №' + str(turn) + ' (' + first_player +'):')
        else:
            print('Ход игрока №' + str(turn) + ' (' + second_player +'):')
            
        input_g = input_gamer(turn, first_player, second_player, squares, letters, xy)
        
        turn = fill_square(turn, input_g, squares, letters, first_player, second_player)
        
        
main()