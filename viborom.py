def print_list(spisok):
    for value in spisok:
        i = 0
        buf = ''
        while i < value:
            buf += '#'
            i+=1
        print(buf)

def pusirek(spisok):
    not_sorted = True
    while not_sorted:
        print('---------------------')
        perestanovki = 0
        for i in range(len(spisok) - 1):
            if spisok[i] > spisok[i+1]:
                buf = spisok[i]
                spisok[i] = spisok[i+1]
                spisok[i+1] = buf
                perestanovki += 1
                
            print_list(spisok)
            print('- - - - - - - - - -')
        print('---------------------')
        if perestanovki == 0:
            not_sorted = False

def find_min_index(spisok, start_index):
    i = start_index
    min_index = start_index
    while i < len(spisok):
        if spisok[i] < spisok[min_index]:
            min_index = i
        i += 1
    return min_index
         
def sort_change(spisok):
    pointer = 0
    while pointer < len(spisok):
        min_i = find_min_index(spisok, pointer)
        buf = spisok[min_i]
        spisok[min_i] = spisok[pointer]
        spisok[pointer] = buf
        print_list(spisok)
        print('----------------------')
        pointer += 1
    
a = [1,4,2,5,3,6,4,7,5,8,6,9,7,10]
print_list(a)
print('----------------------')
sort_change(a)

print(a)


                
                
                
                
                
                
                