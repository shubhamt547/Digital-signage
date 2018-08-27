from django.db import models
from django.core.files.storage import default_storage
import os
from django.dispatch import receiver

# Create your models here.
asset_types = (
    ('I', 'Image'),
    ('V', 'Video')
)


class Asset(models.Model):
    name = models.TextField()
    source = models.FileField(upload_to="uploads/", storage=default_storage)
    type = models.CharField(choices=asset_types, max_length=2)
    start_date = models.DateTimeField()
    active = models.BooleanField(default=False)
    end_date = models.DateTimeField()
    changed_time = models.DateTimeField(null=True)
    duration = models.IntegerField(default=15)

    def __str__(self):
        return self.name



@receiver(models.signals.post_delete, sender=Asset)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.source:
        if os.path.isfile(instance.source.path):
            os.remove(instance.source.path)

@receiver(models.signals.pre_save, sender=Asset)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Asset.objects.get(pk=instance.pk).source
    except Asset.DoesNotExist:
        return False

    new_file = instance.source
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
