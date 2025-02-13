from django.db import models

# Create your models here.
class History(models.Model):
    user_input = models.CharField(max_length=1000)
    api_output = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_input
    