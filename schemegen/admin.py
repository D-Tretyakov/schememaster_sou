from django.contrib import admin

from .models import Tree, Choice, Variant, Schema

admin.site.register(Tree)
admin.site.register(Choice)
admin.site.register(Variant)
admin.site.register(Schema)