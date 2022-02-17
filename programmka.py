from os import *

def input_n():
    n = input('Введите путь к папке: ')
    if path.isdir(n) == True:
        return dictionary(n)
    else:
        return input_n()

def dictionary(n):
    result = {}
    for i in listdir(n):
        if path.isdir(n + "\\" + i):
            result.update(dictionary(n + "\\" + i))
        elif path.isfile(n + '\\' + i):
            result[n + "\\" + i] = path.getsize(n + "\\" + i)
    return result

def duplicate(a: dict):
    keys = list(a.keys())
    dubl = {}
    for i1 in range(len(keys) - 1):
        key1 = keys[i1]
        result_key = (a[key1], key1)
        for i2 in range(i1 +1, len(keys)):
            key2 = keys[i2]
            if path.basename(key1) == path.basename(key2) and a[key1] == a[key2]:
                if result_key not in dubl:
                    dubl[result_key] = []
                dubl[result_key].append(key2)
        if result_key in dubl:
            yield result_key, dubl[result_key]

def duplicate_2(result):
    for key, val in result.items():
        print(val)
        for i in key:
            print(key)
        print()

if __name__ == '__main__':
    duplicate_2(input_n())