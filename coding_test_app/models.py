from django.db import models

# Create your models here.

class TimestampedValue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField()
    value = models.IntegerField()

    class Meta:
        db_table = "timestamped_values"