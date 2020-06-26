a = int(input('Введите a: '))
b = int(input('Введите b: '))
k = 1
while a <= b:
    print(f'{k}-й день:', '{:.2f}'.format(a))
    a = a*1.1
    k += 1
print(f'{k}-й день:', '{:.2f}'.format(a))
print('Ответ: на', f'{k}-й день спортсмен достиг результата - не менее', str(b), 'км')
