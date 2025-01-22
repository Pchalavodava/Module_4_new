from typing import Any

"""
Var_1 Словарь из списка кортежей

"""


class MyDict:

    def __init__(self):
        self.mydict = []

    def __str__(self) -> str:
        """
        Строковое представление словаря из списка кортежей
        :return: str: список тьюплов
        """
        return str(self.mydict)

    def __getitem__(self, key: Any) -> Any | None:
        """
        Получение значения по ключу. В данном случае получение второго значение кортежа [1],
        где первое значение [0] является ключом
        :param key: Any: Ключ
        :return: Any | None: Второй элемент кортежа, если ключ существует, иначе None
        """
        my_key_list = [k[0] for k in self.mydict]
        if key in my_key_list:
            my_value_list = [v[1] for v in self.mydict]
            ind = my_key_list.index(key)
            return my_value_list[ind]
        else:
            return None

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Присваивает значение по ключу. В данном случае создат кортеж из двух элементов: ключ и значение
        :param key: Any: Ключ словаря
        :param value: Any: Значение словаря
        :return: None
        """
        self.mydict.append((key, value))

    def __delitem__(self, key: Any) -> None:
        """
        Удаление объекта ключ + значение
        :param key: Any: Ключ для удаления
        :return: None
        """
        my_key_list = [k[0] for k in self.mydict]
        if key in my_key_list:
            ind = my_key_list.index(key)
            self.mydict.pop(ind)

    def __contains__(self, key: Any) -> bool:
        """
        Проверка принадлежности ключа key словарю
        :param key: Any: Ключ для проверки
        :return: bool: True, если существует, False иначе
        """
        return key in [k[0] for k in self.mydict]

    def keys(self) -> list[Any]:
        """
        Создание списка ключей словаря
        :return: list[Any]: Список ключей словаря
        """
        return [k[0] for k in self.mydict]

    def values(self) -> list[Any]:
        """
        Создание списка значений словаря
        :return: list[Any]: Список значений словаря
        """
        return [v[1] for v in self.mydict]

    def items(self) -> list[tuple]:
        """
        Получение списка тьюплов (ключ, значение)
        :return: list[tuple]: Список тьюплов
        """
        return self.mydict


print('Вариант 1')
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict['age'])

print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)

"""
Var_2 Словарь из списка списков

"""


class MyDict:
    def __init__(self):
        self.key_list = []
        self.value_list = []

    def __str__(self) -> str:
        """
        Строковое представление словаря
        :return: str: Словарь в виде строки
        """
        return f'keys = {self.key_list} \nvalues = {self.value_list}'

    def __getitem__(self, key: Any) -> Any | None:
        """
        Получение значения по ключу
        :param key: Any: Ключ для получения значения
        :return: Any | None: Значение, если ключ найден, иначе None
        """
        if key not in self.key_list:
            return None
        else:
            return self.value_list[self.key_list.index(key)]

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Присвоение значения по ключу. В данном случае заполнение словарей ключей и их значений
        :param key: Any: Ключ
        :param value: Any: Значение
        :return: None
        """
        self.key_list.append(key)
        self.value_list.append(value)

    def __delitem__(self, key: Any) -> None:
        """
        Удаление объекта словаря. В данном случае удаление ключа и удаление значения из
        списка значений по индексу ключа
        :param key: Any: Ключ для удаления
        :return: None
        """
        if key in self.key_list:
            ind = self.key_list.index(key)
            self.key_list.remove(key)
            self.value_list.pop(ind)

    def __contains__(self, key: Any) -> bool:
        """
        Проверка вхождения ключа в словарь
        :param key: Any: Ключ для проверки
        :return: bool: True, если ключ найден, False иначе
        """
        return key in self.key_list

    def keys(self) -> list[Any]:
        """
        Получение списка ключей
        :return: list[Any]: Список ключей
        """
        return self.key_list

    def values(self) -> list[Any]:
        """
        Получение списка значений
        :return: list[Any]: Список значений
        """
        return self.value_list

    def items(self) -> list[list]:
        """
        Получение списка списков ключ-значение
        :return: list[list]: Список объектов словаря
        """
        item_list = []
        for key in self.key_list:
            item_list.append([key, self.value_list[self.key_list.index(key)]])
        return item_list


print('\nВариант 2')
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict['age'])

print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)

"""
Var_3 Создание словаря с помощью встроенного словаря

"""


class MyDict:

    def __init__(self):
        """
        Объявление словаря
        """
        self.mydict = {}

    def __str__(self) -> str:
        """
        Строковое представление словаря
        :return: str: Словарь в текстовом представлении
        """
        return str(self.mydict)

    def __getitem__(self, key: Any) -> Any:
        """
        Получение значения по заданному ключу
        :param key: Any: Ключ
        :return: Any: Значение по ключу
        """
        return self.mydict.get(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Присвоение значения ключу
        :param key: Any: Ключ
        :param value: Any: Значение
        :return: None
        """
        self.mydict[key] = value

    def __delitem__(self, key: Any) -> None:
        """
        Удаление объекта словаря
        :param key: Any: Ключ для удаления
        :return: None
        """
        if key in self.mydict:
            self.mydict.pop(key)

    def __contains__(self, key: Any) -> bool:
        """
        Проверка на вхождение ключа в словарь
        :param key: Any: Ключ
        :return: bool: True, если ключ найден, False иначе
        """
        return key in self.mydict

    def keys(self) -> list[Any]:
        """
        Получение списка ключей
        :return: list[Any]: Список ключей
        """
        return list(self.mydict.keys())

    def values(self) -> list[Any]:
        """
        Получение списка значений
        :return: list[Any]: Список значений
        """
        return list(self.mydict.values())

    def items(self) -> dict[Any: Any]:
        """
        Получение словаря
        :return: dict[Any: Any]: Словарь ключ-значение
        """
        return self.mydict.items()


print('\nВариант 3')
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict['age'])

print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)

"""
Var_4 Создание словаря с помощью встроенного словаря __dict__ без инициализации пустого словаря

"""


class MyDict:
    def __init__(self):
        pass

    def __str__(self) -> str:
        """
        Строковое представление словаря
        :return: str: Словарь текстом
        """
        return f'{self.__dict__}'

    def __getitem__(self, key: Any) -> Any:
        """
        Получение значения по ключу
        :param key: Any: Ключ
        :return: Any: Значение ключа Key
        """
        return self.__dict__.get(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Установление значения ключу
        :param key: Any: Ключ
        :param value: Any: Устанавливаемое значение
        :return: None
        """
        setattr(self, key, value)

    def __delitem__(self, key: Any) -> None:
        """
        Удаление значения по ключу
        :param key: Any: Ключ для удаления
        :return: None
        """
        if key in self.__dict__.keys():
            delattr(self, key)

    def __contains__(self, key: Any) -> bool:
        """
        Проверка на вхождение ключа в словарь
        :param key: Any: Проверяемый ключ
        :return: bool: True - ключ найден, False - нет
        """
        return key in self.__dict__

    def keys(self) -> list[Any]:
        """
        Получение списка ключей
        :return: list[Any]: Список ключей
        """
        return list(self.__dict__.keys())

    def values(self) -> list[Any]:
        """
        Получение списка значений
        :return: list[Any]: Список значений
        """
        return list(self.__dict__.values())

    def items(self):
        """
        Получение словаря
        :return: dict[Any: Any]: Словарь ключ-значение
        """
        return list(self.__dict__.items())


print('\nВариант 4')
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict['age'])

print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)
