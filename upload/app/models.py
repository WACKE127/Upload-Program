from django.db import models
import uuid
import os

class UploadHandler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='uploads/')  # This is the actual uploaded file
    file_name = models.CharField(max_length=255, blank=True)  # Optional as requested
    file_path = models.TextField(editable=False)
    file_size = models.BigIntegerField(editable=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True, blank=True)
    permissions = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = os.path.basename(self.file.name)
        self.file_path = self.file.path
        self.file_size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name
