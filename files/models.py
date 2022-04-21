from django.db import models
from django.utils import timezone


class File(models.Model):
    file = models.FileField(upload_to="files", null=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    
    class Meta:
        ordering = ["created_at"]
        verbose_name = ("File")
        verbose_name_plural = ("Files")