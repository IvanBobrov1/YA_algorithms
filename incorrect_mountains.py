import sys


def valid_mountain_array(array: list[int]) -> bool:
    if len(array) < 3:
        return False
    moutain_top: int = max(array)
    if array.count(moutain_top) > 1:
        return False
    index_moutain_top: int = array.index(moutain_top)
    if moutain_top == array[0] or moutain_top == array[-1]:
        return False
    for i in array[0:(index_moutain_top + 1)]:
        if i == moutain_top:
            break
        if i < array[array.index(i) + 1]:
            pass
        else:
            return False
    for j in array[index_moutain_top:]:
        if j == array[-1]:
            break
        if j > array[array[index_moutain_top:].index(j) + 1
                     + index_moutain_top]:
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    mountain_height_measurements: list[int] = (
        list(map(int, sys.stdin.readline().rstrip().split(' ')))
    )
    print(valid_mountain_array(mountain_height_measurements))
