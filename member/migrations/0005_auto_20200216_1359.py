# Generated by Django 3.0.3 on 2020-02-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20200216_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
