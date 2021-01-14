'''
1: Создайте модуль (т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9
в папке из которой запущен данный код.
Затем создайте вторую функцию удаляющую эти папки.
Проверьте работу функций в этом же модуле.
'''

import os
import sys

def make_dir(count: int):
    for i in range(1, count+1):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(path)

def del_dir(user_path: str, name: str):
    if user_path == '..':
        user_path = os.path.join(os.getcwd())
    os.rmdir(f'{user_path}/{name}')

command = sys.argv[1]

if command == 'makedir':
    make_dir(int(sys.argv[2]))
elif command == 'deldir':
    del_dir(sys.argv[2], sys.argv[3])

