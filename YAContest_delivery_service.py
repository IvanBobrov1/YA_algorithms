"""
Время посылки:  17 дек 2023, 13:14:36
           ID:  103128283
       Задача:  A
   Компилятор:  Python 3.11.4
      Вердикт:  OK
        Время:  49ms
       Память:  4.15Mb
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
        count_platform += 1
        if array[rigth_index] == limit:
            rigth_index -= 1
            continue
        if left_index == rigth_index:
            break
        if array[rigth_index] < limit:
            weight_sum = (array[left_index] + array[rigth_index])
            if weight_sum == limit:
                rigth_index -= 1
                left_index += 1
            elif weight_sum > limit:
                rigth_index -= 1
            else:
                rigth_index -= 1
                left_index += 1
    return count_platform


if __name__ == '__main__':
    weight: list[int] = (
        list(map(int, sys.stdin.readline().rstrip().split(' ')))
    )
    max_lifting: int = int(sys.stdin.readline().rstrip())
    print(min_transport_platfor_for_delivery(weight, max_lifting))
