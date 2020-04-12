# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных
# имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random)

from random import choices

def choices_name(list_names,N=15):
    '''Задается список имен - list_names и целое число - N.
    Возвращает список длины N случайных имен.'''
    return choices(list_names,k=N)

new_list_names = ['Ваня','Дима','Лена','Ира','Игорь','Ян','Маша','Даша','Наташа','Вася']
b=choices_name(new_list_names)
print(b)

            # 2  Напишите функцию вывода самого частого имени из списка на выходе функции F

def often_word(listik):
    '''Задается список listik.
    Возвращает самый частый элемент списка'''

    c_dict={}
    for i in range (len(b)):
        c_dict[b[i]]=0
    for sym in b:
        c_dict[sym]+=1
    print(c_dict)  # выводит словарь
    d=list(c_dict.items())
    #print(d)
    #print(list(c_dict.values()))   #  выводит список значений
    e=max(list(c_dict.values()))
    #print(max(list(c_dict.values())))  #  выводит максим значение из списка
    #print(c_dict[2])

    most_often=[]
    for key,values in d:
        if values == e:
           # return(key,':',values)
           #print(key,':',values)
            most_often.append((key,values))
    return most_often
print(often_word(b))


# 3 Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на

def redkaiy_bukva(names):
    '''
    :param names: Задаем список имен
    :return: Самую редкую букву, с которой начинаются имена
    '''

    #print(b)
    new = []
    for word in b:
        new+= word[0]
    print(new)

    new_dict = {}
    for r in new:
        new_dict[r]=0
    for sym in new:
        new_dict[sym]+=1
    print(new_dict)
    dd=list(new_dict.items())
    ee=min(list(new_dict.values())) # мин значение

    most_min=[]
    for key,values in dd:
        if values == ee:
            most_min.append((key)[0])
    ccc_dict={}
    for i in range (len(most_min)):
        ccc_dict[most_min[i]]=0
    for sym in most_min:
        ccc_dict[sym]+=1
    #print(ccc_dict.keys())
    return list(ccc_dict.keys()) # ТАК ВЫВОДИТ ВСЕ РЕДКИЕ БУКВЫ!!!!!!!!!!!!

print(redkaiy_bukva(b))








#PRO: LIGHT +
#4.  В файле с логами найти дату самого позднего лога (по метке времени)

text='''
2011-08-01 18:03:34,338 - exampleApp - INFO - Program started
2012-09-02 19:13:53,338 - exampleApp - INFO - added 7 and 8 to get15
2012-10-02 20:23:31,338 - exampleApp - INFO - Done!
2013-08-01 01:43:33,338 - exampleApp - INFO - Program started
2011-09-19 12:53:33,338 - exampleApp - INFO - added 10 and 11 to get15
2012-10-12 22:03:33,338 - exampleApp - INFO - Done!
2017-08-01 01:13:51,338 - exampleApp - INFO - Program started
2019-09-19 12:21:34,338 - exampleApp - INFO - added 7 and 8 to get15
2018-10-12 23:31:01,338 - exampleApp - INFO - Done!
'''
#https://andreyex.ru/yazyk-programmirovaniya-python/uchebnik-po-python-3/python-3-vremya-metod-strptime/
from datetime import datetime
#помещаем файл в папку с проектом!!!!!
with open('log.csv','r') as file:
    last_date =()
    for line in file:
        if not last_date:
            last_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
            continue
        date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
        if date > last_date:
            last_date = date
print(last_date)
