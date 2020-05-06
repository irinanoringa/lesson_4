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
    else: 'break'  # Здесь 'break' проходит только в ковычках...почему?

def max_simple_delitel(a):
    '''Возвращает самый большой простой делитель числа.'''
    list=vse_deliteli(a)
    list_max=[]
    for i in range(1,len(list)):
        if simple_numbers(list[i]):list_max == list_max.insert(i,list[i])

    return max(list_max)

print(simple_numbers(36))
print(vse_deliteli(36))
print(max_simple_delitel(36))



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

print(simple_deliteli(36))



def max_delitel(a):
    '''
    Функция выводит самый большой множитель (не обязательно простой) числа.
    '''
    x=simple_deliteli(a) # выводит все множетели числа а
    x.reverse()   # меняет порядок
    return x[0]   # выводит самый первый

print(max_delitel(36))