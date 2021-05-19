from django.db import models


# Create your models here.
class CommandElem(models.Model):
    command = models.TextField()
    script = models.FileField(upload_to="action/")

    def __str__(self):
        return f"{self.command}"
