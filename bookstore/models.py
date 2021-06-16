from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    # Propiedades
    author_id = models.BigAutoField(primary_key=True) # ID automática, aumenta 1 en cada registro nuevo
    name = models.CharField(max_length=100)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    # Método mágico
    def __str__(self):
        return self.name

class Book(models.Model):
    # Propiedades
    book_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta 1 en cada registro nuevo
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title