# Generated by Django 3.2.7 on 2021-09-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210925_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cte',
            name='contract',
        ),
        migrations.AddField(
            model_name='cte',
            name='contract',
            field=models.ManyToManyField(null=True, to='core.Contract'),
        ),
    ]