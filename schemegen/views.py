from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tree, Choice, Variant, Schema
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

def from_frontend(request):
    k = {
        'Физическое лицо': '_______\nАдрес: ______\nИНН: ______',
        'Юридическое лицо': '________\nАдрес: _______\nОГРН:_______\nИНН: ________',
        'Государственный орган (орган местного самоуправления)': '________\nАдрес: ______',
        'Индивидуальный предприниматель': 'ИП _______\nАдрес: _______\nОГРНИП: ______\nИНН: ______'
    }
    d = {
        'c1-v1': k['Физическое лицо'],
        'c1-v2': k['Юридическое лицо'],
        'c1-v3': k['Государственный орган (орган местного самоуправления)'],
        'c1-v4': k['Индивидуальный предприниматель'],

        'c2-v1': '',
        'c2-v2': 'Есть',
        'c2-v3': k['Физическое лицо'],
        'c2-v4': k['Юридическое лицо'],
        'c2-v5': k['Государственный орган (орган местного самоуправления)'],
        'c2-v6': k['Индивидуальный предприниматель'],

        'c3-v1': k['Физическое лицо'],
        'c3-v2': k['Юридическое лицо'],
        'c3-v3': k['Государственный орган (орган местного самоуправления)'],
        'c3-v4': k['Индивидуальный предприниматель'],

        'c4-v1': '',
        'c4-v2': 'Есть',
        'c4-v3': k['Физическое лицо'],
        'c4-v4': k['Юридическое лицо'],
        'c4-v5': k['Государственный орган (орган местного самоуправления)'],
        'c4-v6': k['Индивидуальный предприниматель'],

        'c5-v1': 'Цена иска: ______',
        'c5-v2': '',

        'c6-v1': '________',
        'c6-v2': 'не взимается',
        'c6-v3': 'не взимается',
        'c6-v4': 'не взимается',
        'c6-v5': 'не взимается',
        'c6-v6': 'не взимается',
        'c6-v7': 'не взимается',
        'c6-v8': 'не взимается',
        'c6-v9': 'не взимается',
        'c6-v10': 'не взимается',
        'c6-v11': 'не взимается',
        'c6-v12': 'не взимается',
        'c6-v13': 'не взимается',
        'c6-v14': 'не взимается',
        'c6-v15': 'не взимается',
        'c6-v16': 'не взимается',
        'c6-v17': 'не взимается',
        'c6-v18': 'не взимается',
        'c6-v19': 'не взимается',
        'c6-v20': 'не взимается',
        'c6-v21': 'не взимается',
        'c6-v22': 'не взимается',
        'c6-v23': 'не взимается',
        'c6-v24': 'не взимается',
        'c6-v25': 'не взимается',
        'c6-v26': 'не взимается',
        'c6-v27': 'не взимается',
        'c6-v28': 'не взимается',
    }

    schema = """
<div style='text-align: right;'>В __________

Адрес:_______

{0}

{3}

{1}

{2}

Цена иска: ______\n Госпошлина: {5} </div>

<div style='text-align: center;'> ИСКОВОЕ ЗАЯВЛЕНИЕ

о ________ 

ПРОШУ: </div>

Приложение: 
{6}

{7} 
    """

    req = dict(request.POST)
    res = {}
    for choice in req:
        i = int(choice.split('-')[1])
        res[i] = d[req[choice][0]]
    
    ans = [res[key] for key in sorted(res.keys())]
    ans += ['1. Копия доверенности или иного документа, подтверждающего полномочия представителя' if res[2] else '']
    ans += ['2. Платежное поручение №___ от «__»______ ____ г., подтверждающее уплату государственной пошлины.\n\n« » ________ _____г. _____________ (________________)'
            if res[6] != 'не взимается' else '']
    text = schema.format(*ans)

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