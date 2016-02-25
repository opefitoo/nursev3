# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.JobPosition'),
        ),
    ]
