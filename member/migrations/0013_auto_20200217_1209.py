# Generated by Django 3.0.3 on 2020-02-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20200217_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='register_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
