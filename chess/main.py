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
    '''
    index = 0
    while index < len(ret):
        i_in = 0
        while i_in < len(ret[index]):

            if ret[index][i_in] < 0:
                ret.pop(index)
                index -= 1
                break
            i_in += 1
        index += 1
    '''
    b = [] #список для хранения индексов с отрицательными координатами
    index = 0
    while index < len(ret):
        i = 0
        while i < len(ret[index]):
            if ret[index][i] < 0:
                b.append(index)
                break
            i += 1
        index += 1
    
   
    return b

   

a = [1,2,3,4,5,6,7]
b = [0,4]

a.pop(b[0])
a.pop(b[1])

print(a)

#c = [0,0]
#print(knight(c))