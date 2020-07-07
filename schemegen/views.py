from django.http import HttpResponse
from django.shortcuts import render

from .models import Choice


def detail(request, choice_id):
    return HttpResponse("You're looking at choice %s." % choice_id)

def index(request):
    latest_choice_list = Choice.objects.all()[:5]
    context = {'latest_choice_list': latest_choice_list}
    return render(request, 'schemegen/index.html', context)