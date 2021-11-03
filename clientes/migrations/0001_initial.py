# Generated by Django 3.2.7 on 2021-10-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('altura', models.FloatField(max_length=4)),
                ('peso', models.FloatField(max_length=6)),
                ('endereco', models.CharField(max_length=300)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/')),
                ('obs', models.TextField(max_length=400)),
            ],
        ),
    ]
