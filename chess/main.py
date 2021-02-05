# комментарий
def knight(coord):
    '''
    knight - функция возвращающая все доступные варианты ходов для фигуры конь
    coord - список двух координат фигуры (номер строки и номер столбца)
    '''
    ret = []
    ret.append([coord[0] - 2 , coord[1] - 1]) # вверх на 2 и налево на 1
    ret.append([coord[0] - 1 , coord[1] - 2]) # вверх на 1 и налево на 2
    ret.append([coord[0] + 1 , coord[1] - 2]) # вниз на 1 и налево на 2
    ret.append([coord[0] + 2 , coord[1] - 1]) # вниз на 2 и налево на 1
    ret.append([coord[0] + 2 , coord[1] + 1]) # вниз на 2 и направо на 1
    ret.append([coord[0] + 1 , coord[1] + 2]) # вниз на 1 и направо на 2
    ret.append([coord[0] - 1 , coord[1] + 2]) # вверх на 1 и направо на 2
    ret.append([coord[0] - 2 , coord[1] + 1]) # вверх на 2 и направо на 1

    index = 0
    index_to_pop = []
    while index < len(ret):
        index_inside_elem_ret = 0
        while index_inside_elem_ret < len(ret[index]):
            if ret[index][index_inside_elem_ret] < 0:
                index_to_pop.append(index)
                print(index)
            index_inside_elem_ret += 1
        index  = index + 1

    index = 0
    

    return ret


c = [0,0]
print(knight(c))