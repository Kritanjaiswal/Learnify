# contact_app/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    suggestion = models.TextField()

    def __str__(self):
        return self.subject

