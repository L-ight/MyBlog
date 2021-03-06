# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 12:55
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tag', '0001_initial'),
        ('Classification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('created_Datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_Datetime', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='content')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Classification.Classification')),
                ('tag', models.ManyToManyField(blank=True, to='Tag.Tag')),
            ],
        ),
    ]
