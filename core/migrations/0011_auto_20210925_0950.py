# Generated by Django 3.2.7 on 2021-09-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='supplier_inn',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='supplier_kpp',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='сustomer_inn',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='сustomer_kpp',
            field=models.BigIntegerField(),
        ),
    ]
