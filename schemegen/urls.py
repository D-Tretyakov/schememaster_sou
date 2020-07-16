from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convert/<int:tree_id>', views.convert, name='convert'),
    path('tree/<int:tree_id>', views.get_tree, name='get_tree'),
    path('full_tree/<int:tree_id>', views.get_full_tree, name='get_full_tree'),
    path('front/', views.from_frontend, name='from_frontend'),
]