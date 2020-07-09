from rest_framework import serializers

from .models import Tree, Choice, Variant, Schema


class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree
        fields = '__all__'

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class VariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class SchemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schema
        fields = '__all__'