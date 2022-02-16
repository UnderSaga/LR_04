from os import *

def input_n():
    n = input('Введите путь к папке: ')
    if path.isdir(n) == True:
        return n
    else:
        return input_n()

def dictionary(n):
    for i in listdir(n):
        if path.isdir(n + "\\" + i):
            return dictionary(n + '\\' + i)
        elif path.isfile(n + '\\' + i):
            name1 = n + "\\" + i
            size = stat(n + "\\" + i).st_size
            d1[name1] = size
    return d1

def duplicate(d1):
    dubl = {}
    for i1 in d1:
        for i2 in d1:
            if i1 == i2:
                pass
            elif i1[i1.rfind('\\'):] == i2[i2.rfind('\\'):] and d1[i1] == d1[i2]:
                if i1 in dubl:
                    continue
                dubl.update({i1: d1[i1]})
            else:
                return dubl

def duplicate_2(dubl):
    if dubl == {}:
        print('Нет дубликатов')
    list1 = []
    for i1 in dubl:
        if i1 not in list1:
            print('\n', '-----', path.getsize(i1), 'байт -----')
            print(i1)
            for i2 in dubl:
                if i1 == i2:
                    pass
                elif i1[i1.rfind('\\'):] == i2[i2.rfind('\\'):] and dubl[i1] == dubl[i2]:
                    print(i2)
                    list1.append(i2)

if __name__ == '__main__':
    d1 = {}
    q = input_n()
    r = dictionary(q)
    s = duplicate(r)
    duplicate_2(s)