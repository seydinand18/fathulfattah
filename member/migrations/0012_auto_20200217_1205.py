# Generated by Django 3.0.3 on 2020-02-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_auto_20200217_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='register_date',
            field=models.DateField(blank=True),
        ),
    ]
