from django.db import models

class ScaleLabel(models.Model):
    description = models.TextField(default='')
    name = models.CharField(max_length=128, default='')
    class Meta:
        """Meta definition for ScaleLabel."""

        verbose_name =  'ScaleLabel'
        verbose_name_plural =  'ScaleLabel'

    def __str__(self):
        """Unicode representation of ScaleLabel."""
        pass