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
    buf = stroka.split('-')
    print(buf[0])
    print(buf[1])

move('e2-e4', pole, numbers, letters)

render(pole, numbers, letters)

