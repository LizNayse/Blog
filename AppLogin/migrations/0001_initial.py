# Generated by Django 4.1.7 on 2023-04-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=256)),
                ('contrasenia', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
