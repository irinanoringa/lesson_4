
import timeit


code_to_test ='''
import datetime
from docxtpl import DocxTemplate

with open ('dog','r', encoding="utf-8") as f:
    list_dog = f.read()
a = ','
list_dog = list_dog.replace(', ',a)
list_dog = list_dog.split(',')
list_dog = list(list_dog)
company = list_dog[0]
poroda_list = list_dog[1]
old_list = list_dog[2]
weith_list = list_dog[3]

def get_context(company, poroda_list, old_list,  weith_list): # возвращает словарь аргуменов
    return {
        'company': company,
        'poroda': poroda_list,
        'old': old_list,
        'weith': weith_list,
    }
def from_template(company, poroda_list, old_list, weith_list, template):
    template = DocxTemplate(template)
    context = get_context(company, poroda_list, old_list, weith_list)  # gets the context used to render the document

    template.render(context)
    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(company, poroda_list, old_list, weith_list):
    template = 'shablon.docx' # название шаблона
    document = from_template(company, poroda_list, old_list, weith_list, template)

generate_report(company, poroda_list, old_list, weith_list)
'''
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print('время 1ого кода равно',elapsed_time)




code_to_test_2='''
import csv


dogs=[['poroda','weight','old'],['layika',25,18],['mops',11,8]]

with open ('dog.csv','w') as d:
    writer = csv.writer(d, delimiter = '-')
    writer.writerows(dogs)
'''
elapsed_time_2 = timeit.timeit(code_to_test_2, number=100)/100
print('время 2ого кода равно',elapsed_time_2)


code_to_test_3='''
import json


dogs={'poroda':'layika','weight':25,'old':18}

with open ('dog.txt','w') as c:
    json.dump(dogs,c)
'''
elapsed_time_3 = timeit.timeit(code_to_test_3, number=100)/100
print('время 3ого кода равно',elapsed_time_3)