from django.contrib import admin

from .models import Tree, Choice, Variant, Schema, Template, TextAlias

admin.site.register(Tree)
admin.site.register(Choice)
admin.site.register(Variant)
admin.site.register(Schema)
admin.site.register(Template)
admin.site.register(TextAlias)
