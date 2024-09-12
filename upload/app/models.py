from django.db import models

# Create your models here.
class UploadHander(models.Model):
    timestamp = models.DateTimeField(auto_now_add=true)
    file = models.FileField(upload_to='media/')