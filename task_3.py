'''
3: Дан список заполненный произвольными целыми числами.
Получите новый список,
элементами которого будут только уникальные элементы исходного.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
'''

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result_list = []
for el in my_list_1:
    if my_list_1.count(el) == 1:
        result_list.append(el)

print(result_list)
