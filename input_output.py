# однострочный коммент

'''
первая строка
вторая строка
'''

print('Hello')
print('=' * 8, 'Hello', 'World!', '=' * 8)
print('=' * 8, 'Hello', 'World!', '=' * 8, sep = '')
print('=' * 8, 'Hello', 'World!', '=' * 8, sep = ' *** ')
print('=' * 8, 'Hello', 'World!', '=' * 8, end = ' yyy')

# Ввод
name = input('\nВведите ваше имя: ')
print(name, type(name))
age = input('\nСколько вам лет: ')
print(int(age), type(int(age)))