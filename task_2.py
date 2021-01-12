'''
2: Создайте функцию,
принимающую на вход 3 числа и возвращающую наибольшее из них.
'''

def max_number(*args):
    return max(args)

print(max_number(5, 7, 9))
