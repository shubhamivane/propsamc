from django.db import models

# Create your models here.

class API(models.Model):
    key = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
