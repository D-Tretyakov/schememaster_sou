# Generated by Django 3.0.7 on 2020-07-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemegen', '0004_variant_text_repr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
    ]