# Generated by Django 3.2 on 2021-06-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verb',
            name='future',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='verb',
            name='meaning',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='verb',
            name='past',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='verb',
            name='present',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='verb',
            name='word',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
