def insertion_sort(arr: list[int]) -> None:
    """
    Сортировка вставками
    :param arr: list[int]: Входящий массив для сортировки
    :return: None
    """
    sortable_element = 1
    while sortable_element < len(arr):
        right_element = sortable_element
        left_element = right_element - 1
        while arr[right_element] < arr[left_element]:
            arr[left_element], arr[right_element] = arr[right_element], arr[left_element]
            if left_element > 0:
                right_element -= 1
                left_element -= 1
            else:
                break
        sortable_element += 1


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)