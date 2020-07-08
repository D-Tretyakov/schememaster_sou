from django.db import models

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice_text

class Variant(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    variant_text = models.CharField(max_length=200)
    text_repr = models.TextField()

    def __str__(self):
        return self.variant_text
