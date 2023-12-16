# numbers = [3, 7, 10, 20, 23]
# search_num = 25

import sys


def find_element(sorted_numbers: list[int], element: int) -> int:
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers) - 1
    if sorted_numbers.count(element) == len(sorted_numbers):
        return 0
    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == element:
            return mid
        if sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    if sorted_numbers[mid] > element:
        return mid
    return mid + 1


if __name__ == '__main__':
    numbers: list[int] = list(map(int,
                                  sys.stdin.readline().rstrip().split(' ')))
    search_num: int = int(sys.stdin.readline().rstrip())
    print(find_element(numbers, search_num))
