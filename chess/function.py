a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]

def summa(array):
    sum = 0
    index = 0
    while index < len(array):
        sum += array[index]
        index += 1
    print('перед ретёрн')
    return sum
    print('после ретёрн')


peremennaya = summa(a)
print(peremennaya)

a = input()
print(a)

