example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    # Напишите здесь код сортировки.
    last_index = len(data) - 1
    swapped = False

    for i in range(0, last_index):
        for item_index in range(0, last_index - i):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
        if swapped is False:
            break
    return data


print(bubble_sort(example_array))
