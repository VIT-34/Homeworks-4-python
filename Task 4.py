  # 1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

""" num = [1, 5, 2, 3, 4, 6, 1, 7]

def get_up(num):
    ups = []
    for i in range(len(num)):
        if num[i] == max(num[:i+1:]) and num[i] not in ups:
            ups.append(num[i])
    return ups
print(get_up(num)) """

# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию

""" from random import randint

with open('output.txt','w') as fw:
    for i in range (10): fw.write(str(randint(1,1000))+',')
    with open('output.txt','r') as fr:
        a=fr.readline().split(',')
        a.pop()
print (sorted(map(int, a))) """