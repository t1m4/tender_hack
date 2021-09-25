# Generated by Django 3.2.7 on 2021-09-25 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210925_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cte',
            name='cte_product',
        ),
        migrations.AddField(
            model_name='cte',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.contract'),
        ),
        migrations.AddField(
            model_name='cte_product',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.cte'),
        ),
    ]