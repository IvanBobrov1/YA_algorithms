import sys


# len_array = sys.stdin.readline().rstrip()
# numbers = list(map(int, input().split(' ')))

# numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def delete_duplicate(len_array, numbers):

    res = set(numbers)

    # for num in numbers:
    #     if num in res:
    #         continue
    #     else:
    #         result_array.append(num)

    split = '_ ' * (len_array - len(res))
    print(*res, split, sep=' ')


len_array = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))
delete_duplicate(len_array, numbers)
