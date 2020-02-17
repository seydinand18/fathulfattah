from django.db import models
from django.contrib.auth.models import User

class Cell(models.Model):

    cell_label = models.CharField(max_length=40)
    cell_addr = models.CharField(max_length=40)
    cell_link_map = models.URLField(max_length=255)
    
    def __str__(self):
        return "Cellule " + self.cell_label
   