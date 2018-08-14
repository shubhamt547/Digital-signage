from django.db import models
from django.core.files.storage import default_storage
# Create your models here.
asset_types = (
    ('I', 'Image'),
    ('V', 'Video')
)


class Asset(models.Model):
    name = models.TextField()
    source = models.FileField(upload_to="uploads/", storage=default_storage)
    type = models.CharField(choices=asset_types,max_length=2)
    start_date = models.DateTimeField()
    active = models.BooleanField(default=False)
    end_date = models.DateTimeField()
    changed_time=models.DateTimeField(null=True)
    duration = models.IntegerField(default=15)


    def __str__ (self):
        return self.name


