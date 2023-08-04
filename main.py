from random import randint


def ar_prog(first, d, n):
    return [first + (i - 1) * d for i in range(1, n + 1)]


def index_of_elem_in_diapazon(lst, mn, mx):
    return [i for i in range(len(lst)) if mn <= lst[i] <= mx]


print('ЗАДАЧА 1:')
print(f'для проверки входных данных из условия: {ar_prog(7, 2, 5)}')
#print(ar_prog(int(input('введите 1й элемент ап ')), int(input('введите разность ')), int(input('введите число элем '))))

print('ЗАДАЧА 2:')
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
lst2 = [randint(1, 50) for i in range(20)]
print(index_of_elem_in_diapazon(lst1, 5, 15))
print(f'список для проверки: {lst2}')
print(f'резудьтат: {index_of_elem_in_diapazon(lst2, int(input("введите левую границу ")), int(input("введите правую границу ")))}')

