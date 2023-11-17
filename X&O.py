#Введение игрового поля

playing_field = [1,2,3,
                 4,5,6,
                 7,8,9]
#Установка условий победы
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
# Функция вывода игрового поля на экран

def print_playing_field():
    print(playing_field[0], end=" ")
    print(playing_field[1], end=" ")
    print(playing_field[2])

    print(playing_field[3], end=" ")
    print(playing_field[4], end=" ")
    print(playing_field[5])

    print(playing_field[6], end=" ")
    print(playing_field[7], end=" ")
    print(playing_field[8])

# Порядок хода игроков на игровом поле
def step_playing_field(step,symbol):
    ind= playing_field.index(step)
    playing_field[ind] = symbol


# Проверка выполнения условий победы
def get_result():
    win = ""

    for i in victories:
        if playing_field[i[0]] == "X" and playing_field[i[1]] == "X" and playing_field[i[2]] == "X":
            win = "X"
        if playing_field[i[0]] == "O" and playing_field[i[1]] == "O" and playing_field[i[2]] == "O":
            win = "O"

    return win

# Выполнение программы
game_over = False
player1 = True

while game_over == False:

# 1. Выводим игровое поле
    print_playing_field()

# 2. Просим игроков выполнить ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    step_playing_field(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)
# Игра окончена. Выводим игровое поле. Объявляем победителя.
print_playing_field()
print("Победил", win)