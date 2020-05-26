            #    ТЕСТИРОВАНИЕ ФУНКЦИЙ
            #    ТЕСТИРУЕМ УРОК 5

def simple_numbers(a):
    '''На входе-натуральные числа от 0 до 1000.
    Функция проверяет числа на простоту.
    '''
    if 0<a<=1000:
        for i in range(2,a+1):
            if a%i==0: break
        return a==i



def vse_deliteli(a):
    '''На входе-натуральные числа от 0 до 1000.
    Возвращает список всех делителей числа.
    '''
    if 0<a<=1000:
        list_del=[]
        for i in range(1,a+1):
            if a%i==0: list_del==list_del.insert(i,i)
        return(list_del)
    else: 'break'
print(vse_deliteli(8))
print(vse_deliteli(1001))
print(vse_deliteli(0))

def test_poluavtomat_1_2_3():
    a=8
    a_out=vse_deliteli(a)
    if  a_out==[1, 2, 4, 8]:
        print('test 1 is OK')
    else: print('test 1 is failed')

    a=1001
    a_out=vse_deliteli(a)
    if  a_out==None:
        print('test 2 is OK')
    else: print('test 2 is failed')

    a=0
    a_out=vse_deliteli(a)
    if  a_out==None:
        print('test 3 is OK')
    else: print('test 3 is failed')

test_poluavtomat_1_2_3()



def max_simple_delitel(a):
    '''Возвращает самый большой простой делитель числа.'''
    list=vse_deliteli(a)
    list_max=[]
    for i in range(1,len(list)):
        if simple_numbers(list[i]):list_max == list_max.insert(i,list[i])

    return max(list_max)
print(max_simple_delitel(8))

def test_poluavtomat_4():
    a=8
    a_out=max_simple_delitel(a)
    if a_out==2:
        print('test 4 is OK')
    else:print('test 4 is faild')

test_poluavtomat_4()



def simple_deliteli(a):
    '''
    Возвращает каноническое разложение числа на простые множители.
    '''
    if 0<a<=1000:
        list_simple_delitelei=[]
        for i in range(2,a):
            while simple_numbers(i)==1 and a%i==0:
                list_simple_delitelei.append(i) #список простых делителей 'a'
                a=a/i
            else:
                i+=1

    return list_simple_delitelei

print(simple_deliteli(12))
#print(simple_deliteli(0))

def test_poluavtomat_5():
    a=12
    a_out=simple_deliteli(a)
    if a_out==[2,2,3]:
        print('test 5 is OK')
    else:print('test 5 is faild')

test_poluavtomat_5()


def max_delitel(a):
    '''
    Функция выводит самый большой множитель (не обязательно простой) числа.
    '''
    x=simple_deliteli(a) # выводит все множетели числа а
    x.reverse()   # меняет порядок
    return x[0]   # выводит самый первый

print(max_delitel(12))


def test_poluavtomat_6():
    a=12
    a_out=max_delitel(a)
    if a_out==3:
        print('test 6 is OK')
    else:print('test 6 is faild')
test_poluavtomat_6()

                       # Тестируем функции урока №4


from random import choices

def choices_name(new_list_names,N=100):
    '''Задается список имен - list_names и целое число - N.
    Возвращает список длины N случайных имен.'''
    return choices(new_list_names,k=N)

new_list_names = ['Ваня','Дима','Лена','Ира','Игорь','Ян','Маша','Даша','Наташа','Вася']
b=choices_name(new_list_names)
print(b)

def test_choices():
    a=['Ваня','Дима','Лена','Ира','Игорь','Ян','Маша','Даша','Наташа','Вася']
    a_out=len(choices_name(a))
    if a_out==100:
        print('test 7 is OK')
    else:print('test 7 is faild')

test_choices()


def often_word(listik):
    '''Задается список listik.
    Возвращает самый частый элемент списка'''
    global c_dict
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
#print(often_word(b))

def test_often_word():
    a=choices_name(new_list_names)
    a_out=often_word(a)
    if 'Ваня' in c_dict:
        print('test 8 is OK')
    else:print('test 8 is faild')

test_often_word()

