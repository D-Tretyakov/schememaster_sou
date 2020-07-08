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
    result = [Variant.objects.get(id=int(request.POST[f'variant_choice{i}'])).text_repr
               for i in range(1, len(Choice.objects.all())+1)]
    return HttpResponse(str(result))


# def get_choices(request):
#     choices = Choice.objects.all()
#     query
