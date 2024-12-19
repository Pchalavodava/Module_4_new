def insertion_sort(arr: list[int]) -> None:
    """
    Сортировка вставками
    :param arr: list[int]: Входящий массив для сортировки
    :return: None
    """
    sortable_element = 1
    while sortable_element < len(arr):
        i = sortable_element
        while arr[i] < arr[i - 1]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i - 1 > 0:
                i -= 1
            else:
                break
        sortable_element += 1


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)