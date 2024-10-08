def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, 'students', False]
print_params(*values_list)
values_dict = {'a': 'Vlad', 'b': 'Urban', 'c': 2024}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)