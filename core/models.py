from django.db import models


class CTE(models.Model):
    cte_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=2048, null=True)
    category = models.CharField(max_length=2048, null=True)
    code_kphz = models.CharField(max_length=2048, null=True)


# Create your models here.
class CTE_product(models.Model):
    name = models.CharField(max_length=1024, null=True)
    cte_product_id = models.BigIntegerField(null=True)
    value = models.CharField(max_length=1024, null=True)
    cte = models.ForeignKey(CTE, on_delete=models.DO_NOTHING, null=True)


# ['Номер контракта', 'Дата публикации КС на ПП', 'Дата заключения контракта', 'Цена контракта', 'ИНН заказчика',
# 'КПП заказчика', 'Наименование заказчика', 'ИНН поставщика', 'КПП поставщика', 'Наименование поставщика', 'СТЕ']
class Contract(models.Model):
    number = models.IntegerField()
    public_date = models.DateTimeField()
    close_date = models.DateTimeField()
    price = models.FloatField()
    сustomer_inn = models.IntegerField()
    сustomer_kpp = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    supplier_inn = models.IntegerField()
    supplier_kpp = models.IntegerField()
    supplier_name = models.CharField(max_length=255)
    products = models.ForeignKey(CTE, on_delete=models.DO_NOTHING)
