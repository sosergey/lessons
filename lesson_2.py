#Задание (a)

print('Задание сложности (a) 1')
name = '  Сергей Со  123123.,!'#"#input('Введите ваше имя и фамилию: ')
print('Добрый день '+name.strip('.,!@#$%^&*()1234567890 ')+', рады приветствовать вас!')

print('\nЗадание сложности (a) 2\nВ процентах:')
a = '0,15542352' #input('Введите дробное число: ')
if a.find(',')!=-1:
    a = float(a.replace(',', '.'))
    print(round(a, 2)*100,'%')
elif a.find('.')!=-1:
    a = float(a)
    print(round(a, 2)*100,'%')
else:
    print('Нужно ввести дробное число через запятую или точку')

print('\nВ валюте:')
b = "3542352515,156467496846546" #input('Введите число: ')
b = float(b.replace(',', '.'))
print("{:,.2f}$".format(b))


print('\n----------------------------------------'
      '\nЗадание сложности (b)')
#Задание B
import re
regName = re.compile('[^a-zA-Z]') #шаблон регулярки для имен
regNumber = re.compile('[^0-9]') #шаблон для чисел

name = regName.sub('',input('Имя: ')).capitalize()
surname = regName.sub('',input('Фамилия: ')).capitalize()
age = regNumber.sub('',input('Возраст: '))
adress = input('Адрес: ').strip('!@#$%^&*() ')
phone = regNumber.sub('',input('Телефон: '))

print('\n1')
data = {'Имя': name, 'Фамилия': surname, 'Возраст': age, 'Адрес':adress,'Телефон':phone}
for key, value in data.items():
    print('{0} : {1}'.format(key, value))

print('\n2')
if int(age) > 18:
    temp = "Добрый день господин {surname}, на почте свежие котировки акций"
    print(temp.format(surname=surname))
elif int(age)<=18:
    temp = "Привет малыш {name}, в холодильнике есть мороженное для тебя"
    print(temp.format(name=name))

print('\n----------------------------------------'
      '\nЗадание сложности (c)')
#Задание С
print('1')

arrBadWords = ['мудак','козел','урод','баран'] #Создаем массив с матами
text = 'козел и баран пошли гулять на базар'#input('Введите строку с плохим словом: ').lower().split(' ') #Ввод строки
print('Вводные данные: ',text)
text = text.lower().split(' ')
result=[]
for i in text:
    if i in arrBadWords:
        i = '*'*len(i)
        result.append(i)
    else:
        result.append(i)
result = ' '.join(result)
print('Результат: '+result)

print('\n2')
text2 = 'этот подлец планирует ограбление'
dictionary = {'убегать':'канать','пивная':'тошниловка','ограбление':'гоп-стоп','подлец':'редиска'}
text2=text2.lower().split(' ') #к нижнему регистру и разбить в список
result2=[]
for word in text2:
    if word in dictionary:
        result2.append(dictionary[word])
    else:
        result2.append(word)
result2 = ' '.join(result2)
print('Результат: ',result2)
