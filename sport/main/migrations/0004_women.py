# Generated by Django 4.0.2 on 2022-03-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullnamew', models.CharField(max_length=50)),
                ('photow', models.TextField(max_length=20000)),
                ('textw', models.TextField(max_length=15000)),
            ],
        ),
    ]