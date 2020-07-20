from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tree, Choice, Variant, Schema, Template, TextAlias
from .serializers import TreeSerializer, ChoiceSerializer, VariantSerializer, SchemaSerializer


def index(request):
    latest_choice_list = Choice.objects.all()
    context = {'latest_choice_list': latest_choice_list}
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
    p = document.add_paragraph('{{complainant_1}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph('{{otvetchik}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph('{{third}}')
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
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
    document.add_paragraph('{{posh}}', style = 'List Number')
    document.add_paragraph('Копия уведомления о вручении или иные документы, подтверждающие направление другим лицам, участвующим в деле, копий искового заявления и приложенных к нему документов, которые у других лиц, участвующих в деле, отсутствуют;', style = 'List Number')
    document.add_paragraph('Иные документы, на которых Истец обосновывает свои требования;', style = 'List Number')
    document.add_paragraph('{{complainant_2}}', style = 'List Number')
    document.add_paragraph('{{demand_3}}', style = 'List Number')
    document.add_paragraph('{{dop_demand_2}}', style = 'List Number')
    document.add_paragraph('{{regulation}}', style = 'List Number')
    document.add_paragraph('{{peace}}', style = 'List Number')
    document.add_paragraph('« » ________ _____г. \t\t\t\t\t\t\t\t_____________ (________________)')
    document.save('demo.docx')
    document = DocxTemplate("demo.docx")
    context = { 'court' : ans[0],'complainant_1':ans[1][0], 'otvetchik':ans[2],'third':ans[3],'price_isk':ans[4],'poshlina':ans[5], 'demand_1':ans[6][0], 'demand_2':ans[6][1], 'dop_demand_1':ans[7][0], 'potrebiteli':ans[8], 'posh':ans[9], 'complainant_2':ans[1][1], 'demand_3':ans[6][2], 'dop_demand_2':ans[7][1], 'regulation':ans[10], 'peace':ans[11]}
    document.render(context)
    document.save("demo.docx") 
    text = """Шаблон успешно скачан"""
    return HttpResponse(text.replace('\n', '<br>')) 

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
    ans = [res[key] for key in sorted(res.keys())]
    ans += ['1. Копия доверенности или иного документа, подтверждающего полномочия представителя' if res[2] else '']
    ans += ['2. Платежное поручение №___ от «__»______ ____ г., подтверждающее уплату государственной пошлины.\n\n« » ________ _____г. _____________ (________________)'
            if res[6] != 'не взимается' else '']
    text = schema.format(*ans)
    convertion(text)
    return HttpResponse(text.replace('\n', '<br>'))

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
