# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 11:01
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
import invoices

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name=b'montant brut')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_contract', models.DateField(verbose_name=b'start date')),
                ('end_contract', models.DateField(verbose_name=b'end date')),
                ('occupation', models.TextField(max_length=30)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=invoices.models.get_default_invoice_number, max_length=50)),
                ('accident_id', models.CharField(blank=True, help_text="Numero d'accident est facultatif", max_length=30, null=True)),
                ('accident_date', models.DateField(blank=True, help_text="Date d'accident est facultatif", null=True)),
                ('invoice_date', models.DateField(verbose_name=b'Invoice date')),
                ('patient_invoice_date', models.DateField(verbose_name=b'Date envoi au patient  ')),
                ('invoice_sent', models.BooleanField()),
                ('invoice_paid', models.BooleanField()),
                ('medical_prescription_date', models.DateField(blank=True, null=True, verbose_name=b'Date ordonnance')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_sn', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('participation_statutaire', models.BooleanField()),
                ('private_patient', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=b'date')),
                ('carecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.CareCode')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateInvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=invoices.models.get_default_invoice_number, max_length=50)),
                ('accident_id', models.CharField(blank=True, help_text="Numero d'accident est facultatif", max_length=30, null=True)),
                ('accident_date', models.DateField(blank=True, help_text="Date d'accident est facultatif", null=True)),
                ('invoice_date', models.DateField(verbose_name=b'Date facture')),
                ('invoice_send_date', models.DateField(blank=True, null=True, verbose_name=b'Date envoi facture')),
                ('medical_prescription_date', models.DateField(blank=True, null=True, verbose_name=b'Date ordonnance')),
                ('invoice_sent', models.BooleanField()),
                ('invoice_paid', models.BooleanField()),
                ('prestations', models.ManyToManyField(blank=True, editable=False, related_name='private_invoice_prestations', to='invoices.Prestation')),
                ('private_patient', models.ForeignKey(help_text=b'choisir parmi ces patients pour le mois precedent', on_delete=django.db.models.deletion.CASCADE, related_name='private_invoice_patient', to='invoices.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='patient',
            field=models.ForeignKey(help_text=b'choisir parmi ces patients pour le mois precedent', on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='invoices.Patient'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='prestations',
            field=models.ManyToManyField(blank=True, editable=False, related_name='prestations', to='invoices.Prestation'),
        ),
    ]
