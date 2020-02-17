from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):

    MAN = 'M'
    WOMAN = 'W'
    SEX = [
        (MAN,'Serigne'),
        (WOMAN,'Soxna'),
    ]

    SIGLE = 'S'
    COUPLE = 'C'
    DIVORCED = 'D'
    WIDOWER = 'W'
    MARIAGE_STATUS = [
        (SIGLE,'Célibataire'),
        (COUPLE,'Marié(e)'),
        (DIVORCED,'Divorcé(e)'),
        (WIDOWER,'Veuf(ve)'),
    ]

    code_member = models.CharField(max_length=20, default='DFF120190001',blank=True)
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    birth_date = models.DateField(blank=True, null=True)
    place_birth = models.CharField(max_length=150, default='',blank=True)
    sex = models.CharField(max_length=1,choices=SEX, default=MAN)
    mariage_status = models.CharField(max_length=1, choices=MARIAGE_STATUS, blank=True, default=SIGLE)
    register_date = models.DateField(blank=True, null=True)
    home_addr = models.CharField(max_length=150, default='', blank=True)
    current_addr = models.CharField(max_length=150, default='Bambey',blank=True)
    identity_photo = models.ImageField(("identity"), upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    phone_number1 = models.IntegerField(blank=True, null=True)
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, default='',blank=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name +" "+ self.last_name
   