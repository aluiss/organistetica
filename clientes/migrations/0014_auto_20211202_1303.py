# Generated by Django 3.2.9 on 2021-12-02 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_alter_anamnese_alergia_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnese',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 2, 13, 3, 18, 391581)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='filhos_qt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='peso',
            field=models.FloatField(max_length=7),
        ),
    ]
