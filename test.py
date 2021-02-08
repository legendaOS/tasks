from random import randint as randint

row = 10 #макс строка + 1
col = 10 #макс столбец + 1
#привязка клавиш
attach = {'w':[-1, 0], 'a':[0, -1], 's':[1, 0], 'd':[0, 1]}


'''
координаты элемента описываются как [строка, столбец]
'''

snake = [[randint(0,row-1), randint(0, col-1)]]

place = [['-' for i in range(col)] for j in range(row)]

def print_place(a):
    for i in a:
        str = ''
        for j in i:
            str += j + ' '
        print(str)

def set_place(place, list_coord):
    head = True
    for coord in list_coord:
        if head:
            place[coord[0]][coord[1]] = '#'
            head = False
        else:
            place[coord[0]][coord[1]] = '0'


def turn_place(place, list_coord, symbol, attach):
    index = 0
    while index < len(list_coord):
        place[list_coord[index][0]][list_coord[index][1]] = '-'
        list_coord[index][0] += attach[symbol][0]
        list_coord[index][1] += attach[symbol][1]
        index += 1
    index = 0
    while index < len(list_coord):
        if list_coord[index][0] < 0:
            list_coord[index][0] = row - 1
        if list_coord[index][1] < 0:
            list_coord[index][1] = col - 1
        if list_coord[index][0] > row - 1:
            list_coord[index][0] = 0
        if list_coord[index][1] > col - 1:
            list_coord[index][1] = 0
        index += 1

while True:
    s = input('wasd:')
    if s not in attach:
        break
    turn_place(place, snake, s, attach)
    set_place(place, snake)
    print_place(place)

        
        

        