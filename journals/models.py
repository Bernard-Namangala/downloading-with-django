from django.db import models


class Journal(models.Model):
    name = models.CharField(max_length=25)
    file = models.FileField(upload_to="journals/")
    download_count = models.IntegerField(default=0)
