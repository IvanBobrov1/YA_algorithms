import sys


def check_numbers_less_given(numbers):
    result_list = []
    for i in numbers:
        count = 0
        # Для второго индекса и второго слагаемого.
        for j in numbers:
            # Если индексы равны, то есть это один и тот же элемент...
            if i > j:
                count += 1
        result_list.append(count)
    return result_list


if __name__ == '__main__':
    numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(*(check_numbers_less_given(numbers)))
