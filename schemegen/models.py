from django.db import models


# class Tree(models.Model):
#     name = models.CharField(max_length=400)

#     def __str__(self):
#         return self.name

# class Choice(models.Model):
#     choice_text = models.CharField(max_length=200)
#     tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
#     multiple = models.BooleanField()

#     def __str__(self):
#         return self.choice_text

# class Variant(models.Model):
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
#     variant_text = models.CharField(max_length=200)
#     text_repr = models.TextField()

#     def __str__(self):
#         return self.variant_text

# class Schema(models.Model):
#     tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
#     text_repr = models.TextField()

#     def __str__(self):
#         return f'Schema for \'{self.tree.name}\''

class Template(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField()
    body = models.TextField()
    footer = models.TextField()

    def __str__(self):
        return 'Template: ' + self.name

class TextAlias(models.Model):
    html_id = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return f'{self.html_id}: {self.text}'
