from django.db import models

from backend import settings
from labels.models import Label


class Note(models.Model):
    COLOR_CHOICES = [
        ('#ffffff', 'White'),
        ('#fef3c7', 'Yellow'),
        ('#e0f2fe', 'Blue'),
        ('#dcfce7', 'Green'),
        ('#fce7f3', 'Pink'),
        ('#fee2e2', 'Red'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return str(self.id) + ": " + self.title
