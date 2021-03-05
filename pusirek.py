def pusirek(spisok):
    not_sorted = True
    while not_sorted:
        perestanovki = 0
        for i in range(len(spisok) - 1):
            if spisok[i] > spisok[i+1]:
                buf = spisok[i]
                spisok[i] = spisok[i+1]
                spisok[i+1] = buf
                perestanovki += 1
        if perestanovki == 0:
            not_sorted = False

a = [3,2,1]
pusirek(a)
print(a)