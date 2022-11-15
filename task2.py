import math

file_path1 = input('Введите путь до файла с параметрами окружности: ')
file_path2 = input('Введите путь до файла с координатами точек: ')


# Получаем центр окружности и радиус

def coord_circle(file_path1):
    with open(file_path1) as file:
        lines = [line.rstrip() for line in file]
        coord = lines[0]
        coord_list = [float(num) for num in filter(
            lambda num: num.isnumeric(), coord)]
        x0, y0 = coord_list[0], coord_list[1]
        rad = float(lines[1])
    return (x0, y0, rad)


# Получаем координаты точек для проверки
def coord_of_points(file_path2):
    result = []
    with open(file_path2) as f:
        for line in f:
            result.append(list(map(float, line.split())))
    return (result)


# Проходим по точкам
def place_of_point(x_c, y_c, r_c, lst_points):
    for i in range(len(lst_points)):
        x_point = lst_points[i][0]
        y_point = lst_points[i][1]
        hypotenuse = math.sqrt((abs(x_point) - x_c) ** 2 + ((abs(y_point) - y_c) ** 2))
        if hypotenuse < r_c:
            print('1' + '\n')
        elif hypotenuse == r_c:
            print('0' + '\n')
        else:
            print('2' + '\n')


def main():
    p_c = coord_circle(file_path1)
    lst_points = coord_of_points(file_path2)
    place_of_point(x_c=p_c[0], y_c=p_c[1], r_c=p_c[2], lst_points=lst_points)


if __name__ == '__main__':
    main()
