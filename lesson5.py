cash = int(input('Введите сумму выручки: '))
lost = int(input('Введите сумму издержек: '))
if cash > lost:
    print('Zer gud')
    print('Рентабельность: ', float((cash-lost)/cash))
    workers = int(input('Сколько сотрудников, отвечай!: '))
    print('Прибыль на сотрудника:', "{:.3f}".format((cash-lost)/workers))
else:
    print('Закрывайся! Твоя работа не эффективна')
