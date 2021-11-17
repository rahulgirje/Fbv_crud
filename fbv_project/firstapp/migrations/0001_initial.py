# Generated by Django 3.2.9 on 2021-11-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
