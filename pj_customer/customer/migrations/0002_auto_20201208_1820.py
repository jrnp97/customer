# Generated by Django 3.1.4 on 2020-12-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
