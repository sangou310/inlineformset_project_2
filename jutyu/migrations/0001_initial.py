# Generated by Django 3.0.8 on 2020-07-10 05:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='顧客名')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='部品コード')),
                ('name', models.CharField(max_length=50, verbose_name='部品名')),
            ],
        ),
        migrations.CreateModel(
            name='JutyuHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jutyu_date', models.DateField(default=datetime.date.today, verbose_name='受注日')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jutyu.Customer', verbose_name='顧客')),
            ],
        ),
        migrations.CreateModel(
            name='JutyuDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='受注数量')),
                ('jutyu_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jutyu.JutyuHead')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jutyu.Part', verbose_name='部品')),
            ],
        ),
    ]
