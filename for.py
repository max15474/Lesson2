for i in range(10):
    print(i)

for i in range(0, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
    if i == 5: break

for i in range(10):
    answer = input('Какая марка авто лучше всех? ')
    if answer == 'Volvo':
        print('Вы правы!')
        break