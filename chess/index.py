def find_el(spisok, elem, flag = True, left = 0, right = None):
    '''
    find_el - находит индекс(ы) элемента(ов) в списке
    spisok - список
    elem - елемент для поиска
    flag - True(первое вхождение), False(список вхождений)
    left, right - левая и правая границы поиска
    '''
    if flag == False: buf = []
    index = left
    if right == None:
        right = len(spisok) 
    while index < right:
        if spisok[index] == elem:
            if flag:
                return index
            else:
                buf.append(index)
        index += 1
    if flag == False and buf != []:
        return buf
    return -1

player_color = True
#True - белый цвет игрока
#False - черный цвет игрока
playing = True

pole = [
    [['r', 0],['n', 0],['b', 0],['k', 0],['q', 0],['b', 0],['n', 0],['r', 0]],
    [['p', 0],['p', 0],['p', 0],['p', 0],['p', 0],['p', 0],['p', 0],['p', 0]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[]],
    [['P', 1],['P', 1],['P', 1],['P', 1],['P', 1],['P', 1],['P', 1],['P', 1]],
    [['R', 1],['N', 1],['B', 1],['Q', 1],['K', 1],['B', 1],['N', 1],['R', 1]]
]

numbers = ['8','7','6','5','4','3','2','1']
letters = ['a','b','c','d','e','f','g','h']

def render(pole_list, numbers_list, letters_list):
    height = len(pole)
    index = 0
    while index < height:
        buf_str = numbers_list[index] + ' |'
        width = len(pole_list[index])
        index_width = 0
        while index_width < width:
            if pole_list[index][index_width] == []:
                buf_str += '- '
            else:
                buf_str += pole_list[index][index_width][0] + ' '
            index_width += 1
        print(buf_str)
        index += 1
    
    index = 0
    buf_str = '   '
    while index < len(letters):
        buf_str += letters[index] + ' '
        index += 1
    print('   '+'_'*(len(buf_str)-4))
    print(buf_str)
    return True

def move(stroka, pole_list, numbers_list, letters_list):
    buf = stroka.split(' ')
    coord1 = []
    coord1.append(find_el(numbers_list,buf[0][1]))
    coord1.append(find_el(letters_list,buf[0][0]))
    coord2 = []
    coord2.append(find_el(numbers_list,buf[1][1]))
    coord2.append(find_el(letters_list,buf[1][0]))
    super_bufer = pole_list[coord1[0]][coord1[1]].copy()
    pole_list[coord1[0]][coord1[1]] = []
    pole_list[coord2[0]][coord2[1]] = super_bufer


#move('e2 e4', pole, numbers, letters)

#render(pole, numbers, letters)

def main(pole = pole, numbers = numbers, letters = letters, player_color = player_color, playing = playing):
    count = 1
    while playing:
        print('Ход:', count)
        count += 1
        if player_color:
            print('Ходит первый игрок')
        else:
            print('Ходит второй игрок')
        render(pole, numbers, letters)
        print('Введите ход')
        in_stroka = input()
        if in_stroka == '':
            playing = False
            continue
        move(in_stroka, pole, numbers, letters)
        player_color = not player_color
        
    return 0

main()
