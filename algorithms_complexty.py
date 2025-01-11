# 1. Алгоритм проверки наличия дубликатов в массиве

def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

"""
Константная сложность O(1) в лучшем случае, если первый элемент i == первому элементу j. 
Квадратичная сложность O(n^2) в худшем случае, если дубликаты находятся в конце списка. Так как
для каждого цикла for сложность является линейной O(n). Там самым получаем O(n*n) = O(n^2)
"""


# 2. Алгоритм поиска максимально элемента в неотсортированном массиве
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val


"""
Линейная сложность O(n), так алгоритм проходит по всему списку в любом случае. И если каждый последующий
элемент больше предыдущего, то операция max_val = val также имеет сложность O(n). Таким образом 
получаем O(n*2). Но так как, по правилам, интересует самая быстрорастущая часть, то получаем O(n)
"""

# 3. Алгоритм сортировки выбором (Selection Sort)


def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


"""
Цикл for j ... имеет линейную сложность O(n), так как он проходит по всем элементам и сравнивает 
их с arr[min_ind]. Также цикл for i ... имеет такую же сложность O(n), так как также проходит по
каждому элементу списка для предоставления его дальшему циклу для сравнения. Следовательно,
сложность для сортировки выбором будет O(n * n) = O(n^2) - квадратичная.
"""

# 4. Алгоритм быстрой сортировки


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


"""
Линейно-логарифмическая сложность O(n log n). Так как разделение на разделение списка уходит log n
операций. Но для сортировки подсписков уходит n операций. Таким образом получаем сложность O(n log n)
"""

# Алгоритм вычисления n-го числа Фибоначчи (рекурсивно)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

"""
Сложность рекурсивного вычисления числа Фибоначчи - экспоненциальная O(2^n), чем больше n - количество
элементов, тем быстрее растет функция
"""
# Факторы, которые могут повлиять на производительность алгоритмов это объем данных, сортировка в
# обратном порядке, непонимание задачи и выбор неверного алгоритма.


my_list = [1, 5, 7, 2, 5, 9, 3, 14]
print(has_duplicates(my_list))
print(find_max(my_list))
print(selection_sort(my_list))
print(quick_sort(my_list))
print(fibonacci_recursive(10))
