memory=0
while True:
    
    a=input("Введите 1 число:")
    
    if a=="mr":
        print(memory)
        continue
    
    if a=="mc":
        memory=0
        continue


    a=int(a)
    b=input("Введите знак:")

    if b=="m+":
        memory+=a
        continue

    c=input("Введите 2 число:")
    c=int(c)
    k="Итог:"

    if b=="+":
        print(k,a+c)
    elif "*"==b:
        print(k,a*c)
    elif "/"==b and b==0:
        print('ТЫ БОЛЬНОЙ???') 
    elif "/"==b:
        print(k,a/c)
    elif "-"==b:
        print(k,a-c)