# Generated by Django 3.0.3 on 2020-02-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20200216_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='code_member',
            field=models.CharField(default='DFF120190001', max_length=20, null=True),
        ),
    ]