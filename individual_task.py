#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу с использованием замыканий для решения задачи. 
# Номер варианта 2. На вход программы поступает строка из целых чисел, 
# записанных через пробел. Напишите функцию get_list , 
# которая преобразовывает эту строку в список из целых чисел и возвращает его. 
# Определите декоратор для этой функции, который сортирует список чисел, 
# полученный из вызываемой в нем функции. 
# Результат сортировки должен возвращаться при вызове декоратора. 
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список на экране.


def sort_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sorted_result = sorted(result)
        return sorted_result
    return wrapper


@sort_decorator
def get_list(input_string):
    number_list = list(map(int, input_string.split()))
    return number_list


if __name__=="__main__":
    input_string = input("Введите строку из целых чисел через пробел: ")
    sorted_list = get_list(input_string)
    print("Отсортированный список:", sorted_list)
