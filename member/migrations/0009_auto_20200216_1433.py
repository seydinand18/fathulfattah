# Generated by Django 3.0.3 on 2020-02-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20200216_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='code_member',
            field=models.CharField(blank=True, default='DFF120190001', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_addr',
            field=models.CharField(blank=True, default='Bambey', max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='home_addr',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='identity_photo',
            field=models.ImageField(blank=True, upload_to=None, verbose_name='identity'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mariage_status',
            field=models.CharField(blank=True, choices=[('S', 'Célibataire'), ('C', 'Marié(e)'), ('D', 'Divorcé(e)'), ('W', 'Veuf(ve)')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number1',
            field=models.CharField(blank=True, default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number2',
            field=models.CharField(blank=True, default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='member',
            name='place_birth',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
