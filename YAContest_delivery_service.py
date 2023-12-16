"""
Время посылки:  16 дек 2023, 23:19:44
           ID:  103107523
       Задача:  A
   Компилятор:  Python 3.11.4
      Вердикт:  OK
        Время:  58ms
       Память:  4.24Mb
"""
import sys


def min_transport_platfor_for_delivery(array: int, limit: int) -> int:
    """Считает минимальное количество платформ,
    неодходимых для доставки роботов"""
    array.sort()
    count_platform: int = 0
    left_index: int = 0
    rigth_index: int = len(array) - 1
    while left_index <= rigth_index:
        if array[rigth_index] == limit:
            count_platform += 1
            rigth_index -= 1
            continue
        if left_index == rigth_index:
            count_platform += 1
            break
        if array[rigth_index] < limit:
            if (array[left_index] + array[rigth_index]) == limit:
                count_platform += 1
                rigth_index -= 1
                left_index += 1
            elif (array[left_index] + array[rigth_index]) > limit:
                count_platform += 1
                rigth_index -= 1
            else:
                count_platform += 1
                rigth_index -= 1
                left_index += 1
    return count_platform


if __name__ == '__main__':
    weight: list[int] = (
        list(map(int, sys.stdin.readline().rstrip().split(' ')))
    )
    max_lifting: int = int(sys.stdin.readline().rstrip())
    print(min_transport_platfor_for_delivery(weight, max_lifting))
