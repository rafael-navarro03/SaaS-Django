from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # DB -> Tabela
    # id -> primary key -> autofield = 1, 2, 3, 4, ...
    path = models.TextField(blank=True, null=True)          # Coluna
    timestamp = models.DateTimeField(auto_now_add=True)     # Coluna

    