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

#пример запуска
s = [5,4,3,7,6,8,8,8,10,6,7,7,4,5,3,2,1,4,5,6,7,7,6,5,4,3,2,5,6,7,7,6,4,2,0]
pr = find_el(s,8,flag = False, left=3)
print(pr)