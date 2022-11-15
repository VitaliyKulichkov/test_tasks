def main():
    # Имя файла

    file_path = input('Введите путь до файла: ')
    # Чтение данных из файла
    text = open(file_path, "r", encoding='utf-8').readlines()
    a = []
    for line in text:
        a.append(int(line.strip()))

    # Нахождение минимального количества ходов
    m = sorted(a)[len(a) // 2]
    print(sum(abs(v - m) for v in a))


if __name__ == '__main__':
    main()
