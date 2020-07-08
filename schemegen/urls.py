from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kek', views.kek, name='kek'),
    path('<int:choice_id>/', views.detail, name='detail'),
    path('convert/', views.convert, name='convert'),
]