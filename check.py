import sys

# for _ in range(10**6):
#     sys.stdin.readline().rstrip()

# elements_count = int(input())

# data = [None] * elements_count

# for index in range(elements_count):
#     data[index] = input()

# print(data)

# ускорим считывание элементов:

elements_count = int(sys.stdin.readline().rstrip())

data = [None] * elements_count

for index in range(elements_count):
    data[index] = sys.stdin.readline().rstrip()

print(data)

# эффективный вывод элементов:

# Импорт системной библиотеки, 
# при помощи которой будем считывать данные из стандартного потока ввода.


def main():
    # Прочитали первую строку, в которой указано количество строк,
    # преобразовали в число:
    num_lines = int(sys.stdin.readline().rstrip())  
    output_numbers = [None] * num_lines
    # Читаем следующие строки ввода:
    for i in range(num_lines):
        # Считали строку и удалили символы перевода строки.
        line = sys.stdin.readline().rstrip()
        # Разделили строку по пробельному символу,        
        # присвоили значения из строки переменным first и second соответственно.
        first, second = line.split()  
        # Преобразовали строки в целые числа.
        first = int(first)  
        second = int(second)
        # Получили сумму.
        result = first + second  
        # Записали в массив ответов текущий результат как строку.
        output_numbers[i] = str(result)
    # В конце вывели все полученные ответы за один раз.
    # print('\n'.join(output_numbers)) - работает для вывода в файл
    # или
    print(*output_numbers, sep='\n') # только для вывода в консоль


if __name__ == '__main__':
    main()
