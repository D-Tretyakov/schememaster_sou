from django.http import HttpResponse
from django.shortcuts import render
import json

from .models import Choice, Variant


def detail(request, choice_id):
    return HttpResponse("You're looking at choice %s." % choice_id)

def index(request):
    latest_choice_list = Choice.objects.all()
    context = {'latest_choice_list': latest_choice_list}
    return render(request, 'schemegen/index.html', context)

def kek(request):
    latest_choice_list = Choice.objects.all()
    context = {'latest_choice_list': latest_choice_list}
    return render(request, 'schemegen/kek.html', context)

def convert(request):
    result = [Variant.objects.get(id=int(request.POST[f'variant_choice{c.id}'])).text_repr
            for c in Choice.objects.all()]
    document = Document()     
    document.save('demo.docx')   
    document.add_heading("\t\t\tИсковое заявление", 0)
    document.add_paragraph('\t\tо расторжении брака и разделе общего имущества супругов ')
    p = document.add_paragraph('Истец вступил(а) в брак с ответчиком ____________________________. (число, месяц, год). Брак зарегистрирован __________________________ (наименование органа ЗАГСа), актовая запись N ____ {{child}}')
    p.add_run('Совместная жизнь истца и ответчика не сложилась _______________________________________________________________. (указать причины)')
    p.add_run('Брачные отношения между истцом и ответчиком прекращены с ______________________, общее хозяйство не ведется. (год, месяц)')
    p.add_run('Примирение между истцом и ответчиком невозможно. {{argue}} Ответчик на расторжение брака {{answer}} ___________')
    p.add_run('{{divide}} Общая стоимость совместно нажитого имущества составляет ___________ рублей, что подтверждается _______________')
    p.add_run('{{liability}}В соответствии со ст. 39 Семейного кодекса Российской Федерации при разделе общего имущества супругов и определении долей в этом имуществе доли супругов признаются равными, если иное не предусмотрено договором между супругами.')
    p.add_run('Суд вправе отступить от начала равенства долей супругов в их общем имуществе исходя из интересов несовершеннолетних детей и (или) исходя из заслуживающего внимания интереса одного из супругов, в частности в случаях, если другой супруг не получал доходов по неуважительным причинам или расходовал общее имущество супругов в ущерб интересам семьи.')
    p.add_run('Общие долги супругов при разделе общего имущества супругов распределяются между супругами пропорционально присужденным им долям. На основании вышеизложенного и в соответствии со ст. ст. 23 (22), 38, 39 Семейного кодекса Российской Федерации, руководствуясь п. 1 ст. 98, ст. ст. 131, 132 Гражданского процессуального кодекса Российской Федерации,')
    p = document.add_paragraph('ПРОШУ:')
    document.add_paragraph('Расторгнуть брак между истцом и ответчиком, зарегистрированный _______________________ (дата регистрации брака) в _______________________ (наименование органа ЗАГСа), актовая запись N __________.',style = 'List Number')
    p = document.add_paragraph('Разделить имущество, являющееся общей совместной собственностью, выделив истцу _____________________________________________________________(наименование вещей, стоимость каждого предмета) на общую сумму ______________ рублей.',style = 'List Number')
    p.add_run('Ответчику выделить____________________________________________________(наименование вещей, стоимость каждого предмета) на общую сумму ______________ рублей.')
    document.add_paragraph('Общие долги распределить между истцом и ответчиком пропорционально присужденным долям следующим образом: ____________________.', style = 'List Number')
    document.add_paragraph('{{money}}', style = 'List Number')
    document.save('demo.docx')
    document = DocxTemplate("demo.docx")
    context = { 'child' : result[0],'argue':result[1], 'answer':result[2],'divide':result[3],'liability':result[4],'money':result[5]}
    document.render(context)
    document.save("demo.docx") 
    text = """Ваш шаблон успешно скачан""".format(*result)
    return HttpResponse(text)  
