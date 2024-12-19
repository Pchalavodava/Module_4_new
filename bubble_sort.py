import random


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Функция сортировки методом пузырьком
    :param arr: list[int]: Входящий массив значений для сортировки
    :return: list[int]: Отсортированный список
    """
    i = 0
    unchanged_index = 0
    while unchanged_index < len(arr) - 1:
        unchanged_index = 0
        while i + 1 < len(arr):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                unchanged_index += 1
            i += 1
        i = 0

    return arr


# my_list = []
# for _ in range(10, 20):
#     my_list.append(random.randint(1, 99))
my_list = [64, 34, 25, 12, 22, 11, 90]
print(f'Список на входе: {my_list}')
bubble_sort(my_list)
print(f'Отсортированный список: {my_list}')

