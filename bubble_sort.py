import random


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Функция сортировки методом пузырьком
    :param arr: list[int]: Входящий массив значений для сортировки
    :return: list[int]: Отсортированный список
    """
    left_element, right_element = 0, 1
    steps = len(arr) - 1
    while steps > 0:
        while right_element < len(arr):
            if arr[left_element] > arr[right_element]:
                arr[left_element], arr[right_element] = arr[right_element], arr[left_element]
            left_element += 1
            right_element += 1
        steps -= 1
        left_element, right_element = 0, 1
    return arr


# my_list = []
# for _ in range(10, 20):
#     my_list.append(random.randint(1, 99))
my_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(my_list))
