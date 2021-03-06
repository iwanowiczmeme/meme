from django.db import models
from django.contrib.auth.models import User


class InputSignal(models.Model):

    name = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    adnotations = models.TextField(blank=True, null=True)
    input_file = models.FileField(upload_to='signals/', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
