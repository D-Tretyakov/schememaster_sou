from django.http import HttpResponse
from django.shortcuts import render
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

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
    ans[1] = re.split('\n',ans[1][0])
    for i in ans[1]:
        p = document.add_paragraph(i)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if ans[2] != ['']:
        ans[2] = re.split(r'[1]\d*.|\n[2,3]\d*.|\n',ans[2][0])
        ans[2].pop(0)
        res = re.split('\n',ans[2][0])
        ans[2]=ans[2][1]
        for i in res:
            p = document.add_paragraph(i)
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT 
    ans[3] = re.split('\n',ans[3][0])
    for i in ans[3]:
        p = document.add_paragraph(i)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT   
    if ans[4] != ['']:
        ans[4] = re.split('\n',ans[4][0])
        for i in ans[4]:
            p = document.add_paragraph(i)
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT 
    if ans[5] != ['']:
        p = document.add_paragraph('{{price_isk}}')
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if ans[6] != ['']:
        p = document.add_paragraph('{{poshlina}}')
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = document.add_paragraph("Исковое заявление")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ans[7] = re.split(r'[1]\d*.|\n[2,3]\d*.|\n',ans[7][0])
    ans[7].pop(0)
    print(ans[7])
    ans[8] = re.split(r'[1]\d*.|\n[2,3]\d*.|\n',ans[8][0])
    ans[8].pop(0)
    p = document.add_paragraph("о {{demand_1}}")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph("ПРОШУ:")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('1. {{demand_2}}')
    document.add_paragraph('2. {{dop_demand_1}}')
    if ans[11]!= ['']:
        document.add_paragraph('3. {{potrebiteli}}')
    document.add_paragraph('Приложение:')
    if ans[6] != ['']:
        document.add_paragraph('Платежное поручение №___ от «__»______ ____ г., подтверждающее уплату государственной пошлины.\n\n« » ________ _____г. _____________ (________________)', style = 'List Number')
    document.add_paragraph('Копия уведомления о вручении или иные документы, подтверждающие направление другим лицам, участвующим в деле, копий искового заявления и приложенных к нему документов, которые у других лиц, участвующих в деле, отсутствуют;', style = 'List Number')
    document.add_paragraph('Иные документы, на которых Истец обосновывает свои требования;', style = 'List Number')
    if ans[2]!= ['']:
        document.add_paragraph('{{complainant}}', style = 'List Number')
    document.add_paragraph('{{demand_3}}', style = 'List Number')
    if len(ans[7]) > 3:
        document.add_paragraph(ans[7][3])
    document.add_paragraph('{{dop_demand_2}}', style = 'List Number')
    if ans[9] != ['']:
        document.add_paragraph('{{regulation}}', style = 'List Number')
    if ans[10] != ['']:
        document.add_paragraph('{{peace}}', style = 'List Number')
    document.add_paragraph('« » ________ _____г. \t\t\t\t\t\t_____________ (________________)')
    document.save('demo.docx')
    document = DocxTemplate("demo.docx")
    context = { 'court' : ans[0][0],'complainant':ans[2], 'price_isk':ans[5][0],'poshlina':ans[6][0], 'demand_1':ans[7][0], 'demand_2':ans[7][1], 'dop_demand_1':ans[8][0], 'demand_3':ans[7][2], 'dop_demand_2':ans[8][1], 'regulation':ans[9][0], 'peace':ans[10][0], 'potrebiteli':ans[11][0]}
    document.render(context)
    document.save("demo.docx") 

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
