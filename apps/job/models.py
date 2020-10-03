from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title