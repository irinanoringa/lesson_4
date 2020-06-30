# декоратор

from datetime import datetime
import time
import sys

def showtime(func):
    def show_t(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(time.time()-start)
        return result
    return show_t

def timesize(func):
    '''
    :param func: исполняеый код
    :return: время исполнения кода
    '''
    def times(*args,**kwargs):
        start=datetime.now()
        result=func(*args,**kwargs)
        print(datetime.now()- start)
        return result
    return times

def volumesize(func):
    '''
    :param func: исполняемый код
    :return: обьем оперативной памяти
    '''
    def volumes(*args,**kwargs):

        result=func(*args,**kwargs)
        vol=sys.getsizeof(result))
        return vol
    return volumes



@timesize
@showtime

def spisok_generator(n):
    g=(i for i in range(n+1))
    return g

too_1=spisok_generator(1000000)
print(type(too_1))
print(sys.getsizeof(too_1))




@timesize
@showtime
def spisok_list(n):
    l=[]
    for i in range(n+1):
        l.append(i)
    return l

too_2=spisok_list(1000000)
print(type(too_2))
print(sys.getsizeof(too_2))