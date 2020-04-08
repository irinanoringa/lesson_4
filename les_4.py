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
    #print(list(c_dict.values()))   #  выводит список значений
    e=max(list(c_dict.values()))
    #print(max(list(c_dict.values())))  #  выводит максим значение из списка
    #print(c_dict[2])
    for key,values in d:
        if values == e:
           # return(key,':',values) ВЫВОДИТ СПИСОК, ПРИЧЕМ ЕСЛИ ОДИНАКОВЫХ МАКС ЗНАЧЕНИЙ БОЛЕЕ ОДНОГО ТО ВЫВОДИТ ТОЛЬКО 1 КЛЮЧ И ЭТО ЗНАЧЕНИЕ,ЗАБЫВАЯ ПРО ДРУГИЕ КЛЮЧИ С ТАКИМ ЖЕ ЗНАЧЕНИЕМ. ПОЧЕМУ?
           print(key,':',values) # но тут в выводе пишет верно и выводит несколько ключей при равных макс значениях, но еще выводи None!!! КАК БЫТЬ???

print(often_word(b))


            # 3 Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функц (F)
def redkaiy_bukva(names):
    '''
    :param names: Задаем список имен
    :return: Самую редкую букву, с которой начинаются имена
    '''

    c_dict={}
    for i in range (len(b)):
        c_dict[b[i]]=0
    for sym in b:
        c_dict[sym]+=1
    print(c_dict)  # выводит словарь
    d=list(c_dict.items())
    e=min(list(c_dict.values())) # мин значение
    #print(min(list(c_dict.values())))  #  выводит мин значение из списка
    for key,values in d:
        if values == e:
            #print(key,':',values)
            print((key)[0]) # разберись с print и return

# прога работает, но если Игорь и Ира выпадает по 1 разу,то выводит И И, а надо ведь 1 букву И.
 #У меня мозг закпел не пойму как их в строку чтоли собрать чтобы делать дальше или как быть

    #print(list(c_dict.keys()))
   #a=list(c_dict.keys()) # список ключей

print(redkaiy_bukva(b))

#PRO:

#LIGHT +

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
