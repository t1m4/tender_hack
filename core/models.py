from django.db import models

# ['Номер контракта', 'Дата публикации КС на ПП', 'Дата заключения контракта', 'Цена контракта', 'ИНН заказчика',
# 'КПП заказчика', 'Наименование заказчика', 'ИНН поставщика', 'КПП поставщика', 'Наименование поставщика', 'СТЕ']
class Contract(models.Model):
    number = models.CharField(max_length=255, null=True)
    public_date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
    сustomer_inn = models.BigIntegerField(null=True)
    сustomer_kpp = models.BigIntegerField(null=True)
    customer_name = models.CharField(max_length=255, null=True)
    supplier_inn = models.BigIntegerField(null=True)
    supplier_kpp = models.BigIntegerField(null=True)
    supplier_name = models.CharField(max_length=255, null=True)

class ContractCTE(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.BigIntegerField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)


class CTE(models.Model):
    cte_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=2048, null=True)
    category = models.CharField(max_length=2048, null=True)
    code_kphz = models.CharField(max_length=2048, null=True)
    contract_cte = models.ForeignKey(ContractCTE, on_delete=models.SET_NULL, null=True, blank=True)


# Create your models here.
class CTE_product(models.Model):
    name = models.CharField(max_length=1024, null=True)
    cte_product_id = models.BigIntegerField(null=True)
    value = models.CharField(max_length=1024, null=True)
    contract = models.ForeignKey(CTE, on_delete=models.SET_NULL, null=True)
