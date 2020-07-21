from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
import json

from .models import Tree, Choice, Variant, Schema, Template, TextAlias
from .serializers import TreeSerializer, ChoiceSerializer, VariantSerializer, SchemaSerializer


def index(request):
    context = {}
    return render(request, 'schemegen/index.html', context)

def get_tree(request, tree_id):
    tree_ids = {tree.id: tree.name for tree in Tree.objects.all()}
    tree = Tree.objects.get(id=tree_id)
    context = {'tree': tree, 'tree_ids': tree_ids}
    return render(request, 'schemegen/tree.html', context)

def convert(request, tree_id):
    print(request.POST)
    result = [Variant.objects.get(id=int(request.POST[f'variant_choice{c.id}'])).text_repr
            for c in Tree.objects.get(id=tree_id).choice_set.all()]
    text = Tree.objects.get(id=tree_id).schema_set.all()[0].text_repr.format(*result)

    return HttpResponse(text.replace('\n', '<br>'))

def convertion(ans):
    document = Document()     
    document.save('demo.docx')  
    p = document.add_paragraph("В___________________")
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph("Адрес:_____________________")
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph('{{court}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if ans[1] != ['','']: 
        p = document.add_paragraph('{{complainant_1}}')
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph('{{otvetchik}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if ans[3] != '':
        p = document.add_paragraph('{{third}}')
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if ans[4] != '':
        p = document.add_paragraph('{{price_isk}}')
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph('{{poshlina}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph("Исковое заявление")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph("о {{demand_1}}")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph("ПРОШУ:")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('{{demand_2}}')
    document.add_paragraph('{{dop_demand_1}}')
    document.add_paragraph('{{potrebiteli}}')
    document.add_paragraph('Приложение:')
    if ans[9] != '':
        document.add_paragraph('Платежное поручение №___ от «__»______ ____ г., подтверждающее уплату государственной пошлины.\n\n« » ________ _____г. _____________ (________________)', style = 'List Number')
    document.add_paragraph('Копия уведомления о вручении или иные документы, подтверждающие направление другим лицам, участвующим в деле, копий искового заявления и приложенных к нему документов, которые у других лиц, участвующих в деле, отсутствуют;', style = 'List Number')
    document.add_paragraph('Иные документы, на которых Истец обосновывает свои требования;', style = 'List Number')
    if ans[1] != ['','']:
        document.add_paragraph('{{complainant_2}}', style = 'List Number')
    document.add_paragraph('{{demand_3}}', style = 'List Number')
    document.add_paragraph('{{dop_demand_2}}', style = 'List Number')
    if ans[10] != '':
        document.add_paragraph('{{regulation}}', style = 'List Number')
    if ans[11] != '':
        document.add_paragraph('{{peace}}', style = 'List Number')
    document.add_paragraph('« » ________ _____г. \t\t\t\t\t\t\t\t_____________ (________________)')
    document.save('demo.docx')
    document = DocxTemplate("demo.docx")
    print(repr(ans))
    context = { 'court' : ans[0],'complainant_1':ans[1][0], 'otvetchik':ans[2],'third':ans[3],'price_isk':ans[4],'poshlina':ans[5], 'demand_1':ans[6][0], 'demand_2':ans[6][1], 'dop_demand_1':ans[7][0], 'potrebiteli':ans[8], 'posh':ans[9], 'complainant_2':ans[1][1], 'demand_3':ans[6][2], 'dop_demand_2':ans[7][1], 'regulation':ans[10], 'peace':ans[11]}
    document.render(context)
    document.save("demo.docx") 
    # text = """Шаблон успешно скачан"""
    # return HttpResponse(text.replace('\n', '<br>')) 

def get_text(request):
    template = Template.objects.first()
    header = "<div style='text-align: right;'>" + template.header + "</div>"
    body = "<div style='text-align: center;'>" + template.body + "</div>"
    footer = template.footer

    schema = header + body + footer
    
    req = dict(request.POST)
    res = {}
    for choice in req:
        i = int(choice.split('-')[1])
        answer = []
        for j in req[choice]:
            answer.append(TextAlias.objects.get(html_id=j).text)
            res[i] = answer 
    ans = []
    for key in sorted(res.keys()):
      ans += res[key]

    text = schema.format(*ans)
    # convertion(ans)
    # text = """Шаблон успешно скачан"""
    return HttpResponse(text.replace('\n', '<br>'))

@api_view(['POST'])
def pretty_print(request):   
    req = dict(request.POST)
    del req['csrfmiddlewaretoken']
    
    res = {}
    for choice in req:
        i = int(choice.split('-')[1])
        answer = []
        for j in req[choice]:
            answer.append(TextAlias.objects.get(html_id=j).text)
            res[i] = answer 
    ans = []
    for key in sorted(res.keys()):
      ans.append(res[key])

    return Response({
        'req': req,
        'res':res,
        'ans': ans,
    })

# def get_text(request):
#     template = Template.objects.first()
#     header = "<div style='text-align: right;'>" + template.header + "</div>"
#     body = "<div style='text-align: center;'>" + template.body + "</div>"
#     footer = template.footer

#     schema = header + body + footer
    
#     req = dict(request.POST)
#     res = {}
#     for choice in req:
#         i = int(choice.split('-')[1])
#         res[i] = TextAlias.objects.get(html_id=req[choice][0]).text
   
#     ans = [res[key] for key in sorted(res.keys())]
#     ans += ['1. Копия доверенности или иного документа, подтверждающего полномочия представителя' if res[2] else '']
#     ans += ['2. Платежное поручение №___ от «__»______ ____ г., подтверждающее уплату государственной пошлины.\n\n« » ________ _____г. _____________ (________________)'
#             if res[6] != 'не взимается' else '']
#     text = schema.format(*ans)

#     return HttpResponse(text.replace('\n', '<br>'))

@api_view()
def pass_func(request):
    template = Template.objects.first()
    header = "<div style='text-align: right;'>" + template.header + "</div>"
    body = "<div style='text-align: center;'>" + template.body + "</div>"
    footer = template.footer

    schema = header + body + footer

    return Response({'text': schema})

@api_view()
def get_full_tree(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    
    return Response({
        'tree_name': tree.name,
        'choices': { choice.choice_text : 
            [variant.variant_text for variant in choice.variant_set.all()]
            for choice in tree.choice_set.all()}
    })

class TreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class VariantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class SchemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer



d = {
    'c0-v1': 'Мировому судье судебного участка № ____',
    'c0-v2': 'В __________районный суд г. _______',
    'c0-v3': 'В _________________ гарнизонный военный суд',
    'c0-v4': 'В _________(верховный суд республики /краевой/ областной суд/ суд города федерального значения/суд автономной области/суд автономного округа) ___________(указать республику /край/область/город федерального значения/автономную область/ автономный округ)',

    'c7-v1': '1) взыскании денежных средств\n2) Взыскать с Ответчика в пользу Истца денежные средства ______ (основание требования о взыскании) в размере ______ (______) руб.\n3) Расчет взыскиваемой суммы за период с «__»____ ____г. по «__»____ ___г.\nКопия договора от __________.',
    'c7-v2': '', 
    'c7-v3': '1) возврате неосновательно переданного права\n2) Обязать Ответчика вернуть Истцу неосновательно переданное право ______.\nОбязать Ответчика вернуть Истцу документы, удостоверяющие переданное право, а именно ______.',
    'c7-v4': '1) возврате неосновательно переданного права\n2) Обязать Ответчика вернуть Истцу неосновательно переданное право ______.\nОбязать Ответчика вернуть Истцу документы, удостоверяющие переданное право, а именно ______.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.\nКопия договора от ______.',
    'c7-v5': '1) возврате неосновательно переданного права\n2) Обязать Ответчика вернуть Истцу неосновательно переданное право ______.\nОбязать Ответчика вернуть Истцу документы, удостоверяющие переданное право, а именно ______.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.',
    'c7-v6': '1) возврате неосновательного обогащения',
    'c7-v7': '1) возврате неосновательного обогащения\n2) Обязать Ответчика вернуть Истцу неосновательно приобретенное имущество ______.\nОбязать Ответчика вернуть Истцу сопроводительную документацию к неосновательно приобретенному имуществу, а именно ______.',
    'c7-v8': '1) возврате неосновательного обогащения\n2) Обязать Ответчика вернуть Истцу неосновательно приобретенное имущество ______.\n',
    'c7-v9': '1) возврате неосновательного обогащения\n2) Обязать Ответчика вернуть Истцу неосновательно приобретенное имущество ______.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.\nКопия договора от ______.',
    'c7-v10': '1) возврате неосновательного обогащения\n2) Обязать Ответчика вернуть Истцу неосновательно приобретенное имущество ______.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.',
    'c7-v11': '1) взыскании неосновательного обогащения\n2) Взыскать с Ответчика в пользу Истца неосновательное обогащение в размере ______ (______) руб.',
    'c7-v12': '1) взыскании неосновательного обогащения\n2) Взыскать с Ответчика в пользу Истца неосновательное обогащение в размере ______ (______) руб.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.\nРасчет суммы неосновательного обогащения.\nКопия договора от ______.',
    'c7-v13': '1) взыскании неосновательного обогащения\n2) Взыскать с Ответчика в пользу Истца неосновательное обогащение в размере ______ (______) руб.\n3) Копия документа, подтверждающее неосновательное обогащение Ответчика.\nРасчет суммы неосновательного обогащения.',
    'c7-v14': '1) возмещении вреда, причиненного _______ (объект посягательства)\n2) Обязать Ответчика возместить Истцу вред, причиненный ______ (объект посягательства) в размере _______ (_____) руб.\n3) Расчет суммы исковых требований.\nДокументы, подтверждающие причинение истцу _______ вреда',
    'c7-v15': '1) возмещении убытков\n2) Взыскать с Ответчика в пользу Истца убытки в размере _______ (_____) руб. 3) Расчет суммы исковых требований.\nДокументы, подтверждающие причинение истцу убытков.',
    'c7-v16': '1) о признании недействительной сделки и применении последствий ее недействительности\n2) Признать недействительным договор ________________ и применить последствия недействительности сделки в виде ____________________.\n3) Обязать Ответчика_________________________\n1. Копии документов, подтверждающих заключение сделки (соглашения), от "__"___________ ____ г.\n2. Документы, подтверждающие нарушение прав и законных интересов Истца.\n3. Документы, подтверждающие наступление неблагоприятных последствий для Истца.',
    'c7-v17': '1) о признании права собственности на недвижимое имущество\n2) Признать право собственности истца на _____________________________ (указать недвижимое имущество).\n1. Копия технического паспорта (технической документации и т.д.) на объект недвижимости от "___"________ ____ г. с приложениями.\n2. Документы, подтверждающие возникновение права истца на объект недвижимости.\n3. Выписка из единого государственного реестра недвижимости об объекте недвижимости\n3) Исковое заявление о признании права собственности на движимую вещь',
    'c7-v18': '1) восстановлении в праве\n2) Восстановить истца в ___________ праве в отношении __________.\n3) Копия документа, подтверждающее правовое основание права.',
    'c7-v19': '1) восстановлении на работе\n2) Восстановить истца ____________ (ФИО) на работе в (у) _____________ (наименование работодателя) в должности ______________.\nВзыскать с ________________ (наименование работодателя) в пользу истца средний заработок за время вынужденного прогула с «__»_____ ____г. по «__»_____ ____г. в сумме _________(______) руб.\n3) Копия приказа о приеме истца на работу.\nКопия трудового договора №__ от «__»_____ ____г.\nКопия приказа об увольнении истца с работы.\nДокументы, подтверждающие обоснованность доводов истца о незаконности увольнения (заключения специалистов, материалы проверок, объяснения свидетелей и т.д.)\nСправка о заработной плате истца за фактически проработанное время.\nРасчет заработной платы за время вынужденного прогула',
    'c7-v20': '1) восстановлении срока\n2) Восстановить срок для ________________(цель).\n3) Копия документа, подтверждающего уважительные причины пропуска срока __________ (какой срок, для чего).',
    'c7-v21': '1) Об обязании нотариуса совершить нотариальное действие…\n2) Обязать нотариуса ________________ нотариального участка ____________совершить нотариальное действие…\n3) * если иск связан с наследственными правоотношениями – то Копия свидетельства о смерти Наследодателя от "___"_________ ____ г.',
    'c7-v22': '1) Об обязании исполнить обязательство в натуре по договору\n2) Исполнить в натуре обязательство по Договору от "__"________ ____ г. N ____.)\n3)\n1. Копия Договора от "__"___________ ____ г. N ____.)\n2. Доказательства исполнения обязательств по Договору от "__"___________ ____ г. N ____.) Истцом\n3. Доказательства неисполнения (ненадлежащего исполнения) обязательств по Договору от "__"___________ ____ г. N ____.) Ответчиком',
    'c7-v23': '1) Об обязании устранить недостатки работ по договору\n2) Обязать Ответчика безвозмездно устранить недостатки работ, выполненных им по Договору от "__"___________ ____ г. N ____.)\n3) Копия Договора от "__"___________ ____ г. N ____.)',
    'c7-v24': '1) Об обязании передать индивидуально-определенную вещь в соответствии с условиями договора\n2) Обязать Ответчика передать Истцу вещь в соответствии с Договором от "__"___________ ____ г. N ____.)\n3)\n1. Копия Договора (или иного правоустанавливающего документа) N ___ от "__"________ ___ г.\n2. Доказательства невыполнения Ответчиком обязательств по передаче Вещи в установленный Договором срок\n3. Копия документа, иного материала, подтверждающего нахождение Вещи у Ответчика (или: на хранении, в безвозмездном пользовании у третьего лица).',
    
    'c8-v1': '1) Взыскать с Ответчика в пользу Истца проценты за пользование чужими денежными средствами в размере ________ (_______) руб.\n2) Расчет взыскиваемой суммы за период с «__»____ ____г. по «__»____ ___г.',
    'c8-v2': '1) Взыскать с Ответчика в пользу Истца неустойку в размере ________ (_______) руб.\n2) Расчет взыскиваемой суммы за период с «__»____ ____г. по «__»____ ___г.',
    'c8-v3': '1) Взыскать с Ответчика в пользу Истца неустойку в размере ________ (_______) руб.\n2) Копия документа, обосновывающего размер компенсации морального вреда (если есть).',
    'c8-v4': '1) Взыскать с Ответчика в пользу Истца расходы на оплату услуг представителя в размере _______ (_____________) рублей.\n2) Документы, подтверждающие оплату услуг представителя.',

    'c9-v1': 'Копия претензии от ________',
    'c9-v2': '',

    'c10-v1': 'Копия документа, подтверждающие совершение стороной (сторонами) действий, направленных на примирение, если такие действия предпринимались и соответствующие документы имеются',
    'c10-v2': '',

    'c11-v1': '',
    'c11-v2': 'Взыскать с Ответчика в пользу Истца штраф за отказ в удовлетворении требований в добровольном порядке в размере 50 % от суммы исковых требований',
    'c11-v3': '',
    'c11-v4': '',
}