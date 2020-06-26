sec = int(input('Введите количество секунд: '))
h = sec//3600%24
m = (sec - h*3600)//60%60
s = sec % 60
print("{:02}:{:02}:{:02}".format(h, m, s))
