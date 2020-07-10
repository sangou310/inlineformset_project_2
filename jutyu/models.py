from datetime import date

from django.db import models


class Customer(models.Model):
    name = models.CharField('顧客名', max_length=50)

    def __str__(self):
        return self.name


class Part(models.Model):
    code = models.CharField('部品コード', max_length=15)
    name = models.CharField('部品名', max_length=50)

    def __str__(self):
        return f'{self.code} / {self.name}'


class JutyuHead(models.Model):
    jutyu_date = models.DateField('受注日', default=date.today)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='顧客')


class JutyuDetail(models.Model):
    jutyu_head = models.ForeignKey(JutyuHead, models.CASCADE)
    part = models.ForeignKey(Part, models.CASCADE, verbose_name='部品')
    quantity = models.IntegerField('受注数量')
