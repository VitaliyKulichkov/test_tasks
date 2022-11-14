#Имя файла
filename = input('Введите название файла: ')
#Чтение данных из файла
text = open(filename,'r').readlines()
a = []
for line in text:
    a.append(int(line.strip()))
print(a)

#Нахождение минимального количества ходов
m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))