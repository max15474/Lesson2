i = 0
while i < 10:
    print(i)
    i = i + 1

answer = None
while answer != 'Volvo':
    answer = input('Какая марка авто лучше всех? ')
print('Вы правы!')

while i < 10:
    print(i)
    i = i + 1
    if i == 9: break
    if i < 3: continue