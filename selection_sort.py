def selection_sort(arr: list[int]) -> None:
    """
    Сортировка выбором
    :param arr: list[int]: Входящий проверяемый массив
    :return: None
    """
    queue_element_index = 0
    while queue_element_index < len(arr) - 1:
        checking_array = arr[queue_element_index + 1: len(arr)]
        min_element = min(checking_array)
        min_element_index = arr.index(min_element)
        if min_element < arr[queue_element_index]:
            arr[queue_element_index], arr[min_element_index] = arr[min_element_index], arr[queue_element_index]
        queue_element_index += 1


my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)